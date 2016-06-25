from django.conf.urls import url
from . import views
app_name = "usercenter"
urlpatterns = [
    url(r'^signup/$', views.signUp, name='signup'),
    url(r'^myinterests/$', views.interstList, name='myinterests'),
    url(r'^addinterest/(\w+)/$', views.addinterst, name='addinterest'),
    url(r'^removeinterest/(\w+)/$', views.removeinterst, name='removeinterst'),

]
