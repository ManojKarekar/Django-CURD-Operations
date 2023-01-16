
from django.urls import path 
from app1 import views

urlpatterns = [
  path("",views.add_data,name="addData"),
  path("update/<int:id>/",views.update_data,name="updateData"),
  path("delete/<int:id>/",views.delete_data,name="deleteData"),
]
