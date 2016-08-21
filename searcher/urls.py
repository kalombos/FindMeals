from django.conf.urls import include, url

urlpatterns = [
    url(r'api/', include('searcher.api.urls')),
]
