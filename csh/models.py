from django.db import models
from django import forms
import datetime

# Create your models here.
STN_CHOICES = (('TPE', 'TPE'), ('KIX', 'KIX'), ('PVG', 'PVG'), ('PEK', 'PEK'), ('NNG', 'NNG'), ('HAN', 'HAN'))
SHIFTS_CHOICE = (('A', 'A'), ('B', 'B'), ('C', 'C'))


class CSH(models.Model):
    stn = models.CharField(choices=STN_CHOICES, blank=False, max_length=10)
    date = models.DateField(blank=False)
    shift = models.CharField(choices=SHIFTS_CHOICE, blank=False, max_length=10)
    value = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return '%s %s' % (self.stn, self.date)

    @staticmethod
    def get_weekly(date):
        if date is None:
            date = datetime.date.today()
        week = []
        for x in range(0, 7):
            week_day = date - datetime.timedelta(days=date.weekday() - x)
            week.append(week_day)

        return week


class SCOM(models.Model):
    stn = models.CharField(choices=STN_CHOICES, blank=False, max_length=10)
    value = models.CharField(blank=False, default='0', max_length=30)
    start_date = models.DateField(blank=False, max_length=15)
    end_date = models.DateField(blank=False, max_length=15)

    class Meta:
        unique_together = (("stn", "start_date", "end_date"),)


class CSHForm(forms.ModelForm):
    class Meta:
        model = CSH
        fields = ['stn', 'date', 'shift', 'value']


class SCOMForm(forms.ModelForm):
    class Meta:
        model = SCOM
        fields = ['stn', 'value', 'start_date', 'end_date']