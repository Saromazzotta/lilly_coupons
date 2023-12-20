from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Coupon

def first_view(request):
    return HttpResponse('Hello Lilly!')

def create_coupon(request):
    return render(request, 'create_coupon.html')

def post_coupon(request):
    print("Here is the POST data")
    print(request.POST)
    if request.method == "POST":
        coupon_data = {
            'name': request.POST.get('name'),
            'description': request.POST.get('description'),
            'location': request.POST.get('location'),
            'date': request.POST.get('date'),
        }
        request.session['coupon_data'] = coupon_data # Store the coupon data in session
        #added in DB
        new_coupon = Coupon.objects.create(**coupon_data) # Create a new coupon instance with the POST data
        return redirect('dashboard') # Redirect to the 'dashboard' view
    return render(request, 'dashboard') # If not a POST request, render the dashboard template

def view_coupon(request, coupon_id):
    # print(request.session.items())
    coupon = Coupon.objects.get(id=coupon_id) # Retrieve the Coupon instance with the given coupon_id
    context = {
        "coupon": coupon
    }
    return render(request, 'view_coupon.html', context) # Render the view_character.html template with the context

def edit_coupon(request, coupon_id):
    # print(request.session.items())
    coupon = Coupon.objects.get(id=coupon_id) # Retrieve the Coupon instance with the given coupon_id
    context = {
        "coupon": coupon
    }
    return render(request, 'edit_coupon.html', context) # Render the edit_character.html template with the context

def delete_coupon(request, coupon_id):
    coupon = Coupon.objects.get(id=coupon_id) # Retrieve the Coupon instance with the given coupon_id
    coupon.delete # Delete the retrieved character
    return redirect(request) # Redirect to the dashboard view