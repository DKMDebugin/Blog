from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    # Log user in
    logout(request)
    return HttpResponseRedirect(reverse('blogs:home'))

def register(request):
    # register user
    if request.method != 'POST':
        # create empty form
        form = UserCreationForm()
    else:
        # submit filled form
        form = UserCreationForm(data = request.POST)

        if form.is_valid():
            new_user = form.save()
            # log user in & redirect to home page
            authenticated_user = authenticate(username= new_user.username,
                                password= request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('blogs:home'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
