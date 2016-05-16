from django.db.models import Sum, Count
from django.shortcuts import render
from jonmat.models import Restaurant


def restaurant_list(request):
    restaurants = Restaurant.objects.most_visited()

    return render(request, 'restaurant/list.html', dict(
        restaurants=restaurants
    ))


def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)

    return render(request, 'restaurant/detail.html', dict(
        restaurant=restaurant
    ))
