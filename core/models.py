from django.db import models

# Create your models here.
class Tenant(models.Model):
    name = models.CharField(max_length=255)
    subdomain = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.name
    
    
class Member(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name} - {self.tenant.name}'
