from django.urls import path, re_path
from . import views
# from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    # Данное РВ сопоставляет любой URL-адрес, который начинается с book/,
    # за которым до конца строки (до маркера конца строки - $) следуют одна, или более цифр.
    # В процессе выполнения данного преобразования, оно "захватывает" цифры и передаёт их в функцию отображения
    # как параметр с именем pk.
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]

urlpatterns += [
    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]