from django.urls import path
from .views import *


urlpatterns = [

    path('category/', CategoryAPIView.as_view(), name = 'category'),
    path('category/<int:id>', CategoryDetails.as_view(), name = 'categories'),
    path('branch/', BranchAPIView.as_view(), name = 'branch'),
    path('branch/<int:id>', BranchDetails.as_view(), name = 'branches'),
    path('contact/', ContactAPIView.as_view(), name = 'contact'),
    path('contact/<int:id>', ContactDetails.as_view(), name = 'contacts'),
    path('course/', CourseAPIView.as_view(), name = "course"),
    path('course/<int:id>', CourseDetails.as_view(), name = "courses"),

]