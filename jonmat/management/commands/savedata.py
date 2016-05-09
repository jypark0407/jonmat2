import json

from os import path

from django.conf import settings
from django.core.management import BaseCommand
from jonmat.models import CongressMember, Restaurant, Eat


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Delete Existing Data.')

        Eat.objects.all().delete()
        Restaurant.objects.all().delete()
        CongressMember.objects.all().delete()

        print('Load Data.')

        geocodes_file_path = path.join(settings.DATA_DIR, 'geocodes.json')
        data_file_path = path.join(settings.DATA_DIR, 'data.json')

        geocodes = json.load(open(geocodes_file_path))
        data = json.load(open(data_file_path))

        print('Save Objects to Database.')

        for man_name, party, restaurant_name, address, kind, price, memo in data:
            if geocodes[address]:
                lat, lng = geocodes[address]
            else:
                lat, lng = None, None

            member, _ = CongressMember.objects.get_or_create(
                name=man_name,
                party=party,
            )

            restaurant, _ = Restaurant.objects.get_or_create(
                name=restaurant_name,
                address=address,
                lat=lat,
                lng=lng,
            )

            eat = Eat(
                member=member,
                restaurant=restaurant,
                price=price,
            )
            eat.save()
