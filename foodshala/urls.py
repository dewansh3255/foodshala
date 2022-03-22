from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('authentication', include('authentication.urls')),
    # path('login', views.login, name="login"),
    # path('register', views.register, name="register"),
    # path('donate', views.donate, name="donate"),
    # path('about', views.about, name="about"),
    # path('contact', views.contact, name="contact"),
    # path('blog', views.blog, name="blog"),
    # path('gallery', views.gallery, name="gallery"),
]