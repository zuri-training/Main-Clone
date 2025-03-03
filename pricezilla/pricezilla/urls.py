
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/',views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('contact/',views.contact, name="contact"),
    path('account/', views.account, name='account'),
    path('sign-up/', views.sign, name='sign'),
    path('search/', views.searchbar, name='search'),
    path('product/', include('product.urls')),
]

urlpatterns += staticfiles_urlpatterns()
