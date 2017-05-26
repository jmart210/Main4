from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^blogs$',views.blogs),
    # url(r'^userorm$',views.userorm),
    url(r'^comments/(?P<id>\d+)$',views.comments),

]
