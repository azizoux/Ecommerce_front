from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import Mug, Cart


class MugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mug
        fields = ('id', 'title', 'description', 'price', 'liked', 'image')


class CartSerializer(WritableNestedModelSerializer):
    mug = MugSerializer(many=False)

    class Meta:
        model = Cart
        fields = ('id', 'mug', 'quantity', 'payed')