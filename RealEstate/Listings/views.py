from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from .models import Listings
from django.core.paginator import Paginator
from .choice import price_choices, bedroom_choices, state_choices
# Create your views here.


def Index(request):
    listings = Listings.objects.order_by(
        '-lsit_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def Listing(request, listing_id):
    listing = get_object_or_404(Listings, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/list.html', context)


def Search(request):

    queryset_list = Listings.objects.order_by('-lsit_date')

    # keyword
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)


    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
    
    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)



    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings':queryset_list,
        'value':request.GET
    }
    return render(request, 'listings/search.html',context)
