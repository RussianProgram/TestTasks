from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HostListView.as_view(), name='users_host_list'),
    path('user/create_host', views.CreateHostView.as_view(), name='user_create_host'),
    path('user/update/<int:pk>', views.UserUpdateHostView.as_view(), name='user_update_host'),
    path('user/<int:pk>/delete', views.UserDeleteHostView.as_view(), name='user_delete_host'),


]