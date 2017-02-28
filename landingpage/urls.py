from django.conf.urls import url

from . import views

app_name = "landingpage"
urlpatterns = [
    # ex : /upload/
    url(r'$', views.landingpage, name="Bienvenue"),

    # ex : /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"),
]