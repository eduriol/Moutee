from django.shortcuts import render, get_object_or_404
from django.views import generic

from Weddings.models import Wedding, Guest

class IndexView(generic.ListView):
    template_name = 'weddings/index.html'
    context_object_name = 'wedding_list'
    def get_queryset(self):
        return Wedding.objects.order_by('-date')

class DetailView(generic.DetailView):
    model = Wedding
    template_name = 'weddings/detail.html'

def guest(request, wedding_id, guest_id):
    w = get_object_or_404(Wedding, pk=wedding_id)
    g = get_object_or_404(Guest, pk=guest_id)
    return render(request, 'weddings/guest.html', {'wedding': w, 'guest': g})

def add_guest(request, wedding_id):
    w = get_object_or_404(Wedding, pk=wedding_id)
    new_guest = Guest(wedding=w, name=request.POST['name'], surname=request.POST['surname'], email=request.POST['email'])
    w.guest_set.add(new_guest)
    w.save()
    return render(request, 'weddings/detail.html', {'wedding': w})
