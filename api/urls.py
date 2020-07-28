from api.views.accounts import AccountViewSet

from rest_framework.routers import DefaultRouter
from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token


router = DefaultRouter()
router.register('user', AccountViewSet)

jwturlpatterns = [
    path('auth-jwt/', obtain_jwt_token),
    path('auth-jwt-refresh/', refresh_jwt_token),
    path('auth-jwt-verify/', verify_jwt_token),
]

urlpatterns = router.urls
