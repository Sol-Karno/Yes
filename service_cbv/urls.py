from django.urls import path

from . import views

app_name = 'service_cbv'

urlpatterns = [
  path('', views.ServiceList.as_view(), name='service_list'),
  path('new/', views.ServiceCreate.as_view(), name='service_new'),
  path('edit/<int:pk>/', views.ServiceUpdate.as_view(), name='service_edit'),
  path('delete/<int:pk>/', views.ServiceDelete.as_view(), name='service_delete'),
]