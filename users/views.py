from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/healthApp/homepage/') # redirect to a path not template

    form = NewUserForm()
    context = {
        'form':form
    }
    return render(request, 'users/register.html', context=context)

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def editprofile(request):
    if request.method == 'POST':
        image = request.FILES['upload']
        contact_number = request.POST.get('contact_number')
        user = request.user
        # Add data to databse
        profile = Profile(image=image, contact_number=contact_number, user=user)
        profile.save()
        return redirect('/users/profile/')
    return render(request, 'users/editprofile.html')
