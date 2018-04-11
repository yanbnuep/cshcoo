from django.shortcuts import render
from django.http import JsonResponse
import json
from django.core import serializers
from django.contrib import messages
# Create your views here.
from .models import CSH,CSHForm, SCOM, SCOMForm


def add_weekly_page(request):
    stn_choices = CSH._meta.get_field('stn').choices
    shift_choices = CSH._meta.get_field('shift').choices
    week_days = CSH.get_weekly()
    context = {'stn_choices': stn_choices, 'shift_choices': shift_choices, 'week_days': week_days}

    return render(request, 'add.html', context)


def post_weekly_data(request):
    if request.method == 'POST':
        if 'weekly_data' in request.POST:
            weekly_data = json.loads(request.POST['weekly_data'])
            for data in weekly_data:
                form = CSHForm(data)
                if form.is_valid():
                    csh = form.save()
        if 'weekly_scom' in request.POST:
            weekly_scom = json.loads(request.POST['weekly_scom'])
            for data in weekly_scom:
                form = SCOMForm(data)
                if form.is_valid():
                    scom = form.save()
                else:

                    return JsonResponse(form.errors.as_json(), safe=False)

    return JsonResponse({'data': 'done'}, safe=False)


def index_view(request):
    week_days = CSH.get_weekly()
    weekly_data = CSH.objects.all().filter(date__range=[week_days[0], week_days[6]])
    weekly_json = serializers.serialize('json', weekly_data)
    weekly_scom = serializers.serialize('json', SCOM.objects.all().filter(start_date=week_days[0]))
    context = {'weekly_data': weekly_json, 'weekly_days': week_days, "weekly_scom": weekly_scom}
    return render(request, 'index.html',context)
