from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index_default'),
    url(r'^index/', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^(?P<course_num>[0-9]+)/', views.detail, name='detail'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^addtopic/$', views.addtopic, name='addtopic'),
    url(r'^topics/(?P<topic_id>\d+)/', views.topicdetail, name='topicdetail'),

    #Register, Login and Logout
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register')
]
