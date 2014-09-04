from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views import generic

from Weddings.models import Wedding, Guest
from Weddings.forms import GuestForm

class IndexView(generic.ListView):
    template_name = 'weddings/index.html'
    context_object_name = 'wedding_list'
    def get_queryset(self):
        return Wedding.objects.order_by('-date')

def detail(request, wedding_id):
    w = get_object_or_404(Wedding, pk=wedding_id)
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            new_guest = Guest(wedding=w, name=form.cleaned_data['name'], surname=form.cleaned_data['surname'], email=form.cleaned_data['email'])
            w.guest_set.add(new_guest)
            w.save()
            return HttpResponseRedirect(reverse('weddings:detail', args=(w.id,)))
    else:
        form = GuestForm()
    return render(request, 'weddings/detail.html', {'form': form, 'wedding': w})


def guest(request, wedding_id, guest_id):
    w = get_object_or_404(Wedding, pk=wedding_id)
    g = get_object_or_404(Guest, pk=guest_id)
    return render(request, 'weddings/guest.html', {'wedding': w, 'guest': g})