from django.shortcuts import render


def hello(request):
    if request.method == "GET":
        print(request.GET)
        name = request.GET.get('name', None)
        message = request.GET.get('message', None)
        content = {
            'name': name,
            'message': message
        }
        return render(request, 'hello/index.html', content)
