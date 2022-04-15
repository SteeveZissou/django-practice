from django.contrib import admin
from django.urls import path

from store.views import books, book

urlpatterns = [
    path('', books, name="url-index"),
    path('<int:book_pk>/', book, name="url-book"),
    path('admin/', admin.site.urls),
]
