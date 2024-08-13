import graphene
from graphene_django import DjangoObjectType
from .models import Author, Post, Comment
from django.core.paginator import Paginator

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author

class PostType(DjangoObjectType):
    class Meta:
        model = Post

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment

class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType, author_id=graphene.Int(), page=graphene.Int(), page_size=graphene.Int())
    post = graphene.Field(PostType, id=graphene.Int(required=True))
    all_comments = graphene.List(CommentType, post_id=graphene.Int(required=True))

    def resolve_all_posts(self, info, author_id=None, page=1, page_size=10):
        if author_id:
            posts = Post.objects.filter(author_id=author_id)
        else:
            posts = Post.objects.all()
        
        paginator = Paginator(posts, page_size)
        return paginator.get_page(page).object_list
    
    def resolve_post(self, info, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            return None

    def resolve_all_comments(self, info, post_id):
        return Comment.objects.filter(post_id=post_id)

class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)

    post = graphene.Field(PostType)

    def mutate(self, info, title, content):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authentication required")

        post = Post.objects.create(title=title, content=content, author=user)
        return CreatePost(post=post)

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

