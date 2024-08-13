# in blog_project/urls.py
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from blog.views import home  # Import the home view

urlpatterns = [
    path("", home, name="home"),  # Add this line for the root URL
    path("graphql", GraphQLView.as_view(graphiql=True)),
    path("admin/", admin.site.urls),
]
