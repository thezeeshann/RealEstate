from django.shortcuts import render
from Listings.models import Listings
from Realtors.models import Realtor
from Listings.choice import price_choices,bedroom_choices,state_choices
# Create your views here.

def IndexPage(request):
    listings = Listings.objects.order_by('-lsit_date').filter(is_published=True)[:3]
    context = {
        'listings':listings,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices
    }
    return render(request,'index.html',context)


def AboutPage(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors':realtors,
        'mvp_realtors':mvp_realtors
    }
    return render(request,'about.html',context)