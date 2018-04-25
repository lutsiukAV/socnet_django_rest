from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from serializers import *
from rest_framework import generics, status
from rest_framework.response import *


# Create your views here.

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserHandler(APIView):

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format='json'):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class PostHandler(APIView):
    def post(self, request, format='json'):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            return Response(post, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format='json'):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class LikesHandler(APIView):

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user_id = Token.objects.filter(key=request.data['token'])[0].user_id
        liked = post.likes.filter(author=user_id)
        if len(liked) > 0:
            liked.likes.remove(user_id)
            return Response(data=liked, status=status.HTTP_202_ACCEPTED)
        elif len(liked) == 0:
            post.likes.add(user_id)
            return Response(data=liked, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


