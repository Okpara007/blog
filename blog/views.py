from django.http import HttpResponse

def home(request):
    return HttpResponse(
        "I apologize for any inconvenience. Please access the GraphQL interface at "
        "'https://blog-api-vyot.onrender.com/graphql'. To obtain a token, go to "
        "'https://blog-api-vyot.onrender.com/api/token/'. Once again, I apologize for any inconvenience."
    )
