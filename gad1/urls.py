from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^index$',views.index,name='index'),
url(r'^page1$',views.page1,name='page1'),
url(r'^page2$',views.page2,name='page2'),
url(r'^page3$',views.page3,name='page3'),
url(r'^page4$',views.page4,name='page4'),
#url(r'^page23$',views.page23,name='page23'),
#url(r'^page24$',views.page24,name='page24'),
url(r'^page5$',views.page5,name='page5'),
url(r'^page6$',views.page6,name='page6'),

url(r'^page7$',views.page7,name='page7'),
url(r'^page8$',views.page8,name='page8'),
url(r'^updatefile$',views.updatefile,name='updatefile'),
url(r'^updatefile2$',views.updatefile2,name='updatefile2'),
url(r'^page18$',views.page18,name='page18'),
url(r'^page9$',views.page9,name='page9'),
url(r'^page19$',views.page19,name='page19'),
url(r'^pagechat$',views.pagechat,name='pagechat'),

#url(r'^accounts/login$',views.login1,name='login'),
#url(r'^page18$',views.page18,name='page18'),

]