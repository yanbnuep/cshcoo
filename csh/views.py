from django.shortcuts import render
from django.http import JsonResponse
import json
from django.core import serializers
from datetime import datetime, date
# Create your views here.
from .models import CSH, CSHForm, SCOM, SCOMForm


def add_weekly_page(request):
    stn_choices = CSH._meta.get_field('stn').choices
    shift_choices = CSH._meta.get_field('shift').choices
    week_days = CSH.get_weekly(datetime.today())
    context = {'stn_choices': stn_choices, 'shift_choices': shift_choices, 'week_days': week_days}

    return render(request, 'add.html', context)


def add_specify_week(request, year, month, day):
    request_date = datetime.strptime(year+'-'+month+'-'+day, '%Y-%m-%d').date()
    stn_choices = CSH._meta.get_field('stn').choices
    shift_choices = CSH._meta.get_field('shift').choices
    week_days = CSH.get_weekly(request_date)
    context = {'stn_choices': stn_choices, 'shift_choices': shift_choices, 'week_days': week_days}

    return render(request, 'add.html', context)


def post_weekly_data(request):
    if request.method == 'POST':
        if 'weekly_data' in request.POST:
            weekly_data = json.loads(request.POST['weekly_data'])
            for index, data in enumerate(weekly_data):
                print(data)
                form = CSHForm(data)
                if form.is_valid():
                    form.save()
                else:
                    return JsonResponse({'row': index, 'error_weekly_data': form.errors.as_json()}, safe=False)

        if 'weekly_scom' in request.POST:
            weekly_scom = json.loads(request.POST['weekly_scom'])
            for index, data in enumerate(weekly_scom):
                form = SCOMForm(data)
                if form.is_valid():
                    form.save()
                else:
                    return JsonResponse({'row': index, 'error_scom': form.errors.as_json()}, safe=False)

    return JsonResponse({'data': 'done'}, safe=False)


def index_view(request):
    week_days = CSH.get_weekly(datetime.today())
    weekly_data = CSH.objects.all().filter(date__range=[week_days[0], week_days[6]])
    weekly_scom = serializers.serialize('json', SCOM.objects.only('stn', 'value').filter(start_date=week_days[0]))
    context = {"weekly_scom": weekly_scom, 'weekly_data': weekly_data, 'weekly_days': week_days}
    return render(request, 'index.html', context)


def specify_weekly(request, year, month, day):
    request_date = datetime.strptime(year + '-' + month + '-' + day, '%Y-%m-%d').date()
    week_days = CSH.get_weekly(request_date)
    weekly_data = CSH.objects.all().filter(date__range=[week_days[0], week_days[6]])
    weekly_scom = serializers.serialize('json', SCOM.objects.only('stn', 'value').filter(start_date=week_days[0]))
    context = {"weekly_scom": weekly_scom, 'weekly_data': weekly_data, 'weekly_days': week_days}
    return render(request, 'index.html', context)
