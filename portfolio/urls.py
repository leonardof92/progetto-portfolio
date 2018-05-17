from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.content_list, name='content_list'),
    url(r'^content/(?P<pk>[0-9]+)/$',views.content_detail, name="content_detail"),
    url(r'^skill/(?P<pk>[0-9]+)/$',views.skill_detail, name="skill_detail"),
    url(r'^content/new/$', views.content_new, name='content_new'),
    url(r'^skill/new/$', views.skill_new, name='skill_new'),
    url(r'^content/(?P<pk>[0-9]+)/edit/$',views.content_edit, name='content_edit'),
    url(r'^skill/(?P<pk>[0-9]+)/edit/$',views.skill_edit, name='skill_edit'),
    url(r'^bozze/$', views.content_lista_bozze, name='content_lista_bozze' ),
    url(r'^bozzeSkill/$', views.skill_lista_bozze, name='skill_lista_bozze' ),
    url(r'^content/(?P<pk>[0-9]+)/publish/$', views.content_publish, name='content_publish'),
    url(r'^skill/(?P<pk>[0-9]+)/publish/$', views.skill_publish, name='skill_publish'),    
    url(r'^content/(?P<pk>\d+)/remove/$', views.content_remove, name='content_remove'),
    url(r'^skill/(?P<pk>\d+)/remove/$', views.skill_remove, name='skill_remove'),    
]

