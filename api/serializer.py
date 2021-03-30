from django.conf import settings
from rest_framework import serializers

from api.models import Student


class StuSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    birthday = serializers.DateField()

    gender = serializers.SerializerMethodField()
    def get_gender(self, obj):
        return obj.get_gender_display()

    pic = serializers.SerializerMethodField()
    def get_pic(self, obj):
        return "%s%s%s" % ("http://127.0.0.1:8000/", settings.MEDIA_URL, str(obj.pic))

    phone = serializers.CharField()


class StuDeSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=20,
        min_length=5,
        error_messages={
            'max_length': '用户名长度过长了',
            'min_length': '用户名长度太短了',
        }
    )
    password = serializers.CharField()
    name = serializers.CharField()
    birthday = serializers.DateField()

    def create(self, validated_data):
        stu_obj = Student.objects.create(**validated_data)
        return stu_obj