from django.db import models

# Create your models here.

CHOISE = (
    ("one","ko'rsatilsin"),
    ("two","ko'rsatilmasin")
)

class Category(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
    

class News(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='static/img')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=150,
                    choices=CHOISE,
                    default="one")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class New(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='static/img')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=150,
                    choices=CHOISE,
                    default="one")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class commets(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Data = models.DateField()
    Massages = models.CharField(max_length=200)
    created_at = models.DateField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)





    def __str__(self):
        return self.name

