from django.http import Http404
from django.shortcuts import render
from django.template import loader
from .models import *
from django.shortcuts import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import View
from django.views import generic
from .forms import *
import re



class IndexView(generic.ListView):
    template_name = 'Website/index.html'
    queryset = LocationInfo.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['college_list'] = LocationInfo.objects.filter(
            infoType=InfoTypes.College.value,
            city__name__contains="Brisbane")
        context['hotel_list'] = LocationInfo.objects.filter(
            infoType=InfoTypes.Hotel.value,
            city__name__contains="Brisbane")
        context['mall_list'] = LocationInfo.objects.filter(
            infoType=InfoTypes.Mall.value,
            city__name__contains="Brisbane")
        return context

class DetailView(generic.DetailView):
    model = LocationInfo
    form_class = ReviewForm
    template_name = 'Website/detail.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(None)
        number = re.sub("[^0-9]", "", request.path)
        place_id = int(number)
        location_info = self.model.objects.get(pk=place_id)
        reviews = Review.objects.filter(place=location_info)
        context = {
            'locationinfo' : location_info,
            'review' : reviews,
            'form' : form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if (form.is_valid()):
            number = re.sub("[^0-9]", "", request.path)
            place_id = int(number)
            rating = form.cleaned_data['rating']
            text = form.cleaned_data['text']

            user = Profile.objects.get(user_id=request.user)
            place = LocationInfo.objects.get(pk=place_id)
            review = Review.create(user, place, rating, text)
            review.save()
            reviews = Review.objects.filter(place=place)
            context = {
                'form' : form,
                'locationinfo': place,
                'review' : reviews,
            }
            return render(request, self.template_name, context)

def city_page(request, city_name):
        city = City.objects.get(name=city_name)
        location_info = LocationInfo.objects.filter(city=city.id)
        context = {
            'city' : city,
            'location_info' : location_info,
        }
        return render(request, 'Website/city.html', context)

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
    context_object_name = 'location_info'
    model = LocationInfo
    user = Profile

    def get_queryset(self):
        self.city_name = self.kwargs['city_name']
        queryset = super(CityView, self).get_queryset()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(CityView, self).get_context_data(**kwargs)
        context['the_city'] = City.objects.get(name=self.city_name)
        context['city_id'] = self.model.objects.filter(
            city=context['the_city'].id)
        context['city_colleges'] = self.model.objects.filter(
            infoType=InfoTypes.College.value,
            city__name__contains=self.city_name)
        context['city_malls'] = self.model.objects.filter(
            infoType=InfoTypes.Mall.value,
            city__name__contains=self.city_name)
        context['city_hotels'] = self.model.objects.filter(
            infoType=InfoTypes.Hotel.value,
            city__name__contains=self.city_name)
        context['city_libraries'] = self.model.objects.filter(
            infoType=InfoTypes.Library.value,
            city__name__contains=self.city_name)
        context['city_industries'] = self.model.objects.filter(
            infoType=InfoTypes.Indusry.value,
            city__name__contains=self.city_name)
        context['city_parks'] = self.model.objects.filter(
            infoType=InfoTypes.Park.value,
            city__name__contains=self.city_name)
        context['city_zoos'] = self.model.objects.filter(
            infoType=InfoTypes.Zoo.value,
            city__name__contains=self.city_name)
        context['city_museums'] = self.model.objects.filter(
            infoType=InfoTypes.Museum.value,
            city__name__contains=self.city_name)
        context['city_restaurants'] = self.model.objects.filter(
            infoType=InfoTypes.Restaurant.value,
            city__name__contains=self.city_name)
        context['city_info'] = self.model.objects.all()
        return context
    
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

def review(request):
    template_name = 'Website/detail.html'

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():

            user = Profile.objects.get(user_id=request.user)
            number = re.sub("[^0-9]", "", request.path)
            place = LocationInfo.objects.get(pk=1)
            rating = form.cleaned_data['rating']
            text = form.cleaned_data['text']

            review = Review.create(user, place, rating, text)
            review.save()
            reviews = Review.objects.filter(place=place)
            context = {
                'form' : form,
                'locationinfo': place,
                'review' : reviews,
                'user' : user,
            }

        return render(request, template_name, context)

class ReviewFormView(View):
    model = LocationInfo
    form_class = ReviewForm
    template_name = 'Website/detail.html'

    def get(self, request, *args, **kwargs):
        user = Profile.objects.get(user_id=request.user)
        number = re.sub("[^0-9]", "", request.path)
        place_id = int(number)
        form = self.form_class(None)
        location_info = self.model.objects.get(pk=place_id)
        reviews = Review.objects.filter(place=location_info)
        context = {
            'location_info' : location_info,
            'form' : form,
            'review' : reviews,
            'user' : user,
        }
        return render(request, self.template_name, context)
 
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if (form.is_valid()) and (request.user.is_authenticated()):

            number = re.sub("[^0-9]", "", request.path)
            place_id = int(number)
            rating = form.cleaned_data['rating']
            text = form.cleaned_data['text']

            user = Profile.objects.get(user_id=request.user)
            place = LocationInfo.objects.get(pk=place_id)
            review = Review.create(user, place, rating, text)
            review.save()
            reviews = Review.objects.filter(place=place)
            context = {
                'form' : form,
                'location_info': place,
                'review' : reviews,
                'user' : user,
            }
            return render(request, self.template_name, context)
