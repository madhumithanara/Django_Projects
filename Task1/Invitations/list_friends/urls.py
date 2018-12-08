from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^input/$',views.inputting,name='inputting'),
    url(r'^input/result$',views.result,name='result'),
    url(r'^$',views.index,name='index'),
]
