from api.views.accounts import AccountViewSet
from api.views.invites import InviteViewSet, InviteRegistrationViewSet

from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views.accounts import account_registration_handler

router = DefaultRouter()
router.register('user', AccountViewSet)
router.register('invite', InviteViewSet)
router.register('invite_reg', InviteRegistrationViewSet)

jwturlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
   path('register_user', account_registration_handler),
] + router.urls  + jwturlpatterns
