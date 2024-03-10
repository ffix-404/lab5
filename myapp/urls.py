from django.urls import path
from . import views
app_name="myapp"
urlpatterns=[
    path("",views.home,name="index1"),
    path("add",views.page1,name="add")
]
    