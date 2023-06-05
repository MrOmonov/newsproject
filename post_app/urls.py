from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
urlpatterns = [
    # path('', PostView.as_view(), name='post_url'),
    path('contacts', ContactView.as_view(), name='contact_page'),
    path('local', LocalNewsView.as_view(), name = 'local_news'),
    path('', IndexView.as_view(), name='home_url'),
    path('post/<slug:slug>', PostDetailView.as_view(), name="post_detail_url"),
    path('about', aboutview, name='about_url'),
    path('singlepage', singleview, name="single_url")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
