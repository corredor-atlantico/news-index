from rest_framework import serializers

from core.models import Message


class MessageSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['sender', 'id', 'parent_new', 'parent_message']


class MessageSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['sender', 'content']


class MessageSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['content']


class MessageSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['content']


class MessageAgreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', ]

    def agree_valoration(self, obj):
        obj.agree = not obj.agree
        obj.save()
