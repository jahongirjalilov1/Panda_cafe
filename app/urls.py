from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from app.views import Indexpage, contact_view

urlpatterns = [
    path('', Indexpage.as_view(), name='index'),
    path('contact/', contact_view, name='contact')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
