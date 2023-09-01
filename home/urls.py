from django.contrib import admin
from django.urls import path, include
from home import views




admin.site.site_header="Login to Ahmar's Dashboard"
admin.site.site_title="Welcome to Ahmar's Dashboard"
admin.site.index_header="Welcome to this portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home' ,  views.home, name='home'),
    path('about' ,  views.about, name='about'),
    path('projects' ,  views.projects, name='project'),
    path('contact' ,  views.contact, name='contact'),
]
