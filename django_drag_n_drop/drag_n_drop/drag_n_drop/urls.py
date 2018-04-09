from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('drag/', include('drag.urls')),
    path('admin/', admin.site.urls),
]