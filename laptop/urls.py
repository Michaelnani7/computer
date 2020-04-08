from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('computers/', views.computers, name='computers'),
    path('computers/<int:pc_id>', views.detail, name='detail'),
    path('iphones/', views.iphones, name='iphones'),
    path('iphones/<int:set_id>', views.phone, name='phone')]