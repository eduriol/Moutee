from django.forms import ModelForm
from Weddings.models import Guest
from django.utils.translation import ugettext_lazy

class GuestForm(ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'surname', 'email']
        labels = {
            'name': ugettext_lazy(''),
            'surname': ugettext_lazy(''),
            'email': ugettext_lazy(''),
        }