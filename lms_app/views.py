from django.shortcuts import render , redirect
from .models import BooK , Category
from .form import BookForm, CategoryForm

# Create your views here.
################index##########################
def index(request):

    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()

        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()

    cotext = {
        'category' : Category.objects.all(),
        'books' : BooK.objects.all(),
        'form' : BookForm(),
        'formcat': CategoryForm(),
        'allbooks': BooK.objects.filter(active = True).count(),
        'booksold': BooK.objects.filter(status= 'sold').count(),
        'bookrental': BooK.objects.filter(status= 'rental').count(),
        'bookavailble': BooK.objects.filter(status='availble').count(),
    }
    return render(request, 'pages/index.html', cotext)


########################books############################

def books(request):
    search = BooK.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains= title)



    if request.method == 'POST':
        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()
    cotext = {
        'category': Category.objects.all(),
        'books': search,
        'formcat': CategoryForm(),
    }
    return render(request, 'pages/books.html', cotext)
#########################delete#################################

def delete(request, id):
    if request.method == 'POST':
        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()

    book_delete =  BooK.objects.get(id = id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')

    cotext = {
        'category': Category.objects.all(),
        'books': BooK.objects.all(),
        'formcat': CategoryForm(),
    }
    return render(request, 'pages/delete.html', cotext)


#############################update############################

def update(request, id):

    if request.method == 'POST':
        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()

    book_id = BooK.objects.get(id = id)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')

    else:
        book_save = BookForm(instance=book_id)

    cotext = {
        'category': Category.objects.all(),
        'books': BooK.objects.all(),
        'formcat': CategoryForm(),
        'form': book_save,
    }
    return render(request, 'pages/update.html', cotext)
