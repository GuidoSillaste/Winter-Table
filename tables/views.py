from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, DessertForm


class PostList(generic.ListView):
    """" doc string """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "table.html"
    paginate_by = 6


class PostDetail(View):
    """" doc string """
    def get(self, request, slug, *args, **kwargs):
        """" doc string """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        desserts = post.dessert.order_by("-created_on")
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        dessert_form = DessertForm()

        return render(
            request,
            "table-content.html",
            {
                "post": post,
                "desserts": desserts,
                "comments": comments,
                "dessert_form": dessert_form,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """" doc string """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        desserts = post.dessert.order_by("-created_on")
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        dessert_form = DessertForm(data=request.POST)
        if dessert_form.is_valid():
            dessert = dessert_form.save(request.POST)
            dessert.post = post
            dessert.save()
        else:
            dessert_form = DessertForm()

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "table-content.html",
            {
                "post": post,
                "comments": comments,
                "desserts": desserts,
                "dessert_form": dessert_form,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):
    """" doc string """
    def post(self, request, slug, *args, **kwargs):
        """" doc string """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('table-content', args=[slug]))
