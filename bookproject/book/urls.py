from django.urls import path


from book.views import index, abc
urlpatterns = [
    path('index/', index, name='index'),
    path('abc/', abc, name='abc'),
]