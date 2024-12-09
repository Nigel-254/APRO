from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserProfileManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)  # This hashes the password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username



class MissingPersonReport(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    username = models.CharField(max_length=100, unique=True, default='your name')
    phone = models.PositiveBigIntegerField(unique=True, default= '0712345678')
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    height = models.PositiveIntegerField(null=True, blank=True)
    physical_details = models.TextField(null=True, blank=True)
    date_of_disappearance = models.DateField()
    location_of_disappearance = models.CharField(max_length=255)
    contact_details = models.EmailField()
    comments = models.TextField(null=True, blank=True)
    images = models.ImageField(upload_to='missing_persons_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class ContactDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


 # found model
class FoundPerson(models.Model):
    your_name = models.CharField(max_length=100, verbose_name="Your Name")
    phone_number = models.CharField(max_length=15, verbose_name="Your Phone Number")
    email = models.EmailField(verbose_name="Your Email")
    found_person_name = models.CharField(max_length=100, verbose_name="Name of Found Person")
    location = models.CharField(max_length=255, verbose_name="Location")
    date_reported = models.DateTimeField(auto_now_add=True, verbose_name="Date Reported")

    def __str__(self):
        return f"Found: {self.found_person_name} at {self.location}"