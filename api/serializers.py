from django.contrib.auth import get_user_model

from rest_framework import serializers

from api.models import (
    Post,
    Like
)

User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=15, required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=15, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class PostSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True)
    likes_amount = serializers.IntegerField(read_only=True)
    modified_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        return Post.objects.create(creator=self.context.get('request').user,
                                   **validated_data)


class LikeAnalyticsSerializer(serializers.ModelSerializer):
    date = serializers.DateField(read_only=True)
    amount = serializers.IntegerField(read_only=True)

    class Meta:
        model = Like
        fields = ('date', 'amount',)


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'last_activity', 'last_login',)
