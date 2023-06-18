from django.contrib import admin
from django.urls import path, include
from coolcite import settings
from django.conf.urls.static import static
from sport.views import page_not_fount,handle_error_403,handle_error_400,handle_error_500

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('sport.urls'))
]

if settings.DEBUG:
    import mimetypes

    mimetypes.add_type("application/javascript", ".js", True)
    # urlpatterns=[
    #     path('__debug__/', include('debug_toolbar.urls'))

    # ] + urlpatterns
    
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler404=page_not_fount
handler500=handle_error_500
handler403=handle_error_403
handler400=handle_error_400