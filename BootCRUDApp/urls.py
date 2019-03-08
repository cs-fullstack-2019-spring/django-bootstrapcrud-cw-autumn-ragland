from django.urls import path
from . import views

urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # edit form
    path('editItem/<int:ID>', views.editItem, name='editItem'),
]
