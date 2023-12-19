from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.first_view),
    path('create/', views.create_coupon, name='create_coupon'),
    path('created/', views.post_coupon, name='post_coupon')
]