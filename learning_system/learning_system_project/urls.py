from django.urls import include, path
from rest_framework import routers
from learning_system_app import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'lessons', views.LessonViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:pk>/grant-access/', views.ProductViewSet.as_view({'post': 'grant_access'})),
    path('products/<int:pk>/check-access/', views.ProductViewSet.as_view({'get': 'check_access'})),
]


