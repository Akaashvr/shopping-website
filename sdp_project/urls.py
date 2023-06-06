
from django.contrib import admin
from django.urls import path
from shopping_app.views import main, electronics, Mfashion, Wfashion, beauty, about, hplap, oneplus
from au_app.views import ulogin, ulogout, usignup
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",main,name="main"),
    path("usignup/", usignup, name="usignup"),
    path("ulogin/", ulogin, name="ulogin"),
    path("ulogout/", ulogout, name="ulogout"),
    path("electronics/", electronics, name="electronics"),
    path("Mfashion/", Mfashion, name="Mfashion"),
    path("Wfashion/", Wfashion, name="Wfashion"),
    path("beauty/", beauty, name="beauty"),
    path("hplap/", hplap, name="hplap"),
    path("oneplus/", oneplus, name="oneplus"),
    path("about/", about, name="about"),
    
]
urlpatterns += staticfiles_urlpatterns()
