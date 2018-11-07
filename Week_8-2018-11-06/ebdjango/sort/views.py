# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django import forms
from django.forms import widgets
from django.forms import fields

def test(request):
    return render(request, 'test.html')

def index(request):
    Biography = Book.objects.filter(genre_type='biography')
    Fiction = Book.objects.filter(genre_type='fiction')
    Classics = Book.objects.filter(genre_type='classics')
    BookList = {'biography': Biography, 'fiction': Fiction, 'classics': Classics}
    return render(request, 'index.html', {'BookList': BookList})

def sort_rating(request,genre):
    showall = request.GET.get('all',False)
    BookList = Book.objects.filter(genre_type=genre).order_by('-rating')[:(int(showall)+1)*10]
    if (int(showall)+1) == 2:
        BookList = Book.objects.filter(genre_type=genre).order_by('-rating')[(int(showall)-1)*10:]
    return render(request, 'home.html', {'BookList': BookList})

def sort_ratingsCount(request,genre):
    showall = request.GET.get('all',False)
    BookList = Book.objects.filter(genre_type=genre).order_by('-ratingsCount')[:(int(showall)+1)*10]
    if (int(showall)+1) == 2:
        BookList = Book.objects.filter(genre_type=genre).order_by('-ratingsCount')[(int(showall)-1)*10:]
    return render(request, 'home.html', {'BookList': BookList})

def sort_publishYear(request,genre):
    showall = request.GET.get('all',False)
    BookList = Book.objects.filter(genre_type=genre).order_by('-publish_year')[:(int(showall)+1)*10]
    if (int(showall)+1) == 2:
        BookList = Book.objects.filter(genre_type=genre).order_by('-publish_year')[(int(showall)-1)*10:]
    return render(request, 'home.html', {'BookList': BookList})