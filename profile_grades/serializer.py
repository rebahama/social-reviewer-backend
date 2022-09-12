from django.db import IntegrityError
from rest_framework import serializers
from profile_grades.models import ProfileLikes


class ProfileLikeSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ProfileLikes
        fields = '__all__'

    def create(self, validated_data):
        """ User can't like a profile twice"""
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
