from django.test import TestCase

from django.core.urlresolvers import reverse

class WeddingIndexViewTests(TestCase):

    def test_index_view_with_no_weddings(self):
        """
        If no weddings exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('weddings:index'))
        self.assertContains(response, "No weddings are available.", status_code=200)
        self.assertQuerysetEqual(response.context['wedding_list'], [])