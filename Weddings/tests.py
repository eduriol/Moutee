from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.timezone import utc

import datetime

from Weddings.models import Wedding, Guest
from Weddings.forms import GuestForm

def create_user(username='john_doe', password='john_doe'):
    return User.objects.create_user(username=username, password=password)

def create_wedding(date, user1, user2):
    return Wedding.objects.create(date=date, user1=user1, user2=user2)

def create_guest(wedding, name='John', surname='Doe', email='john_doe@foo.foo'):
    return Guest.objects.create(wedding=wedding, name=name, surname=surname, email=email)

class WeddingIndexViewTests(TestCase):

    def setUp(self):
        self.u1 = User.objects.create_user(username='john_doe', password='john_doe')
        self.u2 = User.objects.create_user(username='jane_doe', password='jane_doe')

    def test_index_view_with_no_weddings(self):
        """
        If no weddings exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('weddings:index'))
        self.assertContains(response, "No weddings are available.", status_code=200)
        self.assertEqual(len(response.context['wedding_list']), 0)

    def test_index_view_with_one_wedding(self):
        """
        If one wedding exists, it should be displayed.
        """
        w = create_wedding(datetime.datetime.utcnow().replace(tzinfo=utc), self.u1, self.u2)
        response = self.client.get(reverse('weddings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['wedding_list']), 1)

    def test_index_view_with_more_than_one_wedding(self):
        """
        If two wedding exist, they should be displayed.
        """
        w1 = create_wedding(datetime.datetime.utcnow().replace(tzinfo=utc), self.u1, self.u2)
        w2 = create_wedding(datetime.datetime.utcnow().replace(tzinfo=utc), self.u1, self.u2)
        response = self.client.get(reverse('weddings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['wedding_list']), 2)

    def tearDown(self):
        self.u1.delete()
        self.u2.delete()

class WeddingDetailViewTests(TestCase):

    def setUp(self):
        self.u1 = User.objects.create_user(username='john_doe', password='john_doe')
        self.u2 = User.objects.create_user(username='jane_doe', password='jane_doe')

    def test_detail_view_of_a_non_existing_wedding(self):
        """
        The detail view of a wedding that does not exist should return a 404 not found.
        """
        response = self.client.get(reverse('weddings:detail', args=(1,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_of_an_existing_wedding_with_no_guests_and_no_post(self):
        """
        The detail view of this existing wedding should display correctly and show no guests.
        """
        w = create_wedding(datetime.datetime.utcnow().replace(tzinfo=utc), self.u1, self.u2)
        response = self.client.get(reverse('weddings:detail', args=(w.id,)))
        self.assertContains(response, "There are no guests in this wedding yet.", status_code=200)

    def test_detail_view_of_an_existing_wedding_with_one_guest_and_no_post(self):
        """
        The detail view of this existing wedding should display correctly and show one guest.
        """
        w = create_wedding(datetime.datetime.utcnow().replace(tzinfo=utc), self.u1, self.u2)
        g = create_guest(wedding=w, name='John', surname='Doe', email='john_doe@foo.foo')
        response = self.client.get(reverse('weddings:detail', args=(w.id,)))
        self.assertContains(response, "John Doe", status_code=200)

    def test_detail_view_of_an_existing_wedding_with_two_guests_and_no_post(self):
        """
        The detail view of this existing wedding should display correctly and show two guests.
        """
        w = create_wedding(datetime.datetime.utcnow().replace(tzinfo=utc), self.u1, self.u2)
        g1 = create_guest(wedding=w, name='John', surname='Doe', email='john_doe@foo.foo')
        g2 = create_guest(wedding=w, name='Jane', surname='Doe', email='jane_doe@foo.foo')
        response = self.client.get(reverse('weddings:detail', args=(w.id,)))
        self.assertContains(response, "John Doe", status_code=200)
        self.assertContains(response, "Jane Doe", status_code=200)

    # def test_detail_view_of_an_existing_wedding_with_no_guests_and_post_valid_guest(self):
    #
    # def test_detail_view_of_an_existing_wedding_with_one_guest_and_post_valid_guest(self):
    #
    # def test_detail_view_of_an_existing_wedding_with_two_guests_and_post_valid_guest(self):
    #
    # def test_detail_view_of_an_existing_wedding_with_no_guests_and_post_invalid_guest(self):
    #
    # def test_detail_view_of_an_existing_wedding_with_one_guest_and_post_invalid_guest(self):
    #
    # def test_detail_view_of_an_existing_wedding_with_two_guests_and_post_invalid_guest(self):

    def tearDown(self):
        self.u1.delete()
        self.u2.delete()

class GuestFormTests(TestCase):

    def test_valid_form_with_email(self):
        form_data = {'name': 'John', 'surname': 'Doe', 'email': 'john_doe@foo.foo'}
        form = GuestForm(data = form_data)
        self.assertTrue(form.is_valid())

    def test_valid_form_without_email(self):
        form_data = {'name': 'John', 'surname': 'Doe'}
        form = GuestForm(data = form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_empty_name(self):
        form_data = {'surname': 'Doe', 'email': 'john_doe@foo.foo'}
        form = GuestForm(data = form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['name'], [u"This field is required."])

    def test_invalid_form_empty_surname(self):
        form_data = {'name': 'John', 'email': 'john_doe@foo.foo'}
        form = GuestForm(data = form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['surname'], [u"This field is required."])

    def test_invalid_form_invalid_email(self):
        form_data = {'name': 'John', 'surname': 'Doe', 'email': 'john_doefoofoo@'}
        form = GuestForm(data = form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['email'], [u"Enter a valid email address."])

class GuestDetailViewTests(TestCase):

    def setUp(self):
        self.u1 = User.objects.create_user(username='john_doe', password='john_doe')
        self.u2 = User.objects.create_user(username='jane_doe', password='jane_doe')
        self.w = create_wedding(datetime.datetime.utcnow().replace(tzinfo=utc), self.u1, self.u2)

    def test_detail_view_of_a_non_existing_guest(self):
        """
        The detail view of a guest that does not exist should return a 404 not found.
        """
        response = self.client.get(reverse('weddings:guest', args=(self.w.id, 1,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_of_an_existing_guest(self):
        """
        The detail view of an existing guest should display correctly.
        """
        g = create_guest(wedding=self.w, name='John', surname='Doe', email='john_doe@foo.foo')
        response = self.client.get(reverse('weddings:guest', args=(self.w.id, g.id,)))
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.u1.delete()
        self.u2.delete()
        self.w.delete()