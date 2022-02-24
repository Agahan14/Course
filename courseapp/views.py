from django.shortcuts import render
from .serializers import *
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


class CategoryAPIView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetails(APIView):

    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        categories =self.get_object(id)
        serializer = CategorySerializer(categories)
        return Response(serializer.data)

    def put(self, request, id):
        categories = self.get_object(id)
        serializer = CategorySerializer(categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requset, id):
        categories = self.get_object(id)
        categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BranchAPIView(APIView):

    def get(self, request):
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BranchSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BranchDetails(APIView):

    def get_object(self, id):
        try:
            return Branch.objects.get(id=id)
        except Branch.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        branches =self.get_object(id)
        serializer = BranchSerializer(branches)
        return Response(serializer.data)

    def put(self, request, id):
        branches = self.get_object(id)
        serializer = BranchSerializer(branches, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requset, id):
        branches = self.get_object(id)
        branches.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContactAPIView(APIView):

    def get(self, request):
        branches = Contact.objects.all()
        serializer = ContactSerializer(branches, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactDetails(APIView):

    def get_object(self, id):
        try:
            return Contact.objects.get(id=id)
        except Contact.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        branches =self.get_object(id)
        serializer = ContactSerializer(branches)
        return Response(serializer.data)

    def put(self, request, id):
        contacts = self.get_object(id)
        serializer = ContactSerializer(contacts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requset, id):
        branches = self.get_object(id)
        branches.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseAPIView(APIView):

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetails(APIView):

    def get_object(self, id):
        try:
            return Course.objects.get(id=id)
        except Course.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        courses =self.get_object(id)
        serializer = CourseSerializer(courses)
        return Response(serializer.data)

    def delete(self, requset, id):
        branches = self.get_object(id)
        branches.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

