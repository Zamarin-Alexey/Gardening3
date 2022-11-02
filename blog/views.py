from django.shortcuts import render


def home_page(request):
    return render(request, 'blog/home_page.html', {'title': 'Блог'})


def post(request, post_id):
    return render(request, 'blog/post.html', {'title': 'Блог', 'post_id': post_id})
