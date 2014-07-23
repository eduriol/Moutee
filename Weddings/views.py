from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from Weddings.models import Wedding, Guest

def index(request):
    latest_wedding_list = Wedding.objects.all().order_by('-date')[:5]
    context = {'latest_wedding_list': latest_wedding_list}
    return render(request, 'weddings/index.html', context)

def detail(request, wedding_id):
    w = get_object_or_404(Wedding, pk=wedding_id)
    return render(request, 'weddings/detail.html', {'wedding': w})

def add_guest(request, wedding_id):
    w = get_object_or_404(Wedding, pk=wedding_id)
    new_guest = Guest(wedding=w, name=request.POST['name'], surname=request.POST['surname'], email=request.POST['email'])
    w.guest_set.add(new_guest)
    w.save()
    return render(request, 'weddings/detail.html', {'wedding': w})