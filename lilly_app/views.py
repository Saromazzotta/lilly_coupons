from django.shortcuts import render, redirect
from django.http import HttpResponse

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
        return redirect('dashboard') # Redirect to the 'dashboard' view
    return render(request, 'dashboard')