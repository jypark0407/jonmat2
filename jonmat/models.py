from django.db import models as m


# class Party(object):  # TODO : make a model
#     새누리당 = 'S'
#     더민주당 = 'M'
#     국민의당 = 'K'
#     정의당 = 'J'
#
#     CHOICES = (
#         (새누리당, '새누리당'),
#         (더민주당, '더민주당'),
#         (국민의당, '국민의당'),
#         (정의당, '정의당'),
#     )

class CongressMemberManager(m.Manager):
    def most_spent(self):
        return self.annotate(total_price=m.Sum('eats__price')).order_by('-total_price')

    def most_eaten(self):
        return self.annotate(eat_times=m.Count('eats')).order_by('-eat_times')


class CongressMember(m.Model):
    id = m.AutoField(primary_key=True)
    # party = m.CharField(max_length=1, choices=Party.CHOICES)
    party = m.CharField(max_length=20)
    name = m.CharField(max_length=20)

    objects = CongressMemberManager()

    def __str__(self):
        return '<CongressMember name={name} party={party}>'.format(name=self.name, party=self.party)


class RestaurantManager(m.Manager):
    def most_spent(self):
        return self.annotate(total_price=m.Sum('eats__price')).order_by('-total_price')

    def most_visited(self):
        return self.annotate(eat_times=m.Count('eats')).order_by('-eat_times')


class Restaurant(m.Model):
    id = m.AutoField(primary_key=True)
    name = m.CharField(max_length=80)
    address = m.CharField(max_length=200, null=True)
    lng = m.FloatField(null=True)
    lat = m.FloatField(null=True)

    objects = RestaurantManager()

    def __str__(self):
        return '<Restaurant name={name} address={address}>'.format(name=self.name, address=self.address)


class Eat(m.Model):
    id = m.AutoField(primary_key=True)
    member = m.ForeignKey(CongressMember, related_name='eats')
    restaurant = m.ForeignKey(Restaurant, related_name='eats')
    # date = m.DateTimeField()  # TODO :
    price = m.IntegerField()

    def __str__(self):
        return '<Eat member={member} restaurant={restaurant}>'.format(member=self.member, restaurant=self.restaurant)
