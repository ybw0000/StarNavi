from django.urls import path
from .views import UserList, UserCreate, UserDetail, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/', UserCreate.as_view(), name='registration'),
    path('users/', UserList.as_view(), name='list_of_all_users'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user_detail_view'),
    path('token/', MyTokenObtainPairView.as_view(), name='login_for_taking_JWT_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
]
