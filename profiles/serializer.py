from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """ serialize the data to json"""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_like = serializers.ReadOnlyField()
    review_counter = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """ How to check for profile ownership"""
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = '__all__'

