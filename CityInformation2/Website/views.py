from django.http import Http404
from django.shortcuts import render
from django.template import loader
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import View
from django.views import generic
from .forms import UserForm, LoginForm, SearchForm



class IndexView(generic.ListView):
    #template should be 'Website/index.html'
    template_name = 'Website/index.html'
    context_object_name = 'facility_list'
    queryset = LocationInfo.objects.all()
    #context_object_name = 'stuff_list'
    #queryset = LocationInfo.objects.all()

##    def city_map(request, city_name):
##        try:
##            city = City.objects.get(name=city_name)
##        except City.DoesNotExist:
##            raise Http404("City does not exist")
##        return render(request, 'Website/city.html', {'city': city})

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['college_list'] = LocationInfo.objects.filter(infoType=InfoTypes.College.value,
                                                              city__name__contains="Brisbane")
        return context


#     queryset = Library.objects.all()
#
#     def get_context_data(self, **kwargs):
#         context = super(IndexView, self).get_context_data(**kwargs)
#         context['college_list'] = College.objects.all()
#         context['mall_list'] = Mall.objects.all()
#         context['hotel_list'] = Hotel.objects.all()
#         return context

class DetailView(generic.DetailView):
    model = LocationInfo
    template_name = 'Website/detail.html'

########## Need to combine these two functions ##############

# process Brisbane info and city map in html 
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

################################################################

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
    context_object_name = 'facility_list'
    queryset = LocationInfo.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CityView, self).get_context_data(**kwargs)
        context['college_list'] = LocationInfo.objects.all()
        return context

##    def city_map(request, city_name):
##        try:
##            city = City.objects.get(name=city_name)
##        except City.DoesNotExist:
##            raise Http404("City does not exist")
##        return render(request, template_name, {'city': city})

def Search(request):
    template_name = 'Website/search.html'
   
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
        
            search_name = form.cleaned_data['search_name']
            info_type = form.cleaned_data['info_type']

            if info_type == '9':
                search = LocationInfo.objects.filter(name=search_name)
            else:
                search = LocationInfo.objects.filter(name=search_name).filter(infoType=info_type)
        else:
            search = LocationInfo.objects.all()
            match = 1
            return render(request, template_name, {'search': search, 'match': match})
        
    return render(request, template_name, {'search': search})

