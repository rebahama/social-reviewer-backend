from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Likes


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Likes
        fields = '__all__'

    def create(self, validated_data):
        """ The user can't like a post twice
            if the user likes a post twice
            then raise the error."""
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
