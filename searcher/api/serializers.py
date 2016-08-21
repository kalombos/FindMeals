from searcher import models
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient


class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Variation

    measure = serializers.SerializerMethodField()
    ingredient = serializers.SerializerMethodField()

    def get_ingredient(self, obj):
        return obj.ingredient.name

    def get_measure(self, obj):
        return obj.get_measure_display()


class RecipieSerializer(serializers.ModelSerializer):
    variations = VariationSerializer(many=True)

    class Meta:
        model = models.Recipie
