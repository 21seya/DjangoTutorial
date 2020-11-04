from django.urls import path
from .views import NewsP,Home,Contact,NewsDate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',Home,name='home'),
    path('news/',NewsP,name='news'),
    path('newsdate/<int:year>',NewsDate,name='newsdate'),
    path('contact/',Contact,name='contact'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
##urlpatterns += staticfiles_urlpatterns()
