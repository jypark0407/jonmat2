from django.shortcuts import render
from jonmat.models import Restaurant


def restaurant_list(request):
    restaurants = Restaurant.objects.most_visited()

    return render(request, 'restaurant/list.html', dict(
        restaurants=restaurants
    ))


def restaurant_list_distill_func():
    return None


def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)

    return render(request, 'restaurant/detail.html', dict(
        restaurant=restaurant
    ))


def restaurant_detail_distill_func():
    for x in Restaurant.objects.all():
        yield str(x.id)

