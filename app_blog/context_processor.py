from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.contrib.auth.models import User
from .models import Categories






def blog_cat(request):
    return {
       'blog_cats': models.Categories.objects.all().order_by('-date_created') ,
       'blog_cats_counts': models.Categories.objects.all().count()
    }
