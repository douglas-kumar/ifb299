from django.http import Http404
from django.shortcuts import render
from django.template import loader
from .models import College
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


def index(request):
    all_college = College.objects.all()
    return render(request, 'Website/index.html', {'all_college': all_college})


def detail(request, college_id):
    try:
        college = College.objects.get(id=college_id)
    except College.DoesNotExist:
        raise Http404("College does not exist")
    return render(request, 'Website/detail.html', {'college': college})

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
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('Website:index')

        return render(request, self.template_name, {'form': form})
