from django.shortcuts import render

def blog_view(request):
    blog_names = [
        {'name': 'Benjamin Franklin', 'description': "Three can keep a secret, if two of them are dead."},
        {'name': 'William Shakespeare', 'description': "To be or not to be, that is the question."},
        {'name': 'Alexander Pope', 'description': "To err is human, to forgive, divine."},
    ]
    data = {"blogs": blog_names}
    return render(request, 'blog.html', data)
