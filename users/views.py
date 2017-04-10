from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from .models import BlogPost, Tag
from .forms import LoginForm,RegistrationForm
#from . import services
from .decorators import anonymous_required
from django.template import RequestContext
from django.shortcuts import render_to_response


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            return redirect(reverse('simpleofferts:index'))
    form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
    return render(request, 'users/register.html', locals())


@anonymous_required(profile_url=reverse_lazy('simpleofferts:index'))
def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = authenticate(**form.cleaned_data)

            if user is None:
                form.add_error(field='', error='No such user')
            else:
                login(request, user)
                return redirect(reverse('simpleofferts:index'))
                #return render(request, 'users/profile.html', locals())

    return render(request, 'users/login.html', locals())


def logout_user(request):
    logout(request)
    return redirect(reverse('simpleofferts:index'))



# login_required_views = [profile_view]


# for view in login_required_views:
#     fname = view.__name__
#     local_definitions = locals()

#     f = local_definitions.get(fname)

#     f = login_required(f)

#     local_definitions[fname] = f

