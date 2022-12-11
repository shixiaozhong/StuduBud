from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),  # 将base中的urls导入到根下
]
