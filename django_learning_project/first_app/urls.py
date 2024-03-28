from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name="index"),     #huseyinsanal.com/first_app
    path("<int:num1>/",views.course_number_view,name="coursenumberview"),
    path("<str:item>/",views.course,name="course"),     ##huseyinsanal.com/first_app/python
    path("<int:num1>/<int:num2>/",views.multiply_view,name="multiply"),     ##huseyinsanal.com/first_app/5/4
    
]