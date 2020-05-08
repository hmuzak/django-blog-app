from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from taggit.models import Tag, slugify

# Create your views here.
def post_view(request):
    posts = Post.objects.order_by('-published')
    common_tags = Post.tags.most_common()[:4]
    query       = request.POST.get('search')
    if query:
        posts   = posts.filter(title__icontains=query)
    form        = PostForm(request.POST)
    if form.is_valid():
        new_post        = form.save(commit=False)
        new_post.slug   = slugify(new_post.title)
        new_post.save()
        form.save_m2m()
    context = {
        'posts':posts,
        'common_tags':common_tags,
        'form':form
    }
    return render(request, 'posts.html', context)

def tagged_post(request, slug):
    tag     = get_object_or_404(Tag, slug=slug)
    posts   = Post.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'post':posts
    }
    return render(request, 'tagged.html', context)

def post_detail(request,slug):
    post    = get_object_or_404(Post, slug=slug)
    return render(request, 'detail.html', {'post':post})
