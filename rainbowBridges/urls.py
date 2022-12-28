"""asset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.documentation import include_docs_urls

api_urlpatterns = [
    path('', include(('apps.datacenter.urls.api', 'datacenter'), namespace='datacenter')),
    path('', include(('apps.equipment.urls.api', 'equipment'), namespace='equipment')),
    path('', include(('apps.cabinet.urls.api', 'cabinet'), namespace='cabinet')),
    path('', include(('apps.network.urls.api', 'cabinet'), namespace='network')),
    path('', include(('apps.warehouse.urls.api', 'warehouse'), namespace='warehouse')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((api_urlpatterns, 'api'), namespace='api')),
    path('asset/api/', include((api_urlpatterns, 'asset_api'), namespace='asset-api')),
    path('docs/', include_docs_urls(title='文档')),
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
