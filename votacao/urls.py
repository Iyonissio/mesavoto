
from .import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('edit/', views.edit, name='edit'),
    path('update/<str:codigo>', views.update, name='update'),
    path('', views.index, name='home'),
]
