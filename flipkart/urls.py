from django.urls import path, include

from flipkart.routers import router as frouter

urlpatterns = [
    path('', include(frouter.urls)),
]
