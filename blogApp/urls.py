from django.urls import path
from . import views

app_name = "blogApp"

urlpatterns = [
    path('',views.index,name="index"),
    path("detail/<int:post_id>/",views.datail,name="detail"),
    path("contact/",views.contact,name="contact"),
]
