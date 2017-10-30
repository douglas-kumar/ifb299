from django.http import Http404
from django.shortcuts import render
from django.template import loader
from .models import *
from django.shortcuts import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import View
from django.views import generic
from .forms import UserForm, LoginForm, SearchForm

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


class IndexView(generic.ListView):
    template_name = 'Website/index.html'
    context_object_name = 'facility_list'
    queryset = LocationInfo.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['college_list'] = LocationInfo.objects.filter(infoType=InfoTypes.College.value,
                                                              city__name__contains="Brisbane")
        return context

class DetailView(generic.DetailView):
    model = LocationInfo
    template_name = 'Website/detail.html'

def city_page(request, city_name):
        city = City.objects.get(name=city_name)
        location_info = LocationInfo.objects.filter(city=city.id)
        context = {
            'city' : city,
            'location_info' : location_info,
        }
        return render_to_response('Website/city.html', context)

class UserFormView(View):
    form_class = UserForm
    template_name = 'Website/registration_form.html'

    # display blank forms
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            account_type = form.cleaned_data['account_type']
            
            user.set_password(password)
            user.save()
            
            # get user object to add account_type - get userId to get profile
            user_acc = User.objects.get(username=username)
            user_pk = user_acc.pk
            user_acc_profile = Profile.objects.get(user_id=user_pk)
            user_acc_profile.user_type = account_type
            user_acc_profile.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/Website/Brisbane') #change Brisbane

        return render(request, self.template_name, {'form': form})

class LoginFormView(View):
    form_class = LoginForm
    template_name = 'registration/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/Website/')

        return render(request, self.template_name, {'form': form})

def LogOut(request):
    logout(request)
    template_name = 'registration/logged_out.html'
    return render(request, template_name)

class CityView(generic.ListView):
    template_name = 'Website/city.html'
    context_object_name = 'info_list'
    queryset = LocationInfo.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CityView, self).get_context_data(**kwargs)
        context['city_info_list'] = LocationInfo.objects.all()
        return context

    def city_map(request, city_name):
        try:
            city = City.objects.get(name=city_name)
        except City.DoesNotExist:
            raise Http404("City does not exist")
        return render(request, 'Website/city.html', {'city': city})

    # read all info related to the city
    def city_info(request, city_id):
        try:
            location_info = LocationInfo.objects.filter(city=city_id)
        except LocationInfo.DoesNotExist:
            raise Http404("Item not found")
        return render(request, 'Website/city.html', {'location_info': location_info})

def Search(request):
    template_name = 'Website/search.html'
   
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
        
            search_name = form.cleaned_data['search_name']
            info_type = form.cleaned_data['info_type']
            sorting_options = form.cleaned_data['sorting_options']

            if info_type == '9':
                search = LocationInfo.objects.filter(name=search_name).order_by(sorting_options)
            else:
                search = LocationInfo.objects.filter(name=search_name).filter(infoType=info_type).order_by(sorting_options)
        else:
            search = LocationInfo.objects.all()
            match = 1
            return render(request, template_name, {'search': search, 'match': match})
        
    return render(request, template_name, {'search': search})

