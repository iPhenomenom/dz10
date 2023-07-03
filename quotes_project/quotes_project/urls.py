"""
URL configuration for quotes_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from quotes import views
from quotes.views import add_author, add_quote


from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('authors/', views.author_list, name='author_list'),
    path('quotes/', views.quote_list, name='quote_list'),
    path('quote/new/', views.quote_create, name='quote_create'),
    path('', views.home_view, name='index'),
    path('author/create/', views.create_author, name='create_author'),
    path('create_quote/', views.create_quote_view, name='create_quote'),
    path('add-author/', add_author, name='add_author'),
    path('add-quote/', add_quote, name='add_quote'),
    path('create/author/', views.create_author, name='create_author'),  # Новый путь для создания автора
    path('create/quote/', views.create_quote, name='create_quote'),  # Новый путь для создания цитаты
    path('author/create/', views.author_create, name='author_create'),
    path('quote/create/', views.quote_create, name='quote_create'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('quote/<int:quote_id>/', views.quote_detail, name='quote_detail'),
    # Сброс пароля
    path('reset-password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]





