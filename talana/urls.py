from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf.urls import include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Talana - Test')


urlpatterns = [
    url(r'^users/', include('users.urls')),
    path('admin/', admin.site.urls),
    
]
