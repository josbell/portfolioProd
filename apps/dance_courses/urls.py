from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index ,name='index'),
    url(r'^showUserCourses$', views.showUserCourses ,name='showUserCourses'),
    url(r'^createusers/$', views.createUsers ,name='createUsers'),
    url(r'^loginUsers/$', views.loginUsers ,name='loginUsers'),
    url(r'^logoutUsers/$', views.logoutUsers ,name='logoutUsers'),
    url(r'^showClass/(?P<classId>\d+)$',views.showClass, name='showClass'),
    url(r'^subscribe/(?P<courseId>\d+)$',views.subscribe, name='subscribe'),
    url(r'^unsubscribe/(?P<courseId>\d+)$',views.unsubscribe, name='unsubscribe'),
    url(r'^showNav$', views.showNav ,name='showNav'),
    url(r'^createComments/$',views.createComments, name='createComments'),
    url(r'^deleteComments/(?P<commentId>\d+)$',views.deleteComments, name='deleteComments')
 #   url(r'^new/$', views.newNote, name='new'),
 #   url(r'^destroy/(?P<id>\d+)$', views.destroy, name='destroy'),
 #   url(r'^showNotesOnly/$', views.showNotesOnly, name='showNotesOnly')
]