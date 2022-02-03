from django.urls import path, include

from amazon.routers import router as arouter

urlpatterns = [
    path('', include(arouter.urls)),
]
