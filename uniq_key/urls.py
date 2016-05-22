from django.conf.urls import url
from .views import key_detail, key_list

urlpatterns = [
    url(r'^key/(?P<value>\w{4})$', key_detail, name='task_detail'),
    url(r'^keys/$', key_list, name='task_list'),
]
