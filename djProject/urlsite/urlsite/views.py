from django.http import HttpResponse

def main_page(request):
    return HttpResponse("main page")

def product(request, lang):
    resp = f'language: {lang}'
    return HttpResponse(resp)

def post(request, id, blog_id=1):
    resp = f'Post id: {id}, blog_id: {blog_id}'
    return HttpResponse(resp)