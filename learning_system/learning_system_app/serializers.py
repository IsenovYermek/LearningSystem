from rest_framework import serializers
from .models import User, Product, Access, Lesson, Group


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Все поля модели User


class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = '__all__'  # Все поля модели Access


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'  # Все поля модели Lesson


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'  # Все поля модели Group


class ProductSerializer(serializers.ModelSerializer):
    accesses = AccessSerializer(many=True, read_only=True)  # Сериализатор AccessSerializer для связанных моделей Access
    lessons = LessonSerializer(many=True, read_only=True)  # Сериализатор LessonSerializer для связанных моделей Lesson
    groups = GroupSerializer(many=True, read_only=True)  # Сериализатор GroupSerializer для связанных моделей Group

    class Meta:
        model = Product
        fields = '__all__'  # Все поля модели Product
