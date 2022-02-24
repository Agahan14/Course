from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    branches = BranchSerializer(many=True)
    class Meta:
        model = Course
        fields = '__all__'

