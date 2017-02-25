from django.conf.urls import url

from . import views

app_name = "DSOWeb"
urlpatterns = [
    # ex : /upload/
    url(r'^upload/$', views.upload_file, name="upload"),

    url(r'^calibexist/$', views.calibexist, name="calibexist"),

    url(r'^caliberror/$', views.caliberror, name="caliberror"),
    url(r'^calibcreated/$', views.calibcreated, name="calibcreated"),

    # ex : /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"),
]