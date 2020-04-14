from django.conf.urls import url
from App1 import views
app_name = 'App1'
urlpatterns=[
    url('registration/',views.registration,name = 'registration'),
    url('user_login/',views.user_login,name='user_login'),
    url('contactpage/',views.contactpage,name = 'contactpage'),
    ]
