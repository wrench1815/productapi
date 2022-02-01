from django.urls import path, include

from flipkart.routers import router as frouter
from amazon.routers import router as arouter

urlpatterns = [
    path('flipkart/', include('flipkart.urls')),
    path('amazon/', include('amazon.urls')),
]
