from django.shortcuts import render
from .models import Note

MENU={"Главная":"/", "О блоге":"/about", "Страница поста":"/post", "Отзывы":"/note_page"}

def note_page(request):
    notes = Note.objects.all()
    title = "Отзывы"
    data = {"menu": MENU, "title": title, "notes": notes}
    return render(request, './note_page.html', context=data)

def form(request):
    notes = Note.objects.all()
    title = "Форма добавления отзыва"
    data = {"menu": MENU, "title": title, "notes": notes}
    return render(request, './form.html', context=data)

def thanks(request):
    fio = request.POST["fio"]
    email = request.POST["email"]
    text = request.POST["text"]
    Note.objects.create(fio=fio, email=email, text=text, status=False)
    title = "Успех"
    data = {"menu": MENU, "title": title, "fio": fio}
    return render(request, './thanks.html', context=data)