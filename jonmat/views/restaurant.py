from django.db.models import Sum, Count
from django.shortcuts import render
from jonmat.models import Restaurant


def restaurant_list(request):
    # order by 방문횟수
    restaurants = Restaurant.objects.annotate(eat_times=Count('eats')).order_by('-eat_times')

    # order by total price
    # restaurants = Restaurant.objects.annotate(total_price=Sum('eats__price')).order_by('-total_price')

    return render(request, 'restaurant/list.html', dict(
        restaurants=restaurants
    ))


def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)

    return render(request, 'restaurant/detail.html', dict(
        restaurant=restaurant
    ))
