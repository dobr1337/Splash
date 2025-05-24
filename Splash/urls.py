from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from userauth.views import user_auth
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index),
    path('about', main_views.about),
    path('auth', user_auth),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
