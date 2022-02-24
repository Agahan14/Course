from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ..models import *


class CourseTests(APITestCase):
    def setUp(self) -> None:
        category = Category.objects.create(name='Cooking',
                                           imgpath=None)
        contact = Contact.objects.create(type=1,
                                         value='+996776172760')
        branch = Branch.objects.create(latitude='145',
                                       longitude='541',
                                       address='Paris')
        self.course = Course.objects.create(name='Cooking french food',
                                            description='Delicious food',
                                            category=category,
                                            logo=None)
        self.course.save()
        self.course.contacts.add(contact)
        self.course.branches.add(branch)
        self.data = {
            'name': 'Cooking french food',
            'description': 'Delicious food',
            'category': category.id,
            'contacts': contact.id,
            'branches': branch.id,
        }

    def test_course_get(self):
        response = self.client.get(reverse("course"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_detail(self):
        response = self.client.get(reverse("courses", kwargs={'id': self.course.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_create(self):
        response = self.client.post(reverse('course'), self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_course_delete(self):
        response = self.client.delete(reverse('courses', kwargs={'id': self.course.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)