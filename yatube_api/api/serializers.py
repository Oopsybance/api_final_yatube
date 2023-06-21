from rest_framework import serializers
from rest_framework.serializers import CurrentUserDefault

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    '''Сериализатор постов. '''
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Post
        fields = (
            'id', 'text', 'author', 'image', 'group', 'pub_date', 'comments'
        )
        read_only_fields = ('comments',)


class CommentSerializer(serializers.ModelSerializer):
    '''Сериализатор комментариев. '''
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'created', 'post')
        read_only_fields = ('post',)

    def validate(self, data) -> dict:
        if not data['text']:
            raise serializers.ValidationError(
                'Комментарий не может быть пустым'
            )
        return data


class GroupSerializer(serializers.ModelSerializer):
    '''Сериализатор групп. '''
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')


class FollowSerializer(serializers.ModelSerializer):
    '''Сериализатор подписок. '''
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        read_only=False,
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        fields = ('id', 'user', 'following')
        validators = (
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Вы уже подписаны на данного автора!',
            ),
        )

    def validate(self, data) -> dict:
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError(
                'Вы не можете подписаться сам на себя!'
            )
        return data
