from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r"^sign_up/$", views.sign_up, name="sign_up"),
    url(r'^login/$', views.mylogin, name='mylogin'),
    url(r'^logout/$', views.mylogout, name='mylogout'),
    url(r'^panel/$', views.panel, name='panel'),
    url(r'^panel/kalender/$', views.kalender, name='kalender'),
    url(r'^panel/daftarkegiatan/$', views.daftarkegiatan, name='daftarkegiatan'),
    url(r'^panel/stickynotes/$', views.stickynotes, name='stickynotes'),

] 