from django.shortcuts import render,redirect,HttpResponse
from django.db import models

class Subscriber(models.Model):
    subscriber = models.EmailField(primary_key=True)

    def __str__(self):
        return self.subscriber

    def addsubscricer(request):
        su = Subscriber(request.POST['semail'])
        su.save()
        return redirect('index')