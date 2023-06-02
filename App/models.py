from django.db import models

# Create your models here.
class Profile(models.Model):

    RELIGION = (
        ('Islam', 'Islam'),
        ('Hinduism', 'Hinduism'),
        ('Buddhism', 'Buddhism'),
        ('Judaism', 'Judaism'),
        ('Christianity', 'Christianity')
    )

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )

    name =      models.CharField    (max_length=30, null=True, blank=True)
    image =     models.ImageField   (upload_to='profile_pic/', default='default/no_img.jpg', null=True, blank=True)
    email =     models.EmailField   (max_length=30, null=True, blank=True)
    age =       models.CharField    (max_length=2, null=True, blank=True)
    address =   models.TextField    (max_length=300, null=True, blank=True)
    phone =     models.TextField    (max_length=15, null=True, blank=True)
    dob =       models.TextField    (max_length=15, null=True, blank=True)
    religion =  models.CharField    (max_length=20, choices=RELIGION)
    gender =    models.CharField    (max_length=10, choices=GENDER)

    def __str__(self):
        return str(self.name)

