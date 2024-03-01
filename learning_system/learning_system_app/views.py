from rest_framework import viewsets
from .models import User, Product, Lesson, Access
from .serializers import UserSerializer, ProductSerializer, LessonSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def grant_access(self, request, *args, **kwargs):
    product = self.get_object()
    students = [1, 2, 3, 4, 5, 6, 7] # Список студентов которым нужно предоставить доступ

    for student_id in students:
        student = User.objects.get(id=student_id)
        Access.objects.create(user=student, product=product)

    return Response({'message': 'Access granted'}, status=status.HTTP_200_OK)
