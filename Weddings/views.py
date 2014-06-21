from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the Moutee index.")

def detail(request, wedding_id):
    return HttpResponse("You're looking at wedding %s." % wedding_id)