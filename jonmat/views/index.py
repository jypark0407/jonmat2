from django.shortcuts import render
from jonmat.models import Restaurant, CongressMember


def index(request):
    hot_restaurants = Restaurant.objects.most_visited()[:20]
    hot_congress_members = CongressMember.objects.most_eaten()[:20]

    return render(request, 'index.html', dict(
        hot_restaurants=hot_restaurants,
        hot_congress_members=hot_congress_members,
    ))


def index_distill_func():
    return None
