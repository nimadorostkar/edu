import itertools
from django.shortcuts import render, redirect






def home_page(request):
    context = {}
    return render(request, 'home.html', context)





def support(request):
    if request.method == "POST":
        obj = Contact()
        obj.name = request.POST['name']
        obj.phone = request.POST['phone']
        obj.body = request.POST['message']
        obj.save()
        success = 'پیام ارسال شد'
        context = {'products': products, 'cats':cats, 'latestpost_list':latestpost_list, 'success':success}
        return render(request, 'home/index.html', context)
        
    context = {}
    return render(request, 'support.html', context)

































# End
