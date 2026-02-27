from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'claims', ClaimViewSet)

urlpatterns = [
    path('customers/', CustomerListAPIView.as_view()),
    path('customers/<int:pk>/', CustomerDetailAPIView.as_view()),

    path('policies/', PolicyListAPIView.as_view()),
    path('policies/<int:pk>/', PolicyDetailAPIView.as_view()),

    path('payments/', PremiumPaymentListAPIView.as_view()),
    path('payments/<int:pk>/', PremiumPaymentDetailAPIView.as_view()),

    path('', include(router.urls)),
]
