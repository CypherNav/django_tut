from django.urls import path
from hloworld import views
urlpatterns=[
    path("\hlo",views.index),
    path('',views.index)
]