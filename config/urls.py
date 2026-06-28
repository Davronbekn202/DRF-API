from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ListApiView.as_view(), name="list"),
    path('create/', views.ListCreateView.as_view(), name="create"),
    path('detail/<int:pk>/', views.ListDetailView.as_view(), name="detail"),
    path('delete/<int:pk>/', views.ListDeleteView.as_view(), name="delete"),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    path('api/v1/auth/register/', include('dj_rest_auth.registration.urls')),

]
