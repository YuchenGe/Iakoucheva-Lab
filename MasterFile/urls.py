from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^table1/', views.table1, name='table1'),
	url(r'^table2/', views.table2, name='table2'),
	url(r'^table3/', views.table3, name='table3'),
	url(r'^table4/', views.table4, name='table4'),
]