from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from questionbank import views

urlpatterns = [
	url(r'^question/$', views.QuestionList.as_view()),
    url(r'^question/(?P<id>[0-9]+)/$', views.QuestionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)