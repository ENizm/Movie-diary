from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm
from django.views.generic import DetailView, UpdateView, DeleteView


def index(request):
    films = Film.objects.order_by('-grade')
    return render(request, 'main/index.html', {'title': 'Таблица фильмов', 'films': films})


class FilmsDetailView(DetailView):
    model = Film
    template_name = 'main/details_view.html'
    context_object_name = 'film'


class FilmsUpdateView(UpdateView):
    model = Film
    template_name = "main/addfilm.html"
    form_class = FilmForm


class FilmsDeleteView(DeleteView):
    model = Film
    template_name = "main/film-delete.html"
    success_url = '/'

def about(request):
    return render(request, 'main/about.html', {'title': 'О разработчике'})


def addfilm(request):
    error = ''
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Неверное заполнение'
    form = FilmForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/addfilm.html', context)
