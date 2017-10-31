from .models import Favorite
from .forms import FavoriteForm
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.middleware.csrf import get_token
from django.conf import settings 

class FavAlterView(FormView):

    """
    Enables authenticated users to Favorite/Unfavorite objects.
        getattr method sets default values for POSITIVE_NOTATION, 
    NEGATIVE_NOTATION, ALLOW_ANONYMOUS in the case they are not
    set in settings.py
    """

    form_class = FavoriteForm
    model = Favorite
    template_name = 'fav/fav_form.html'

    def form_valid(self, form):
        fav_value = self.request.POST['fav_value']
        csrf_token_value = get_token(self.request)
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        try:
            content_type = ContentType.objects.get(
                app_label=self.request.POST['app_name'],
                model=self.request.POST['model'].lower())
            model_object = content_type.get_object_for_this_type(
                id=self.request.POST['model_id'])
            if fav_value == getattr(settings, 'POSITIVE_NOTATION', 'Favorite'):
                fav = form.save(commit=False)
                fav.content_object = model_object
                if self.request.user.is_authenticated():
                    fav.save()
                else:
                    if getattr(settings, 'ALLOW_ANONYMOUS', 'TRUE') == "TRUE":
                        fav.cookie = self.request.session.session_key
                        fav.save()
                    else:
                        return JsonResponse({
                            'success': 0,
                            'error': "You have to sign in "})
                Favorite.objects.get(id=fav.id)
            else:
                if self.request.user.is_authenticated():
                    Favorite.objects.get(
                        object_id=model_object.id,
                        user=self.request.user,
                        content_type=content_type).delete()
                elif getattr(settings, 'ALLOW_ANONYMOUS', 'TRUE') == "TRUE":
                    Favorite.objects.get(
                        object_id=model_object.id,
                        cookie=self.request.session.session_key,
                        content_type=content_type).delete()
        except:
            return JsonResponse({
                'success': 0,
                'error': "You have to sign in "})
        return JsonResponse({"csrf": csrf_token_value})

    def form_invalid(self, form):
        return JsonResponse({
            'success': 0,
            'error': form.errors})
