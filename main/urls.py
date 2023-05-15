from django.urls import path
from . views import *
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('about', views.about, name='about'),
    path('catalog', views.catalog, name='catalog'),
    path('feedback', views.feedback, name='feedback'),
    path('service_cbv', views.service_cbv, name='service_cbv'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('category/<slug:cat_slug>/', Category.as_view(), name='category'),
]