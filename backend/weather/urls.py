from django.urls import path
from . import views

urlpatterns = [
    path('csrf_token/', views.GetCSRFToken.as_view(), name='csrf_token'),
]
