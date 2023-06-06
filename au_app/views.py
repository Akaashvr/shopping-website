from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import ProfileModel
from django.contrib.auth import login, logout, authenticate
from random import randrange
import requests
# Create your views here.

def usignup(request):
	if request.method=="POST":
		un = request.POST.get("un")
		ph = request.POST.get("ph")
		try:
			usr = User.objects.get(username=un)
			return render(request, "usignup.html", {"msg":"username already registered"})
		except User.DoesNotExist:
			try:
				usr = ProfileModel.objects.get(phone=ph)
				return render(request, "usignup.html",{"msg":"phone number already registered"})
			except ProfileModel.DoesNotExist:
				pw = ""
				text = "123456789"
				for i in range(6):
					pw = pw + text[randrange(len(text))]
				print(pw)
				send_sms(ph, pw)
				usr = User.objects.create_user(username=un, password=pw)
				usr.save()
				pro = ProfileModel(phone=ph, user=usr)
				pro.save()
				return redirect("ulogin")
	else:
		return render(request, "usignup.html")


def ulogin(request):
	if request.method == "POST":
		un = request.POST.get("un")
		pw = request.POST.get("pw")
		usr = authenticate(username=un, password=pw)
		if usr is not None:
			login(request, usr)
			return redirect("main")
		else:
			return render(request, "ulogin.html",{"msg":"invalid login"})
	else:
		return render(request, "ulogin.html")
def ulogout(request):
	logout(request)
	return redirect("ulogin")

def send_sms(ph, pw):
	url = "https://www.fast2sms.com/dev/bulk"
	querystring = {
	"authorization":"TzKcel5I2DYtaMjO6Zb7VpqHmvgCFRkWArQPG8duSnJyB4h3sX2FGBNYjmXM4kqpwQKhV3isfy05Cx8P",
	"sender_id":"CHKSMS",
	"route":"p",
	"numbers":str(ph),
	"message" : "ur password is " + str(pw),
	"language" : "english",
	}

	headers = { 'cache-control': "no=cache" }
	response = requests.request("GET", url, headers=headers, params=querystring)
	print(response.text)
