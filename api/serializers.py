from rest_framework import serializers
from api.models import Post


class PostSerializer(serializers.ModelSerializer):
    likes_amount = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)  # convert to client time

    class Meta:
        model = Post
        fields = '__all__'
