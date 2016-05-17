from django.shortcuts import render
from jonmat.models import CongressMember


def congress_member_list(request):
    members = CongressMember.objects.most_eaten()

    return render(request, 'congress_member/list.html', dict(
        congress_members=members
    ))


def congress_member_list_distill_func():
    return None


def congress_member_detail(request, member_id):
    member = CongressMember.objects.get(id=member_id)

    return render(request, 'congress_member/detail.html', dict(
        congress_member=member
    ))


def congress_member_detail_distill_func():
    for x in CongressMember.objects.all():
        yield str(x.id)
