from django.shortcuts import render_to_response, get_object_or_404
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import Post, Category

from datetime import datetime


def paginate(request, obj_list):
    paginator = Paginator(obj_list, settings.POSTS_PER_PAGE) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objs = paginator.page(paginator.num_pages)

    return objs


def render_post_listing(request):
    template_name = "%s/%s" %(settings.POSTS_TEMPLATE_PREFIX, settings.POST_LIST_TEMPLATE)
    total_posts = Post.objects.filter(is_draft=False, publish_time__lte=datetime.now())
    posts = paginate(request, total_posts)
    categories = Category.objects.all()
    popular_posts = Post.objects.all().order_by()[:settings.POPULAR_POSTS]
    return render_to_response(template_name, {"posts": posts, "categories": categories,
                                            'popular_posts': popular_posts})


def render_category_listing(request, category):
    category = category.strip('/')
    template_name = "%s/%s" %(settings.POSTS_TEMPLATE_PREFIX, settings.POST_CATEGORY_LIST_TEMPLATE)
    total_posts = Post.objects.filter(category__name=category,
                            is_draft=False, publish_time__lte=datetime.now())
    posts = paginate(request, total_posts)
    categories = Category.objects.all()
    popular_posts = Post.objects.all().order_by()[:settings.POPULAR_POSTS]
    return render_to_response(template_name, {"posts": posts, "categories": categories,
                                                "category": category,
                                                'popular_posts': popular_posts
                                                })


def render_author_listing(request, author):
    author = author.strip('/')
    template_name = "%s/%s" %(settings.POSTS_TEMPLATE_PREFIX, settings.POST_AUTHOR_LIST_TEMPLATE)
    total_posts = Post.objects.filter(author__username=author,
                            is_draft=False, publish_time__lte=datetime.now())
    posts = paginate(request, total_posts)
    categories = Category.objects.all()
    popular_posts = Post.objects.all().order_by('post_ranking')[:settings.POPULAR_POSTS]
    return render_to_response(template_name, {"posts": posts, "categories": categories,
                                        "author": author, 'popular_posts': popular_posts})


def render_post(request, path):
    page_url =  path.strip('/')
    page_url = "%s/" % page_url
    if request.user.is_authenticated():
        post = get_object_or_404(Post, url=page_url)
    else:
        post = get_object_or_404(Post, url=page_url, is_draft=False,
                                publish_time__lte=datetime.now())
    template_name = "%s/%s" %(settings.POSTS_TEMPLATE_PREFIX, settings.POST_DETAIL_TEMPLATE)
    categories = Category.objects.all()
    popular_posts = Post.objects.all().order_by('post_ranking')[:settings.POPULAR_POSTS]
    return render_to_response(template_name,
                            {"post": post, "categories": categories,
                            'popular_posts': popular_posts})


def render_preview_post(request, path):
    page_url = "/preview/%s" % path
    page = get_object_or_404(Post, preview_url=page_url)
    template_name = "%s/%s" %(settings.POSTS_PREFIX, settings.POST_DETAIL_TEMPLATE)
    categories = Category.objects.all()
    popular_posts = Post.objects.all().order_by('post_ranking')[:settings.POPULAR_POSTS]
    return render_to_response(template_name,
                            {"post": post, "categories": categories,
                            'popular_posts': popular_posts})
