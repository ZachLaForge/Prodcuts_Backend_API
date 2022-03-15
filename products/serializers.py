from turtle import title
from rest_framework import serializers
from .models import Product




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        title = Product
        fields = ['id','title','description','inventory_quanity']