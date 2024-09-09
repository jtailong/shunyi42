from multiprocessing.managers import public_methods

from django.http import HttpResponse
from django.shortcuts import render

from book.apps import BookConfig
# Create your views here.
from book.models import BookInfo
def index(request):
    books = BookInfo.objects.all()
    print(books)


    return HttpResponse('index')

################### add data
from book.models import BookInfo
book = BookInfo(
    name = 'Django',
    pub_data= '2010-7-4',
    readcount= 10
)
book.save()
## add data
## objects
BookInfo.objects.create(
    name = 'ceshikaifa',
    pub_data = '2033-7-7',
)

book = BookInfo.objects.get(id = 8)
book.name = 'yunweikaifa'
book.save()


BookInfo.objects.filter(id=8).update(name='pachongrumen',commentcount = 6)

book = BookInfo.objects.get(id=8)
book.delete()

BookInfo.objects.filter(id=5).delete()

book = BookInfo.objects.get(id=1)

book = BookInfo.objects.get(id=1)
book = BookInfo.objects.get(id__exact=1)
book = BookInfo.objects.get(pk=1)

BookInfo.objects.filter(name__contains = 'She')
BookInfo.objects.filter(name__endswith = 'She')

BookInfo.objects.filter(id__in=[1,3,5])
BookInfo.objects.filter(id__gt=3)
from django.db.models import F
BookInfo.objects.filter(readcount__gte=F('commentcount'))

BookInfo.objects.filter(readcount__gte=30).filter(id__lt=3)
BookInfo.objects.filter(readcount__gte=30,id__lt=3)

from django.db.models import Q
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=2))

from django.db.models import Sum,Max,Min,Avg,Count

BookInfo.objects.aggregate(Sum('readcount'))
BookInfo.objects.all().order_by('readcount')

book = BookInfo.objects.get(id=1)
book.peopleinfo_set.all()


from book.models import PeopleInfo
person = PeopleInfo.objects.get(id=1)
person.book.pub_data

BookInfo.objects.filter(peopleinfo__name__exact='guojing')
BookInfo.objects.filter(peopleinfo__name='guojing')
BookInfo.objects.filter(peopleinfo__description__contains='ba')

PeopleInfo.objects.filter(book__name__exact='TianLong')
PeopleInfo.objects.filter(book__readcount__gt=30)