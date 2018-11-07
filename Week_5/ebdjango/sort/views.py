# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def index(request):
	return render(request, 'index.html')

def sort_rating(request):
    BookList = Book.objects.all().order_by('-rating')
    return render(request, 'home.html', {'BookList': BookList})