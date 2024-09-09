from django.db import models

# Create your models here.
"""

"""

class BookInfo(models.Model):
    name = models.CharField(max_length=100,unique=True)
    pub_data = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'
        verbose_name = 'ShuJi Guanli'
    def __str__(self):
        return self.name

class PeopleInfo(models.Model):


    GENDER_CHOICES = (
        ('1','male' ),(2,'female'),
    )
    name = models.CharField(max_length=100,unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES,default=1)
    description = models.CharField(max_length=500,null=True)
    is_delete = models.BooleanField(default=False)

    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'peopleinfo'

    def __str__(self):
        return self.name
