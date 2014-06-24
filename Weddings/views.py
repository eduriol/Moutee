from django.http import HttpResponse
from django.shortcuts import render

from Weddings.models import Wedding

def index(request):
    latest_wedding_list = Wedding.objects.all().order_by('-date')[:5]
    context = {'latest_wedding_list': latest_wedding_list}
    return render(request, 'weddings/index.html', context)

def detail(request, wedding_id):
    return HttpResponse("You're looking at wedding %s." % wedding_id)