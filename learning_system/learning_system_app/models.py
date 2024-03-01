from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)


# Модель Product представляет продукт, у которого есть название, дата начала, стоимость и ссылка на создателя (автора/преподавателя)
class Product(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_products')


# Модель Access представляет доступ пользователя к продукту. Она устанавливает связь между пользователем и продуктом.
class Access(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accesses')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='accesses')


# Модель Lesson представляет урок, который принадлежит определенному продукту. Он содержит название урока и ссылку на видео.
class Lesson(models.Model):
    name = models.CharField(max_length=100)
    video_link = models.URLField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='lessons')


# Модель Group представляет группу студентов для конкретного продукта. Она содержит название группы,
# ссылку на продукт и связь со студентами через поле students, указанное как ManyToManyField.
class Group(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='groups')
    students = models.ManyToManyField(User, related_name='groups')
