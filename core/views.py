from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# def login1(request):
#   return render(request, 'core/login1.html')
  
@login_required
def home1(request):
  return render(request, 'core/home1.html')
  


def policy(request):
  return render(request, 'core/policy.html')