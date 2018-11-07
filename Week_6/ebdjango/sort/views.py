# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def index(request):
	return render(request, 'index.html')

def sort_rating(request):
	showall = request.GET.get('all',False)
	BookList = Book.objects.order_by('-rating')[:(int(showall)+1)*10]
	if (int(showall)+1) == 2:
		BookList = Book.objects.order_by('-rating')[(int(showall)-1)*10:]
	return render(request, 'home.html', {'BookList': BookList})

def sort_ratingsCount(request):
	showall = request.GET.get('all',False)
	BookList = Book.objects.order_by('-ratingsCount')[:(int(showall)+1)*10]
	if (int(showall)+1) == 2:
		BookList = Book.objects.order_by('-ratingsCount')[(int(showall)-1)*10:]
	return render(request, 'home.html', {'BookList': BookList})

def sort_publishYear(request):
	showall = request.GET.get('all',False)
	BookList = Book.objects.order_by('-publish_year')[:(int(showall)+1)*10]
	if (int(showall)+1) == 2:
		BookList = Book.objects.order_by('-publish_year')[(int(showall)-1)*10:]
	return render(request, 'home.html', {'BookList': BookList})