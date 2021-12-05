import itertools
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView, View
from django.contrib.auth.models import User
from .models import Contact









def support(request):
    if request.method == "POST":
        obj = Contact()
        obj.name = request.POST['name']
        obj.phone = request.POST['phone']
        obj.subject = request.POST['subject']
        obj.body = request.POST['message']
        obj.save()
        success = 'پیام ارسال شد'
        context = {'success':success}
        return render(request, 'contact/support.html', context)

    context = {}
    return render(request, 'contact/support.html', context)












def about(request):
    context = {}
    return render(request, 'contact/about.html', context)











def contact(request):
    if request.method == "POST":
        obj = Contact()
        obj.name = request.POST['name']
        obj.phone = request.POST['phone']
        obj.subject = request.POST['subject']
        obj.body = request.POST['message']
        obj.save()
        success = 'پیام ارسال شد'
        context = {'success':success}
        return render(request, 'contact/contact.html', context)

    context = {}
    return render(request, 'contact/contact.html', context)














# End
