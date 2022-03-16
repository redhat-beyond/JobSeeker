from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobseeker.urls')),
    path('profile/', include('personal_profile.urls')),
]
