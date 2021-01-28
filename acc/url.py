from django.conf.urls import url
from . import views

app_name = 'account'
urlpatterns=[
    url(r'^signup/$', views.signup, name='sign_up'),
    url(r'^login/$', views.logi, name='login'),
    url(r'^logout/$', views.logo, name='logout'),
]
