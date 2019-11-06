from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser

class CustomUserM(AbstractUser):
    '''Overrides the custom django user model'''
    # Datafields
    SUPER_ADMIN = 1
    ADMIN = 2
    ROLE_CHOICES = (
      (ADMIN,'admin'),
      (SUPER_ADMIN,'super_admin')
    )
    user_role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=ADMIN)

class Organization(models.Model):
    Name_of_Organization = models.CharField(max_length=50)
    Address = models.TextField()

    def __str__(self):
        return self.Name_of_Organization

    class Meta:
        verbose_name_plural = "Manage Organizations"

# Create your models here.
class Visaletters(models.Model):
    Organization_Details = models.ForeignKey(Organization,on_delete=models.PROTECT,related_name="Organization_Name",)
    MULTIPLICITY = (
        ("single", "single"),
        ("double", "double"),
    )
    PAS = (("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"))
    TOUR = (
        ("TOURISM","TOURISM"),
        ("AIM TOURISM","AIM TOURISM")
    )
    GENDER = (
        ("M","M"),
        ("F","F"),
    )
    def number():
        no = Visaletters.objects.count()
        if no == None:
            return 1
        else:
            return (int(str( ( 220 - 64 ) + no + 1 )+"2019"))
    multiplicity = models.CharField(choices=MULTIPLICITY, default="SINGLE",max_length=100)
    no_passengers = models.IntegerField(default=1)
    Country = CountryField(blank_label='(select country)')
    Tourism= models.CharField(choices=TOUR, default="TOURISM",max_length= 100 )
    entry_from = models.CharField(max_length=200)
    departure_to = models.CharField(max_length=200)
    Visa_Letter_Number = models.CharField(default=number,max_length=200)
    Visa_Letter_N = models.CharField(default = str(number),editable=False,max_length=200)
    Date_of_letter = models.CharField(max_length=200, blank=True)
    Routes_and_Places = models.CharField(max_length=500, default="moscow")
    hotels = models.CharField(max_length=264)
    multi = (("Paid", "Paid"), ("unpaid", "unpaid"))
    Payment_status = models.CharField(max_length=200, choices=multi, default="unpaid")
    amount = models.PositiveIntegerField()
    firstname_1 = models.CharField(max_length=264)
    lastname_1 = models.CharField(max_length=264)
    Passport_Number_1 = models.CharField(max_length=200, unique=True)
    Date_Of_Birth_1 = models.CharField(max_length=200)
    Sex_1 = models.CharField(choices=GENDER,max_length=100)
    firstname_2 = models.CharField(max_length=264, blank=True)
    lastname_2 = models.CharField(max_length=264, blank=True)
    Passport_Number_2 = models.CharField(max_length=200, blank=True)
    Date_Of_Birth_2 = models.CharField(max_length=200, blank=True)
    Sex_2 = models.CharField(max_length=100,choices=GENDER, blank=True)
    firstname_3 = models.CharField(max_length=264, blank=True)
    lastname_3 = models.CharField(max_length=264, blank=True)
    Passport_Number_3 = models.CharField(max_length=200, blank=True)
    Date_Of_Birth_3 = models.CharField(max_length=200, blank=True)
    Sex_3 = models.CharField(max_length=100,choices=GENDER, blank=True)
    firstname_4 = models.CharField(max_length=264, blank=True)
    lastname_4 = models.CharField(max_length=264, blank=True)
    Passport_Number_4 = models.CharField(max_length=200, blank=True)
    Date_Of_Birth_4 = models.CharField(max_length=200, blank=True)
    Sex_4 = models.CharField(max_length=100,choices=GENDER, blank=True)
    firstname_5 = models.CharField(max_length=264, blank=True)
    lastname_5 = models.CharField(max_length=264, blank=True)
    Passport_Number_5 = models.CharField(max_length=200, blank=True)
    Date_Of_Birth_5 = models.CharField(max_length=200, blank=True)
    Sex_5 = models.CharField(max_length=100,choices=GENDER, blank=True)

    def __str__(self):
        return self.firstname_1

    class Meta:
        verbose_name_plural = "Fill Form to Generate Visa Letter and Voucher"

