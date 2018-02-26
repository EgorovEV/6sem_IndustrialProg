from django.shortcuts import render

def post_list(request):
    return render(request, 'TODO_List/post_list.html', {})
