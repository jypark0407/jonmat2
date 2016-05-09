from django.shortcuts import render
from jonmat.models import Restaurant, CongressMember


def index(request):
    hot_restaurants = Restaurant.objects.all()[:20]
    hot_congress_members = CongressMember.objects.all()[:20]

    return render(request, 'index.html', dict(
        hot_restaurants=hot_restaurants,
        hot_congress_members=hot_congress_members,
    ))
