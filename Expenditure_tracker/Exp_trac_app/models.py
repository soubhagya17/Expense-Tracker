from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
import calendar
import datetime


fetched_user=get_user_model()
#for Todays date
now = datetime.datetime.now()
#The number of days in current month
no_of_days=calendar.monthrange(now.year, now.month)[1]


# User created models.

class Profile(models.Model):
    #One on One syncronisation with user model
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #To check if the user is loging in first time
    first_login=models.BooleanField(default=True)


@receiver(post_save,sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ For syncronisation of profile model to user model """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender, instance, **kwargs):
    """ For syncronisation of profile model to user model """
    instance.profile.save()

@receiver(user_logged_in)
def post_login(sender, user, request, **kwargs):
    """ For initializing the whole months expenses in first login """
    if user.profile.first_login==True:
        for i in range(no_of_days):
            ob=Expenditure(
            mem_user=user,date=datetime.date(now.year,now.month,i+1),
            food=0,mandatory=0,essentials=0,travel=0,shopping=0,booze=0,entertainment=0,
            people=0,others=0,mobile=0,per_day_total=0)
            ob.save()
        user.profile.first_login=False
        user.profile.save()


class Expenditure(models.Model):
    #Every Expense is linked with a User
    mem_user=models.ForeignKey(fetched_user,related_name='Expense',on_delete=models.DO_NOTHING)
    date= models.DateField()
    food=models.IntegerField()
    mandatory=models.IntegerField()
    essentials=models.IntegerField()
    travel=models.IntegerField()
    shopping=models.IntegerField()
    booze=models.IntegerField()
    entertainment=models.IntegerField()
    people=models.IntegerField()
    others=models.IntegerField()
    mobile=models.IntegerField()
    per_day_total=models.IntegerField()
    comments=models.CharField(max_length=255)

    def __str__(self):
        return str(self.date.strftime('%Y/%m/%d'))
