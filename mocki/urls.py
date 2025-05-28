from django.urls import path
from . import views

app_name = 'mocki'

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('pos-systems/', views.pos_systems, name='pos_systems'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('hospital-management/', views.hospital_management, name='hospital_management'),
    path('school-management/', views.school_management, name='school_management'),
    path('erp-solutions/', views.erp_solutions, name='erp_solutions'),
    path('web-design/', views.web_design, name='web_design'),
    path('hardware-sourcing/', views.hardware_sourcing, name='hardware_sourcing'),
    path('hardware-installation/', views.hardware_installation, name='hardware_installation'),
    path('technical-support/', views.technical_support, name='technical_support'),
    path('it-support/', views.it_support, name='it_support'),
    path('maintenance-services/', views.maintenance_services, name='maintenance_services'),
    path('cctv-security/', views.cctv_security, name='cctv_security'),
    path('blog/', views.blog, name='blog'),
    path('cybersecurity/', views.cybersecurity, name='cybersecurity'),
    path('data-management/', views.data_management, name='data_management'),
] 