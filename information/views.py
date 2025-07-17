from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import New, Category
from .forms import AddNewsForm


def news_list_view(request):
    news = New.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {
        'latest_news': news,
        'categories': categories
    })


def news_detail_view(request, pk):
    news = get_object_or_404(New, id=pk)
    categories = Category.objects.all()

    if request.method == 'POST':
        form = AddNewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect(reverse('news_detail', kwargs={'pk': pk}))
    else:
        form = AddNewsForm(instance=news)

    return render(request, 'news_detail.html', {
        'news': news,
        'form': form,
        'categories': categories,
    })


def add_news_view(request):
    if request.method == 'POST':
        form = AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = AddNewsForm()

    categories = Category.objects.all()
    return render(request, 'add_news.html', {
        'news_form': form,
        'categories': categories,
    })


def delete_news_view(request, pk):
    news = get_object_or_404(New, id=pk)
    if request.method == 'POST':
        news.delete()
        return redirect(reverse('home'))
    return render(request, 'news_delete_confirm.html', {'news': news})
