
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name="index"),
    path('about',views.about, name="about"),
    path('gallery',views.gallery, name="gallery"),
    path('history',views.history, name="history"),
    path('front-person',views.front_person, name="front_person"),
    path('contact',views.contact, name="contact"),
    path('writer',views.writer, name="writer"),
    path('geneology',views.gene, name="gene"),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
