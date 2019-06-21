from django.shortcuts import render

# Your views here

def post_list(request):
    return render(request, 'blog/post_list.html', {})