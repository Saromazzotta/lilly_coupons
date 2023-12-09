from django.shortcuts import render
from django.http import HttpResponse

def first_view(request):
    return HttpResponse('Hello Lilly!')

def create_character(request):
    return render(request, 'create_coupon.html')
