from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from p_library.models import Book, Author, Friend, Publishing_house
from p_library.forms import FriendForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.forms import formset_factory  
from django.http.response import HttpResponseRedirect


def books_list(request):
    template = loader.get_template('book_list.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))

def redaction_list(request):
    template = loader.get_template('redaction_list.html')
    redactions = Publishing_house.objects.all()
    publishers_data = {"data": {publishing_hous.name: 
						list(Book.objects.filter(publishing_house=publishing_hous.id).values_list("title", flat=True))
						 for publishing_hous in redactions}}
    return HttpResponse(template.render(publishers_data, request))

def friend_list(request):
	template = loader.get_template('friend_list.html')
	friends = Friend.objects.all()
	data = {"friends": friends,}
	return HttpResponse(template.render(data, request))	
    
class FriendFormEdit(CreateView):
	model = Friend
	form_class = FriendForm
	success_url = reverse_lazy('p_library:friend_form')
	template_name = 'friend_form_edit.html'

class FriendList(ListView):
	model = Friend
	template_name = 'friend_form.html'

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')



