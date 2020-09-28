from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('our_work', views.our_work, name='our_work'),
    path('about', views.about, name='about'),
    #url(r'^video/(?P<vid>\w+)/$', views.display_video)
    # \w will allow alphanumeric characters or string
]
