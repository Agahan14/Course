from django.test import TestCase
from ..models import *


class CourseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='Cooking',imgpath=None)
        contact = Contact.objects.create(type=1,value='+996776172760')
        branch = Branch.objects.create(latitude='123123',longitude='321321',address='Paris')
        course = Course.objects.create(name='Cooking french food',description='Delicious food',category=category,logo=None)
        course.save()
        course.contacts.add(contact)
        course.branches.add(branch)
        cls.course = Course.objects.get(id=1)

    def test_name_label(self):
        field_label = self.course._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_description_label(self):
        field_label = self.course._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_category_label(self):
        field_label = self.course._meta.get_field('category').verbose_name
        self.assertEquals(field_label, 'category')

    def test_logo_label(self):
        field_label = self.course._meta.get_field('logo').verbose_name
        self.assertEquals(field_label, 'logo')

    def test_get_str(self):
        self.assertEquals(self.course.__str__(), self.course.name)



