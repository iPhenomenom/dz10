

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Quote
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import AuthorForm, QuoteForm
from django.contrib.auth.decorators import login_required

def index(request):
    authors = Author.objects.all()
    quotes = Quote.objects.all()

    if request.method == 'POST':
        if 'author_name' in request.POST:
            # Обработка формы добавления нового автора
            form = AuthorForm(request.POST)
            if form.is_valid():
                author = form.save(commit=False)
                author.user = request.user
                author.save()
                return redirect('index')
        elif 'quote_text' in request.POST:
            # Обработка формы добавления новой цитаты
            form = QuoteForm(request.POST)
            if form.is_valid():
                quote = form.save(commit=False)
                quote.user = request.user
                quote.save()
                return redirect('index')
    else:
        form = AuthorForm()

    context = {
        'authors': authors,
        'quotes': quotes,
        'form': form,
    }
    return render(request, 'index.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            # Пользователь не найден или неверный пароль
            error_message = 'Неверное имя пользователя или пароль'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    quotes = Quote.objects.filter(author=author)
    return render(request, 'author_detail.html', {'author': author, 'quotes': quotes})

def quote_detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'quote_detail.html', {'quote': quote})

def logout_view(request):
    logout(request)
    return redirect('index')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправляем пользователя на страницу входа после успешной регистрации
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def home_view(request):
    quotes = Quote.objects.all()
    return render(request, 'index.html', {'quotes': quotes})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quote_list.html', {'quotes': quotes})


@login_required
def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'author_create.html', {'form': form})


@login_required
def quote_create(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.save()
            return redirect('quote_list')
    else:
        form = QuoteForm()

    return render(request, 'quote_create.html', {'form': form})


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect('index')
    else:
        form = AuthorForm()
    return render(request, 'create_author.html', {'form': form})

# Функция для создания новой цитаты
def create_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.save()
            return redirect('index')
    else:
        form = QuoteForm()
    return render(request, 'create_quote.html', {'form': form})

def create_quote_view(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuoteForm()
    return render(request, 'create_quote.html', {'form': form})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.save()
            return redirect('quote_list')
    else:
        form = QuoteForm()
    return render(request, 'add_quote.html', {'form': form})