from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comments


class CommentSerializer(serializers.ModelSerializer):
    """ set the serializers so that we can acesss these values
        through the api endpoint"""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """ request the user"""
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """ Make the time more readable to human eyes"""
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """ Make the time more readable to human eyes """
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comments
        fields = '__all__'


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is set so that we dont need to set all the post.id for
    each detail comments.
    """
    post = serializers.ReadOnlyField(source='post.id')
