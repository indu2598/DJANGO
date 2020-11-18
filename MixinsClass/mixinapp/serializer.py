from rest_framework import serializers
from .models import ItemsList
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= ItemsList
        fields = ('itemname','itemprice')