# -*- coding: utf-8 -*-
from rest_framework import generics

from searcher import models
from searcher.api import serializers


class SearchRecipiesView(generics.ListAPIView):

    serializer_class = serializers.RecipieSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name:
            return models.Recipie.objects\
                .prefetch_related('variations__ingredient')\
                .filter(name__icontains=name)
        else:
            return models.Recipie.objects.none()