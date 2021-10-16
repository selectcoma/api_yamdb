from django.db.models import base
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    send_code, get_token, AdminViewSet, CommentViewSet,
    CategoryViewSet, GenreViewSet,
    ReviewViewSet, UserInfo, TitleViewSet
)

router = DefaultRouter()
router.register('users', AdminViewSet)

router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)

router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'

)
router.register('genres', GenreViewSet, basename='genres')
router.register('categories', CategoryViewSet, basename='categories')
router.register('titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('v1/auth/signup/', send_code, name='get_email_code'),
    path('v1/auth/token/', get_token, name='get_token'),
    path('v1/users/me/', UserInfo.as_view(), name='user_info'),
    path('v1/', include(router.urls))
]
