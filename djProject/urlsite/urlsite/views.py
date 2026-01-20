from django.http import HttpResponse
from django.shortcuts import render

MENU={"Главная":"/", "О блоге":"/about", "Страница поста":"/post", "Отзывы":"/note_page"}
def main_page(request):
    title = "Главная страница"
    data = {"menu": MENU, "title": title}
    return render(request, './index.html', context=data)

def about(request):
    title = "О блоге"
    about_text = "Кулинарный блог с очень простыми рецептами"
    data = {"menu": MENU, "title": title, "about_text" : about_text }
    #resp = f'language: {lang}'
    return render(request, './about.html', context=data)

def post(request):
    title = "Страница поста"
    post_text= "Рецепт льда: заморозьте воду"
    data = {"menu": MENU, "title": title, "post_text" : post_text }
    #resp = f'Post id: {id}, blog_id: {blog_id}'
    return render(request, './post.html', context=data)
