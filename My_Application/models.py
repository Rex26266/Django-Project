from django.db import models

# Create your models here.


class Member(models.Model):
    MEMBERSHIP_TYPE = (('RE', 'Religious'), ('SE', 'Secular Clergy'), ('LP', 'Lay Person'))

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(verbose_name='DOB')
    age = models.IntegerField()
    membership_type = models.CharField(max_length=2, choices=MEMBERSHIP_TYPE)

    def __str__(self):
        return self.first_name
