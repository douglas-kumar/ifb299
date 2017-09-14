from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, LoginForm
from .models import Album, Song

# Generic view for listing items on main page (index page)
class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'album_list'

    def get_queryset(self):
        return Album.objects.all()


# Generic view for showing details about an item (detail page)
class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


# Create new album via menu button
class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


# Update new album via edit button -or- /music/album/<album_id>/
class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


# Delete album via delete button
class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


# Login new user via /music/login
class LoginFormView(View):
    form_class = LoginForm
    template_name = 'music/login_form.html'

    # display blank form for user registration
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    # submits form information
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalised) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})



# Create new user via /music/register
class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # display blank form for user registration
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    # submits form information
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalised) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})


# Create new song tied to album
class SongCreate(CreateView):
    model = Song
    fields = ['album', 'song_title', 'is_favourite']


# Update song tied to album
class SongUpdate(UpdateView):
    model = Song
    fields = ['album', 'song_title', 'is_favourite']


# Delete song tied to album
class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('music:index')