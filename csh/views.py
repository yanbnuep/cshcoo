from django.shortcuts import render
from django.http import JsonResponse
import json
from django.core import serializers
# Create your views here.
from .models import CSH,CSHForm


def add_weekly_page(request):
    stn_choices = CSH._meta.get_field('stn').choices
    shift_choices = CSH._meta.get_field('shift').choices
    week_days = CSH.get_weekly()
    context = {'stn_choices': stn_choices, 'shift_choices': shift_choices, 'week_days': week_days}

    return render(request, 'add.html', context)


def post_weekly_data(request):
    if request.method == 'POST':
        weekly_data = json.loads(request.POST['weekly_data'])
        for data in weekly_data:
            form = CSHForm(data)
            if form.is_valid():
                csh = form.save()
            else:
                print('error')
    return JsonResponse({'data':'done'})


def index_view(request):
    week_days = CSH.get_weekly()
    weekly_data = CSH.objects.all().filter(date__range=[week_days[0], week_days[6]])
    week_dates = list(set(weekly_data))
    context = {'weekly_data': weekly_data, 'weekly_days':week_days}
    return render(request, 'index.html',context)