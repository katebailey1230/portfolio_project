
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import contact.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',jobs.views.home, name='home'),
    path('cover/', jobs.views.cover, name='cover'),
    path('info/', contact.views.info, name='info'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
