from django.conf.urls import url
from .views import task_detail, task_list

urlpatterns = [
    url(r'^key/(?P<value>\w{4})$', task_detail, name='task_detail'),
    url(r'^keys/$', task_list, name='task_list'),
]
