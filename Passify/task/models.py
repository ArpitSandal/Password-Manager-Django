from django.db import models
from django.contrib.auth.models import User
import random,pytz
from django.core.validators import MaxValueValidator, MinValueValidator

myvalidators=[MaxValueValidator(3000),MinValueValidator(1999)]
# Create your models here.

#For storing the authentication code
class Authenticate(models.Model):
    #models.CASCADE means on deletion of this user its data will get deleted too
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userinfo", default=None, null=True)

    #It stores our code which gets sent to the user
    code = models.CharField(max_length=5)

    def __str__(self):
        return self.code

    #overiding the default save method and generating the authentication code
    def save(self, *args, **kwargs):
        codear=[]
        for i in range(5):
            codear.append(random.randint(0,9))

        mycode="".join(str(i) for i in codear)
        mycode=str(mycode)
        self.code=mycode
        super().save(*args, **kwargs)
    
#parent class for different models
class MyUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="loginpass", default=None, null=True)

    name = models.CharField(max_length=120)

    updated = models.DateField(auto_now=True)


#for login details
class LoginPass(MyUser):
    username = models.CharField(max_length=120)

    password = models.BinaryField(null=True)


# for credit card detatils
class CreditPass(MyUser):

    #select choices for the cards and months
    card_choices = (
        ('Rupay', 'Rupay'),
        ('Visa', 'Visa'),
        ('Mastercard', 'Mastercard'),
        ('American Express', 'American Express'),
        ('Maestro', 'Maestro'),
        ('UnionPay', 'UnionPay'),
        ('Other', 'Other')
    )

    month_choices = (
        ('01 - January','01 - January'),
        ('02 - February','02 - February'),
        ('03 - March','03 - March'),
        ('04 - April','04 - April'),
        ('05 - May','05 - May'),
        ('06 - June','06 - June'),
        ('07 - July','07 - July'),
        ('08 - August','08 - August'),
        ('09 - September','09 - September'),
        ('10 - October','10 - October'),
        ('11 - November','11 - November'),
        ('12 - December','12 - December'),
    )

    number = models.BinaryField(null=True)

    brand = models.CharField(max_length=120, null=True, choices=card_choices)

    expirationmonth = models.CharField(max_length=120, null=True, choices=month_choices)

    expirationyear = models.PositiveIntegerField(null=True,validators=myvalidators)

    pin = models.BinaryField(null=True)

    cvv = models.BinaryField(null=True)



#for storing secure notes
class NotesPass(MyUser):
    
    notes = models.BinaryField(null=True)

    #for decrypting the notes
    noteskey = models.BinaryField(null=True)