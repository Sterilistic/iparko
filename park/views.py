from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
import requests
from django.contrib.auth import login,logout, authenticate
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions
# import json
# from park.forms import LoginForm
# from park.models import register_user

# Create your views here.

class getUser(APIView):
    # allow this API call only if user has logged in
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, format=None):
        user = request.user
        userId = user.username
        return Response(userId)

def home(request):
	#context = {'latest_question_list': "latest_question_list"}
	if not request.user.is_authenticated():
		print 'iski ma ka login ni hua'
		return render(request, 'account/login.html')
	return render(request, 'home.html')

def user_logout(request):
	logout(request)
	return redirect('/')		


















# def reg(request):
# 	form = LoginForm() 
# 	if request.method == 'POST':
# 		form = LoginForm(request.POST)
# 		if form.is_valid():
# 			username = request.POST.get('username', '')
# 			email = request.POST.get('email', '')
# 			password = request.POST.get('password', '')
# 			cnfm_pass = request.POST.get('cnfm_pass', '')
# 			register_user_obj = register_user(username=username,email=email,password=password,cnfm_pass=cnfm_pass)
# 			register_user_obj.save()

# 			return HttpResponseRedirect('/')

	# 	else:
	# 		return HttpResponseRedirect('index.html')
	# 		#form = LoginForm()

	# return render(request, 'signup.html', { 'form': form ,})

