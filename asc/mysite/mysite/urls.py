from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, re_path
from django.conf.urls import url

admin.autodiscover()

urlpatterns = [
    path('', include('contactus.urls')),
    path('', include('blog.urls'), name='articles'),
    path("admin", admin.site.urls),
    path("", include("cms.urls")),
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    url(r'^tinymce/', include('tinymce.urls')),

]

# urlpatterns += i18n_patterns(path("admin/", admin.site.urls), path("", include("cms.urls")))

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# This is only needed when using runserver.
'''if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)'''
