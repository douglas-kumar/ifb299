from django.http import Http404
from django.shortcuts import render
from django.template import loader
from .models import College
from .models import City
from .models import Profile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import View
from django.views import generic
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'Website/index.html'
    context_object_name = 'college_list'

    def get_queryset(self):
        return College.objects.all()

class DetailView(generic.DetailView):
    model = College
    template_name = 'Website/detail.html'

# process Brisbane info and city map in html 
def brisbane(request, city_name):
    try:
        city = City.objects.get(name=city_name)
    except City.DoesNotExist:
        raise Http404("City does not exist")
    return render(request, 'Website/brisbane.html', {'city': city})

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
                    return redirect('/Website/')

        return render(request, self.template_name, {'form': form})
