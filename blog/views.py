from django.shortcuts import render

# Create your videf post_list(request):
def post_list(request):
    return render(request, 'blog/post_list.html', {})

