from django.urls import path
from . import views


#http://127.0.0.1:8000

urlpatterns=[
  
  path('cagrilar', views.call, name='call'),


  path('', views.index, name='index'),
  path('galeri', views.galeri, name='galeri'),
  path('about', views.about, name='hakkimizda'),
  path('duyuru/<str:announcments_url>', views.announcment_pages, name='duyuru'),
  path('duyurular', views.announcment, name='duyurular'),
  path('proje/<str:project_url>', views.project_pages, name='proje'),
  path('projeler', views.project, name='projeler'),
 
  
]

# urlpatterns=[
#   path('', views.index, name='index'),
#   path('about', views.about, name='about'),
# ]