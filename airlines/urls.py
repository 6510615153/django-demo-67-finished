from django.urls import path

from . import views

appname = 'airlines'
urlpatterns = [
    path('' ,views.index, name='index'),
    path('<int:flight_id>', views.flight, name='airlines'),
    path('<int:flight_id>/book', views.book, name='book')
]