from django.urls import path, include
from .routers import router

urlpatterns = [
    path('flipkart/', include(router.urls)),
]
