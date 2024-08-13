from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Blog API. Go to /graphql to interact with the API.")
