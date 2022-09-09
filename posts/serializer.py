from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """ serialize the data to json"""
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def validate_image(self, value):
        """ if image heigt is to big or wide to big"""

        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Warning image is to big Image must be under 2 mbits'
            )

        if value.image.width > 4100:
            raise serializers.ValidationError(
                'Warning image is to wide Image must be under 4100 pixels'
            )
        if value.image.height > 4100:
            raise serializers.ValidationError(
                'Warning image is to high Image must be under 4100 pixels'
            )
        return value

    class Meta:
        model = Post
        fields = '__all__'
