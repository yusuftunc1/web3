from django.shortcuts import render
from .models import project_page , announcments, about_page,galeri_page


# Create your views here.


def about(request):
   about_page_context = about_page.objects.all()
   
   context = {
      'about_page': about_page_context,
   }

   return render(request,'pages/about.html', context) 



def galeri(request):
   galeri_page_content = galeri_page.objects.all().order_by('display')

   context = {
      'galeri_page' : galeri_page_content,
   }
   return render(request,'pages/galeri.html',context) 



def index(request):
   duyurular = announcments.objects.all().order_by('-id')[:8]
   context = {
      'announcments' : duyurular,
   }
   return render(request,'pages/index.html',context) 



def call(request):
   return render(request,'pages/call.html') 


def announcment(request):
   duyurular = announcments.objects.all().order_by('-id')[:]
   context = {
      'announcments' : duyurular,
   }
   return render(request,'pages/duyuru.html', context)



def announcment_pages(request, announcments_url):
   duyurular = announcments.objects.filter(announcments_url = announcments_url)
   context = {
      'announcments' : duyurular,
   }
   return render(request,'pages/duyuru_page.html', context) 




def project(request):
   ProjectPage = project_page.objects.all()
   context = {
      'project_page_content': ProjectPage
   }
   return render(request,'pages/project.html', context) 


def project_pages(request, project_url):
   
   ProjectPage = project_page.objects.filter(project_url = project_url)

   context = {
     'project_page_content': ProjectPage
   }

   return render(request,'pages/project_page.html', context) 

    



