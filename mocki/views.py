from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Service, NewsPost, Testimonial # Import the Service model
from django.http import Http404

# Create your views here.

def home(request):
    services = Service.objects.all() # Fetch all Service objects
    news_posts = NewsPost.objects.filter(is_featured=True)[:3] # Fetch featured news posts
    testimonials = Testimonial.objects.filter(is_featured=True)[:5] # Fetch featured testimonials
    context = {
        'services': services,
        'news_posts': news_posts,
        'testimonials': testimonials,
    }
    return render(request, 'mocki/home.html', context)

def about(request):
    return render(request, 'mocki/about.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'mocki/services.html', {'services': services})

def contact(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        message = request.POST.get('message')
        
        # Here you would typically:
        # 1. Validate the data
        # 2. Save to database
        # 3. Send email notification
        # 4. etc.
        
        # For now, we'll just show a success message
        messages.success(request, 'Thank you for your message! We will get back to you soon.')
        return redirect('mocki:contact')
    
    return render(request, 'mocki/contact.html')

def service_detail(request, service_id):
    service = Service.objects.get(id=service_id)
    related_services = Service.objects.exclude(id=service_id)[:3]
    return render(request, 'mocki/service_detail.html', {
        'service': service,
        'related_services': related_services
    })

def pos_systems(request):
    return render(request, 'mocki/possystems.html')

def hospital_management(request):
    return render(request, 'mocki/hospital_management.html')

def school_management(request):
    return render(request, 'mocki/school_management.html')

def erp_solutions(request):
    return render(request, 'mocki/erp_solutions.html')

def web_design(request):
    return render(request, 'mocki/web_design.html')

def hardware_sourcing(request):
    return render(request, 'mocki/hardware_sourcing.html')

def hardware_installation(request):
    return render(request, 'mocki/hardware_installation.html')

def technical_support(request):
    return render(request, 'mocki/technical_support.html')

def it_support(request):
    return render(request, 'mocki/it_support.html')

def maintenance_services(request):
    return render(request, 'mocki/maintenance_services.html')

def cctv_security(request):
    return render(request, 'mocki/cctv_security.html')

def blog(request):
    return render(request, 'mocki/blog.html')

def cybersecurity(request):
    return render(request, 'mocki/cybersecurity.html')

def data_management(request):
    return render(request, 'mocki/data-management.html')
