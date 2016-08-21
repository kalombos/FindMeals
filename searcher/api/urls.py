# coding:utf8


from django.conf.urls import url
from searcher.api import views


urlpatterns = [
    url('^recipies/search/$',
        views.SearchRecipiesView.as_view(), name='recipies_search'),
]
