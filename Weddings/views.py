from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from Weddings.models import Wedding

def index(request):
    latest_wedding_list = Wedding.objects.all().order_by('-date')[:5]
    context = {'latest_wedding_list': latest_wedding_list}
    return render(request, 'weddings/index.html', context)

def detail(request, wedding_id):
    wedding = get_object_or_404(Wedding, pk=wedding_id)
    return render(request, 'weddings/detail.html', {'wedding': wedding})

def add_guest(request, wedding_id):
    wedding = get_object_or_404(Wedding, pk=wedding_id)
    return render(request, 'weddings/detail.html', {'wedding': wedding})