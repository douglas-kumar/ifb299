from django.http import Http404
from django.shortcuts import render
from django.template import loader
from .models import College
from .models import City
from .models import Profile
from .models import Mall
from .models import Library
from .models import Hotel
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import View
from django.views import generic
from .forms import UserForm, LoginForm


class IndexView(generic.ListView):
    template_name = 'Website/index.html'
    context_object_name = 'stuff_list'
    queryset = Library.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['college_list'] = College.objects.all()
        context['mall_list'] = Mall.objects.all()
        context['hotel_list'] = Hotel.objects.all()
        return context

class DetailView(generic.DetailView):
    model = College
    template_name = 'Website/detail.html'

def brisbane(request, city_name):
    try:
        city = City.objects.get(name=city_name)
    except City.DoesNotExist:
        raise Http404("City does not exist")
    return render(request, 'Website/brisbane.html', {'city': city})

class UserFormView(View):
    form_class = UserForm
    template_name = 'Website/registration_form.html'

    #display blank forms
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            account_type = form.cleaned_data['account_type']
            
            
            user.set_password(password)
            user.save()
            
            #get user object to add account_type - get userId to get profile - silly work around, probably some other way to do it
            
            user_acc = User.objects.get(username=username)
            user_pk = user_acc.pk
            user_acc2 = Profile.objects.get(user_id=user_pk)
            user_acc2.user_type = account_type
            user_acc2.save()

            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/Website/')

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
