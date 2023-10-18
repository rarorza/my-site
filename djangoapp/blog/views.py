from blog.models import Page, Post
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render

POSTS_PER_PAGE = 9


def index(request):
    posts = Post.objects.get_published()

    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_objs = paginator.get_page(page_number)

    page_title = "Home"
    context = {"page_objs": page_objs, "page_title": page_title}
    return render(request, "blog/index.html", context=context)


def created_by(request, author_pk):
    user_obj = User.objects.filter(pk=author_pk).first()
    if user_obj is None:
        raise Http404()

    author_full_name = user_obj.username
    if user_obj.first_name:
        author_full_name = f"{user_obj.first_name} {user_obj.last_name}"

    posts = Post.objects.get_published().filter(created_by__pk=author_pk)

    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_objs = paginator.get_page(page_number)

    page_title = f"Posts de {author_full_name}"
    context = {
        "page_objs": page_objs,
        "page_title": page_title,
    }
    return render(request, "blog/index.html", context=context)


def category(request, slug):
    posts = Post.objects.get_published().filter(category__slug=slug)

    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_objs = paginator.get_page(page_number)

    if len(posts) == 0:
        raise Http404()

    page_title = f"{page_objs[0].category.name} - Category"
    context = {
        "page_objs": page_objs,
        "page_title": page_title,
    }
    return render(request, "blog/index.html", context=context)


def tag(request, slug):
    posts = Post.objects.get_published().filter(tags__slug=slug)

    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_objs = paginator.get_page(page_number)

    if len(posts) == 0:
        raise Http404()

    page_title = page_objs[0].tags.filter(slug=slug).first().name
    context = {
        "page_objs": page_objs,
        "page_title": f"{page_title} - Tag",
    }
    return render(request, "blog/index.html", context=context)


def search(request):
    search_value = request.GET.get("search").strip()
    posts = Post.objects.get_published().filter(
        Q(title__icontains=search_value)
        | Q(excerpt__icontains=search_value)
        | Q(content__icontains=search_value)
    )[:POSTS_PER_PAGE]

    page_title = f"{search_value[:30]} - Search"
    context = {
        "page_objs": posts,
        "search_value": search_value,
        "page_title": page_title,
    }
    return render(request, "blog/index.html", context=context)


def page(request, slug):
    page_obj = Page.objects.filter(is_published=True, slug=slug).first()
    if page_obj is None:
        raise Http404()

    page_title = page_obj.title
    context = {"page": page_obj, "page_title": page_title}
    return render(request, "blog/page.html", context=context)


def post(request, slug):
    post_obj = Post.objects.get_published().filter(slug=slug).first()
    if post_obj is None:
        raise Http404()

    page_title = post_obj.title
    context = {"post": post_obj, "page_title": page_title}
    return render(request, "blog/post.html", context=context)
