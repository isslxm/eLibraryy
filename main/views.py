from django.shortcuts import render, get_object_or_404, redirect
from .models import Card,Tag, Video
from django.http import HttpResponse
from .forms import BookSearchForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from .forms import VideoSearchForm

def render_main_page(request):
    return render(request, 'main/MainPage.html')

def render_contact_page(request):
    return render(request, 'main/videos.html')

def render_about_page(request):
    return render(request, 'main/about.html')

def render_book_page(request):
    form = BookSearchForm(request.GET)
    cards = Card.objects.all()
    tagsAll = Tag.objects.all()

    if form.is_valid():
        tags = form.cleaned_data['tags']
        chosen_tag = form.cleaned_data['tags'].first()
        search_query = form.cleaned_data['search']

        # Заменяем None на пустую строку
        search_query = search_query if search_query is not None else ""


        if tags:
            cards = cards.filter(tags__in=tags).distinct()

        if search_query:  # Обновляем URL с учетом поиска, если введен
            search_query_lower = search_query.lower()
            cards = cards.filter(Q(title__icontains=search_query_lower) | Q(author__icontains=search_query_lower))

        if tags:  # Добавляем тег в параметры поиска перед редиректом
            params = request.GET.copy()
            params['search'] = search_query
            params['tags'] = ",".join(str(tag.id) for tag in tags)
            new_url = f"{request.path_info}?{params.urlencode()}"

            if new_url == request.get_full_path():
                return render(request, 'main/books.html', {'cards': cards, 'form': form, 'chosen_tag': chosen_tag, 'search_query': search_query, 'tagfield':Tag, 'tag_ids': tagsAll})
            return redirect(new_url)
        else:
            return render(request, 'main/books.html',{'cards': cards, 'form': form, 'tagfield': Tag, 'tag_ids': tagsAll})

    return render(request, 'main/books.html', {'cards': cards, 'form': form, 'tags_ids': tagsAll})

def render_one_of_books(request, book_id):
    card = get_object_or_404(Card, pk=book_id)
    return render(request, 'main/book_detail.html', {'card': card})

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'main/videos.html', {'videos': videos})

def video_list(request):
    form = VideoSearchForm(request.GET)
    videos = Video.objects.all()

    if form.is_valid():
        query = form.cleaned_data['search']
        videos = videos.filter(title__icontains=query)

    return render(request, 'main/videos.html', {'videos': videos, 'form': form})