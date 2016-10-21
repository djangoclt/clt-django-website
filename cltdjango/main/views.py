from django.shortcuts import render

from main.models import ActiveMember


def index(request):
    return render(request, 'index.html', {'index': 'index'})


def about(request):
    return render(request, 'main/about.html', {'title': 'About'})


def active_members(request):
    active_members = ActiveMember.objects.all()
    context = {
        'title': "Active Members",
        'active_members':active_members,
    }
    return render(request, 'main/active_members.html', context)
