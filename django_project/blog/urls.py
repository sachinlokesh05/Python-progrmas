from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    SearchResultsView,
    home1,
    PostListView1,
    PostImageUpdateView,
    LabelCreateView,
    archive,
    ArchiveUpdateView,
    trashed,
    TrashedUpdateView,
    ColorUpdateView,
    LabelDetailView,
    LabelUpdateView,
    PinUpdateView,
    CollUpdateView,
    RemainderUpdateView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('listview/', PostListView1.as_view(), name='blog-home1'),
    path('label_listview/', LabelDetailView.as_view(), name='label-home'),
    path('archive/', archive, name='archive_list'),
    path('trashed/', trashed, name='trashed_list'),
    path('archive/<int:pk>/update', ArchiveUpdateView.as_view(), name='archive'),
    path('remainder/<int:pk>/update',
         RemainderUpdateView.as_view(),
         name='remainder'),
    path('pin/<int:pk>/update', PinUpdateView.as_view(), name='pin'),
    path('coll/<int:pk>/update', CollUpdateView.as_view(), name='collaborator'),
    path('label/<int:pk>/update', LabelUpdateView.as_view(), name='label-update'),
    path('trashed/<int:pk>/update', TrashedUpdateView.as_view(), name='trashed'),
    path('color/<int:pk>/update', ColorUpdateView.as_view(), name='color'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('label/new/', LabelCreateView.as_view(), name='label-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/image/update/',
         PostImageUpdateView.as_view(), name='post-image-update'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
