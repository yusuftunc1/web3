from django.db import models
from ckeditor.fields import RichTextField

# class announcments(models.Model):
#     picturelink = models.CharField(blank=True, null= True, max_length = 50, verbose_name = 'Resim Linki')
#     title = models.CharField(blank=True, null= True, max_length = 50, verbose_name = 'Başlık')
#     text = models.TextField(blank=True,null=True, max_length= 200, verbose_name = 'Mesaj')
#     page_link = models.CharField(blank=True, null = True, verbose_name = "Duyuru Link")

class galeri_page(models.Model):
    display = models.IntegerField(blank=False, null= False, verbose_name='Gösterim Sırası')
    image1 = models.CharField(blank=False, null= False, max_length=100, verbose_name='1. Resim linki')
    image2 = models.CharField(blank=False, null= False, max_length=100, verbose_name='2. Resim linki')
    image3 = models.CharField(blank=False, null= False, max_length=100, verbose_name='3. Resim linki')


class about_page(models.Model):
    confg = models.CharField(blank=False, null= False, max_length=100, verbose_name='Confg')
    image1 = models.CharField(blank=True, null=True, max_length=100, verbose_name='1. Resim linki')
    image2 = models.CharField(blank=True, null=True, max_length=100, verbose_name='2. Resim linki')
    image3 = models.CharField(blank=True, null=True, max_length=100, verbose_name='3. Resim linki')
    image4 = models.CharField(blank=True, null=True, max_length=100, verbose_name='4. Resim linki')
    image5 = models.CharField(blank=True, null=True, max_length=100, verbose_name='5. Resim linki')
    image6 = models.CharField(blank=True, null=True, max_length=100, verbose_name='6. Resim linki')



class announcments(models.Model):
    announcments_url = models.CharField(null=False, max_length=200, verbose_name='Duyuru URL adı')
    title = models.CharField(null= False, max_length = 200, verbose_name = 'Duyuru Başlığı') 
    message = models.CharField(null= False, max_length = 50, verbose_name = 'Kısa mesaj')
    content = RichTextField(blank = False, null= False, verbose_name = 'Duyuru İçeriği')
    image = models.CharField(blank=False, null=False, max_length=100, verbose_name='Resim linki')

class project_page(models.Model):
    project_url = models.CharField(null= False, max_length = 200, verbose_name = 'Proje URL adı')
    title = models.CharField(null= False, max_length = 200, verbose_name = 'Proje Başlığı')
    date = models.CharField(null= False, max_length = 100, verbose_name = 'Proje Tarihi')
    referans = models.CharField(blank= False, null= False, max_length = 100, verbose_name = 'Proje Referansı')
    hedef = models.CharField(blank = False, null= False, max_length = 100, verbose_name = 'Hedef Kitle' )
    butce = models.CharField(blank = False, null= False, max_length = 100, verbose_name = 'Proje Bütçesi')
    partner = RichTextField(blank = False, null= False, verbose_name = 'Proje Partnerleri')
    akis = RichTextField(blank = False, null= False, verbose_name = 'Proje Akışı')
    aciklama = RichTextField(blank = False, null= False,verbose_name = 'Proje Açıklaması')
    image1 = models.CharField(blank=True, null=True, max_length=100, verbose_name='1. resim linki')
    image1text = models.CharField(blank=True, null=True, max_length=100, verbose_name='1. resim info')
    image2 = models.CharField(blank=True, null=True, max_length=100, verbose_name='2. resim linki')
    image2text = models.CharField(blank=True, null=True, max_length=100, verbose_name='2. resim info')
    image3 = models.CharField(blank=True, null=True, max_length=100, verbose_name='3. resim linki')
    image3text = models.CharField(blank=True, null=True, max_length=100, verbose_name='3. resim info')
    image4 = models.CharField(blank=True, null=True, max_length=100, verbose_name='4. resim linki')
    image4text = models.CharField(blank=True, null=True, max_length=100, verbose_name='4. resim info')
    image5 = models.CharField(blank=True, null=True, max_length=100, verbose_name='5. resim linki')
    image5text = models.CharField(blank=True, null=True, max_length=100, verbose_name='5. resim info')
    image6 = models.CharField(blank=True, null=True, max_length=100, verbose_name='6. rsim linki')
    image6text = models.CharField(blank=True, null=True, max_length=100, verbose_name='6. resim info')
    image7 = models.CharField(blank=True, null=True, max_length=100, verbose_name='7. resim linki')
    image7text = models.CharField(blank=True, null=True, max_length=100, verbose_name='7. resim info')
    image8 = models.CharField(blank=True, null=True, max_length=100, verbose_name='8. resim linki')
    image8text = models.CharField(blank=True, null=True, max_length=100, verbose_name='8. resim info')
    image9 = models.CharField(blank=True, null=True, max_length=100, verbose_name='9. resim linki')
    image9text = models.CharField(blank=True, null=True, max_length=100, verbose_name='9. resim info')


# Create your models here.
