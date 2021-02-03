from rest_framework import serializers

from core.models import Tag


class TagSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'label']


class TagSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['label', ]


class TagSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['label', ]