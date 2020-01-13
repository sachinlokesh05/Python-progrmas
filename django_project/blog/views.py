from .models import Post, Label
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.generics import GenericAPIView
from blog.serializers import NotesSerializer
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.contrib import messages
from pymitter import EventEmitter

ee = EventEmitter()

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def home1(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home1.html', context)


def archive(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/archive.html', context)


def trashed(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/trashed.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-is_pined', '-date_posted']
    paginate_by = 5


class PostListView1(ListView):
    model = Post
    template_name = 'blog/home1.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-is_pined', '-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted', '-is_pined')


class PostDetailView(DetailView):
    model = Post


class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    # template_name = 'blog/label_form.html'
    # template_name = 'blog/post_form.html'  # <app>/<model>_<viewtype>.html
    # context_object_name = 'posts'
    fields = ['user', 'name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # template_name = 'blog/post_form.html'  # <app>/<model>_<viewtype>.html
    # context_object_name = 'posts'
    fields = ['title', 'content', 'post_image', 'label', 'is_pined']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'label', 'color',
              'reminder', 'is_archive', 'is_trashed', 'is_pined', 'collaborators']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        if str(query) in cache:
            # get results from cache
            object_list = cache.get(str(query))
            return object_list

            # return Response(products, status=status.HTTP_201_CREATED)

        else:
            object_list = Post.objects.filter(
                Q(title__icontains=query)
            )
            cache.set(str(query), object_list, timeout=CACHE_TTL)
            return object_list

            # results = [product.to_json() for product in products]
            # store data in cache
            # cache.set('product', results, timeout=CACHE_TTL)
            # return Response(results, status=status.HTTP_201_CREATED)
            # object_list = Post.objects.filter(
            #     Q(title__icontains=query)
            # )
            # return object_list


#  if 'product' in cache:
#         # get results from cache
#         products=cache.get('product')
#         return Response(products, status = status.HTTP_201_CREATED)

#     else:
#         products=Product.objects.all()
#         results=[product.to_json() for product in products]
#         # store data in cache
#         cache.set(product, results, timeout = CACHE_TTL)
#         return Response(results, status = status.HTTP_201_CREATED)

class PostImageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['post_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ArchiveUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['is_archive']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class TrashedUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['is_trashed']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ColorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['color']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class LabelDetailView(ListView):
    post_label = Post.objects.all()
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'post_label'
    paginate_by = 5


def detail(request, place_id):
    label_name = Label.objects.get(pk=post_id)
    names = label_name.area.all()

    return render_to_response('blog/home.html', {
        "label_name": label_name,
        "names": names,
    })


class LabelUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['label']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PinUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['is_pined']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CollUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['collaborators']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class RemainderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['reminder']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class Celery(GenericAPIView):
    serializer_class = NotesSerializer

    def get(self, request):
        reminder_data = Post.objects.filter(reminder__isnull=False)
        start = timezone.now()
        end = timezone.now() + timedelta(minutes=1)
        for i in range(len(reminder_data)):
            if start < reminder_data.values()[i]["reminder"] < end:
                user_id = reminder_data.values()[i]['user_id']
                user = User.objects.get(id=user_id)
                mail_message = render_to_string('blog/email_reminder.html', {
                    'user': user,
                    'domain': get_current_site(request).domain,
                    'note_id': reminder_data.values()[i]["user_id"]
                })
                ee.emit(user.email, mail_message)
                return HttpResponse("remaider is set")
        return HttpResponse(reminder_data)
