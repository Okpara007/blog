from django.contrib import admin
from django.urls import path
from blog.views import home  # Import the home view

urlpatterns = [
    path("", home, name="home"),  # Root URL shows the apology message
    path("graphql/", home, name="graphql_"),  # GraphQL URL shows the apology message
    path("admin/", home, name="admin_"),  # Admin URL shows the apology message
]
