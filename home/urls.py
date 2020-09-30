from django.urls import path, include
from home import views
from django.urls import path,include
from .views import about

urlpatterns = [
    path('', views.home, name='home'),
    path('our_work', views.our_work, name='our_work'),
    path('about', views.about, name='about'),
    path('the_blackout_block_party', views.the_blackout_block_party, name='the_blackout_block_party'),
    path('quicksip', views.quicksip, name='quicksip'),
    # path('', include('app.urls')),

    #url(r'^video/(?P<vid>\w+)/$', views.display_video)
    # \w will allow alphanumeric characters or string
]
