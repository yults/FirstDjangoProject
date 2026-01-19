from django.http import HttpResponse

def main_page(request):
    return HttpResponse("main page")

def product(request):
    return HttpResponse("product")

def category(request):
    return HttpResponse("category")