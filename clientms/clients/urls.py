from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    ClientCreateView,
    ClientListView,
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
    VehicleCreateView,
    VehicleDeleteView,
    VehicleUpdateView,
    VehicleListView,
    VehicleDetailView

)


urlpatterns = [
    # client views
    path('client/new/', ClientCreateView.as_view(), name='client_new'),
    path('client/<int:pk>/edit/', ClientUpdateView.as_view(), name='client_edit'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('client', ClientListView.as_view(), name='client_list'),

    # vehicle views
    path('vehicle/new/', VehicleCreateView.as_view(), name='vehicle_new'),
    path('vehicle/<int:pk>/edit/', VehicleUpdateView.as_view(), name='vehicle_edit'),
    path('vehicle/<int:pk>/', VehicleDetailView.as_view(), name='vehicle_detail'),
    path('vehicle/<int:pk>/delete/', VehicleDeleteView.as_view(), name='vehicle_delete'),
    path('vehicle', VehicleListView.as_view(), name='vehicle_list'),

    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    # change password urls
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),



]
