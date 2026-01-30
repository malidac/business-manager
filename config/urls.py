from django.contrib import admin
from django.urls import path, include
from accounts.views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to Business Manager API!"})

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('expenses.urls')),
]
