from rest_framework import serializers

from core.models import New


class NewSerializerList(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ['uploader', 'topic', 'tags']


class NewSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ['uploader', 'topic', 'tags']


class NewSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ['uploader', 'topic', 'tags']


class NewSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ['upload', 'topic', 'tags']