
from .import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('edit/', views.edit, name='edit'),
    path('update/<str:codigo>', views.update, name='update'),
    path('', views.index, name='home'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
