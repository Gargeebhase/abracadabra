from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^index$',views.index,name='index'),
url(r'^page1$',views.page1,name='page1'),
]