from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.first_view),
    path('create/', views.create_coupon, name='create_coupon'),
    path('created/', views.post_coupon, name='post_coupon'),
    path('view/<int:coupon_id>/', views.view_coupon, name='view_coupon'),
    path('edit/<int:coupon_id>/', views.edit_coupon, name='edit_coupon'),
    path('update/<int:coupon_id/', views.update_coupon, name='update_coupon'),
    path('delete/<int:coupon_id>/', views.delete_coupon, name='delete_coupon')


]