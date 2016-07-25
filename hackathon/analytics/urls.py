from django.conf.urls import url

from analytics import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

]
