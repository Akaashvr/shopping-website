from django.shortcuts import render

# Create your views here.
def main(request):
	return render(request, "main.html")

def electronics(request):
	return render(request, "electronics.html")

def Mfashion(request):
	return render(request, "men.html")

def Wfashion(request):
	return render(request, "women.html")

def beauty(request):
	return render(request, "beauty.html")

def about(request):
	return render(request, "about.html")

def hplap(request):
	return render(request, "hplap.html")

def oneplus(request):
	return render(request, "oneplus.html")
