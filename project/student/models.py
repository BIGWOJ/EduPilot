from django.db import models
from django.utils.text import slugify

class Parent(models.Model):
    father_name = models.CharField(max_length=50)
    father_occupation = models.CharField(max_length=100)
    father_mobile = models.CharField(max_length=25)
    father_email = models.EmailField(max_length=50)
    
    mother_name = models.CharField(max_length=50)
    mother_occupation = models.CharField(max_length=100)
    mother_mobile = models.CharField(max_length=25)
    mother_email = models.EmailField(max_length=50)
    
    present_address = models.TextField()
    permanent_address = models.TextField()
    
    def __str__(self):
        return f"{self.father_name} and {self.mother_name}"
    
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female")])
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=100)
    religion = models.CharField(max_length=50)
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=25)
    admission_number = models.CharField(max_length=25)
    mobile_number = models.CharField(max_length=25)
    section = models.CharField(max_length=25)
    student_image = models.ImageField(upload_to='student/', blank=True)
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}-{self.student_id}")
        super(Student, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"