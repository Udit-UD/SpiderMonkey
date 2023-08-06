from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),   # This is your index view
    path('home/', include('home.urls')),  # This might be for other views in your home app
    path('search/', include('home.urls')),  # This is for the search view
]
