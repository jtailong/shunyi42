from tabnanny import verbose

from django.db import models

# Create your models here.
class BookInfo(models.Model):
    # create field
    name = models.CharField(max_length=100,verbose_name = 'MingCheng')
    pub_date = models.DateField(verbose_name =  'faburiqi',null=True)
    readcount = models.IntegerField(default=0,verbose_name='yueduliang')
    commentcount = models.IntegerField(default=0,verbose_name='pinglunliang')
    is_delete = models.BooleanField(default=False,verbose_name='luojishanchu')

    class Meta:
        db_table = 'bookinfo' #dabase rename
        verbose_name = 'TuShu' # show in admin station

    def __str__(self):
        # define each data class show information
        return self.name

class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female'),
    )
    name = models.CharField(max_length=100,verbose_name = 'Renming')
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0,verbose_name='xingbie')
    description = models.CharField(max_length=200,null=True,verbose_name='Miaoshu')
    book = models.ForeignKey('BookInfo',on_delete=models.CASCADE,verbose_name="tushu")
    is_delete = models.BooleanField(default=False,verbose_name='luojishanchu')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = 'Renwuxinxi'


    def __str__(self):
        return self.name
