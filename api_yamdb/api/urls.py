from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    send_code, get_token, AdminViewSet,
    UserInfo, CategoryViewSet, GenreViewSet, TitleViewSet
)

router = DefaultRouter()
router.register('users', AdminViewSet)
router.register('genres', GenreViewSet)
router.register('categories', CategoryViewSet)
router.register('titles', TitleViewSet)

urlpatterns = [
    path('v1/auth/signup/', send_code, name='get_email_code'),
    path('v1/auth/token/', get_token, name='get_token'),
    path('v1/users/me/', UserInfo.as_view(), name='user_info'),
    path('v1/', include(router.urls))
]
