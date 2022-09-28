from rest_framework import serializers

from blogapi.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'author', 'created', 'author_mail', 'author_image', 'read_time']
