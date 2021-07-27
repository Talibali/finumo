from rest_framework import serializers

from project.apps.user import models as user_models
from project.apps.common import models as common_models
from project.apps.user.messages import Messages
# from project.core.helpers.signed_url import S3GenerateSignedUrl


class EmailAuthSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    passcode = serializers.CharField(required=False)

    class Meta:
        model = user_models.Profile
        fields = ('email', 'password', 'passcode')

    def validate(self, attrs):

        obj = user_models.Profile.objects.get(email=attrs.get('email'))
        if obj:
            raise serializers.ValidationError('This email id already exists')
        else:
            return attrs

    def create(self, validated_data):
        return user_models.Profile.objects.create(**validated_data)