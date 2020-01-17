from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
def index(request):
    '''
    View function for the home page
    '''
    return render(request,'index.html')

def features(request):
    '''
    View function for the features page
    '''
    return render(request,'features.html')
