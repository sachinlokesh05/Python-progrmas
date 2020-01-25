from random import randint
from chartjs.views.lines import BaseLineChartView
from django.views.generic import TemplateView
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Post, Label
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.generics import GenericAPIView
from blog.serializers import NotesSerializer
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.views.generic import View

# charts
from itertools import islice
from random import randint, shuffle

from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView

from chartjs.colors import COLORS, next_color
from chartjs.util import date_range, value_or_null
from chartjs.views.columns import BaseColumnsHighChartsView
from chartjs.views.lines import (
    BaseLineChartView,
    BaseLineOptionsChartView,
    HighchartPlotLineChartView,
)
from chartjs.views.pie import HighChartDonutView, HighChartPieView


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
from datetime import timedelta

ee = EventEmitter()

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def home(request):
    context = {
        'posts': Post.objects.filter(username=request.user.username)
    }
    return render(request, 'blog/home.html', context)


def home1(request):
    context = {
        'posts': Post.objects.all(),
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
        print(start, end)
        print(reminder_data)
        for i in range(len(reminder_data)):
            print(i)
            print(start < reminder_data.values()[i]['reminder'] < end)
            print(reminder_data.values()[5]['reminder'])
            if start < reminder_data.values()[i]['reminder'] < end:
                print(reminder_data.values()[i]['reminder'])
                user_id = reminder_data.values()[i]['user_id']
                print(user_id)
                user = User.objects.get(id=user_id)
                print(user)
                mail_message = render_to_string('blog/email_reminder.html', {
                    'user': user,
                    'domain': get_current_site(request).domain,
                    'note_id': reminder_data.values()[i]["user_id"]
                })
                print(mail_message)
                ee.emit(user.email, mail_message)
        return HttpResponse(reminder_data)


# class chart_view(APIView):
#     """
#     View to list all users in the system.

#     * Requires token authentication.
#     * Only admin users are able to access this view.
#     """
#     authentication_classes = []
#     permission_classes = []

#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         qs_set = User.objects.all().count()
#         label = ["user", "Red", "Blue", "Yellow", "Green", "Purple", "Orange"]
#         default = [qs_set, 12, 19, 3, 5, 2, 3]
#         data = {
#             "labels": label,
#             "default": default,
#         }
#         return Response(data)
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request, format=None):
        users_count = User.objects.all().count()
        notes_count = Post.objects.all().count()
        notes_pinned_count = Post.objects.filter(is_pined=True).count()
        notes_others_count = Post.objects.filter(is_pined=False).count()
        notes_archived_count = Post.objects.filter(is_archive=False).count()
        labels_count = Label.objects.all().count()
        labels = ["users count", "notes count", "pinned notes", "Unpinned notes", "archived notes", "labels count"]
        default_items = [users_count, notes_count, notes_pinned_count, notes_others_count, notes_archived_count, labels_count]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/charts.html', {})

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='blog/charts.html')
line_chart_json = LineChartJSONView.as_view()
