from django.db import models
from django.utils import timezone
from datetime import datetime
from django.utils.text import slugify

class Service(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    full_description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    
    # Pricing fields
    base_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pricing_description = models.TextField(help_text="Describe pricing structure and options")
    
    # Features and benefits
    features = models.JSONField(default=list, help_text="List of features as JSON array")
    benefits = models.JSONField(default=list, help_text="List of benefits as JSON array")
    
    # Technical details
    technical_requirements = models.TextField(blank=True)
    implementation_time = models.CharField(max_length=100, blank=True)
    
    # Additional information
    faq = models.JSONField(default=list, help_text="FAQ as JSON array of questions and answers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured', 'name']

    def __str__(self) -> str:
        return str(self.name)

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        if isinstance(self.created_at, datetime):
            date_str = self.created_at.strftime('%Y-%m-%d')
        else:
            date_str = 'Unknown date'
        return f"Message from {self.name} - {date_str}"

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    testimonial = models.TextField()
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured', '-created_at']

    def __str__(self) -> str:
        return f"Testimonial from {self.client_name}"

class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='news/')
    excerpt = models.TextField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(default=timezone.now)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']
        verbose_name = 'News Post'
        verbose_name_plural = 'News Posts'

    def __str__(self) -> str:
        return str(self.title)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    author = models.CharField(max_length=100, default='AI Assistant')
    category = models.CharField(max_length=50, default='Technology')
    tags = models.CharField(max_length=200, blank=True)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
