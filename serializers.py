from socnet.models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class PostSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        post = Post.objects.create(user=validated_data['user'], title=validated_data['title'], description=validated_data['description'])
        return post

    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'description')