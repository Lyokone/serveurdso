from django.conf.urls import url

from . import views

app_name = "3DReconstruct"
urlpatterns = [
    # ex : /upload/
    url(r'^upload/$', views.upload_file, name="upload"),

    url(r'^result/$', views.result, name="result"),

    url(r'^calibexist/$', views.calibexist, name="calibexist"),

    url(r'^caliberror/$', views.caliberror, name="caliberror"),
    url(r'^calibcreated/$', views.calibcreated, name="calibcreated"),

    url(r'^model3dcreated/$', views.model3dcreated, name="model3dcreated"),
    url(r'^calibdontexist/$', views.calibdontexist, name="calibdontexist"),

    # ex : /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"),
]