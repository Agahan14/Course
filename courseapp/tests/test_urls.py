from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import *

class TestUrls(SimpleTestCase):

    def test_category_url_is_resolved(self):
        url = reverse('category')
        self.assertEquals(resolve(url).func.view_class, CategoryAPIView)

    def test_categories_url_is_resolved(self):
        url = reverse('categories')
        self.assertEquals(resolve(url).func.view_class, CategoryDetails)

    def test_branch_url_is_resolved(self):
        url = reverse('branch')
        self.assertEquals(resolve(url).func.view_class, BranchAPIView)

    def test_branches_url_is_resolved(self):
        url = reverse('branches')
        self.assertEquals(resolve(url).func.view_class, BranchDetails)

    def test_contact_url_is_resolved(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func.view_class, ContactAPIView)

    def test_contacts_url_is_resolved(self):
        url = reverse('contacts')
        self.assertEquals(resolve(url).func.view_class, ContactDetails)

    def test_course_url_is_resolved(self):
        url = reverse('course')
        self.assertEquals(resolve(url).func.view_class, CourseAPIView)

    def test_courses_url_is_resolved(self):
        url = reverse('courses')
        self.assertEquals(resolve(url).func.view_class, CourseDetails)