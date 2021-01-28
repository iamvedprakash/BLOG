from django.contrib import admin
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from A import views as av
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'admin/', admin.site.urls),

    url(r'^$', av.list, name="home"),

    url(r'^A/', include('A.url')),

    url(r'^acc/', include('acc.url')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
