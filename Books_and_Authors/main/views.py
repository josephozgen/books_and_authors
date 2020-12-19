from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
  context = {
    "books": Book.objects.all()
  }
  return render(request, "index.html", context) 

def add_book(request):
  form = request.POST

  Book.objects.create(
    title=form['title'],
    description=form['description']
  )

  return redirect('/')

def authors(request):
  context = {
    'authors': Author.objects.all()
  }
  return render(request, "authors.html", context)

def add_author(request):
  form = request.POST

  Author.objects.create(
    first_name = form['first_name'],
    last_name = form['last_name'],
    notes = form['notes']
  )

  return redirect('/authors')

def single_book(request, book_id):
  context = {
    "book": Book.objects.get(id=book_id),
    "authors": Author.objects.all()
  }

  return render(request, "book-details.html", context)

def add_author_to_book(request, book_id):
  form = request.POST
  # print("*"*20)
  # print(form)
  # print("*"*20)
  
  this_book = Book.objects.get(id=book_id)
  try:
    author = Author.objects.get(id=form["author_id"])
  except:
    print("*"*20)
    print("Error is here!")
    print("*"*20)
  
  this_book.authors.add(author)

  return redirect(f"/books/{book_id}")
  #return redirect("/books/" + str(book_id))

def author_details(request, author_id):
  context = {
    "author": Author.objects.get(id = author_id),
    "books": Book.objects.all()
  }

  return render(request, "author-details.html", context)

def add_book_to_author(request, author_id):
  form = request.POST

  this_author = Author.objects.get(id=author_id)
  book = Book.objects.get(id=form["book_id"])

  this_author.books.add(book)
  #print(type(this_author.books))

  return redirect(f'/authors/{author_id}')