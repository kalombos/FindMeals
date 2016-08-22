from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'api/', include('searcher.api.urls', namespace='api')),
    url(r'$', TemplateView.as_view(template_name='search.html')),
]
