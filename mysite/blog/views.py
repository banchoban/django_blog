from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post


class PostListView(ListView):
    queryset = Post.objects.all()  # todo fix queryset for only publishd posts
    context_object_name = 'posts'
    paginate_by = 3
    template_name = './post/list.html'


'''
def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer delivr the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, './post/list.html', {'page': page, 'posts': posts})
'''


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request, './post/detail.html', {'post': post})

