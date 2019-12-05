from django.shortcuts import render

# Create your views here.


def article_list(request):
    return render(request, template_name='articles/article_list.html')