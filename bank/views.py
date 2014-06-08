from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from bank.forms import *

# Create your views here.
def index(request):
   
    return render(request, 'bank/index.html', {})

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
			user.last_name = form.cleaned_data['lastname']
			user.first_name = form.cleaned_data['firstname']
			user.save()

			new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
			login(request, new_user)
			return HttpResponseRedirect("/")
		else:
			form =  RegisterForm()
			return render(request, 'bank/register.html',
                      { 'user_form' :  form })

	else:

		return render(request, 'bank/register.html', {})


