from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django_countries.fields import CountryField

import uuid

# Create your models here.

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def get_contact(self):
        return Contact.objects.get(resume = self)
    
    def get_experience(self):
        return Experience.objects.filter(resume = self)
    
    def get_education(self):
        return Education.objects.filter(resume = self)
    
    def get_certifications(self):
        return Certifications.objects.filter(resume = self)
    
    def get_skills(self):
        return Skills.objects.filter(resume = self)

    def get_summary(self):
        return Summary.objects.get(resume = self)
    
    def __str__(self):
        return f'{self.user} resume'

class Contact(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    current_job_title = models.CharField(max_length=255, blank=True, null=True)
    phone = PhoneField()
    country = CountryField()
    city = models.CharField(max_length=255)
    state_province = models.CharField(max_length=255)
    zip_postal_code = models.CharField(max_length=255)
    email = models.EmailField()
    
    def __str__(self):
        return f'contact info for {self.resume}'

class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    company_organization = models.CharField(max_length=255)
    country = CountryField()
    city = models.CharField(max_length=255)
    state_province = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    current_job = models.BooleanField(default=False)
    
    def get_responsibilities(self):
        return Responsibilities.objects.filter(job = self)
    
    def __str__(self):
        return f'{self.job_title} experience info for {self.resume}'

class Responsibilities(models.Model):
    job = models.ForeignKey(Experience, on_delete=models.CASCADE)
    body = models.TextField()
    
    def __str__(self):
        return f'job point info for {self.job}'

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    country = CountryField()
    city = models.CharField(max_length=255)
    state_province = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return f'education info for {self.resume}'

class Certifications(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    
    def __str__(self):
        return f'certification info for {self.resume}'

class Skills(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    
    def __str__(self):
        return f'skills info for {self.resume}'

class Summary(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    body = models.TextField()
    
    def __str__(self):
        return f'executive summary for {self.resume}'
    


    
    




    