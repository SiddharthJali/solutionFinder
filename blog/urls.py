from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, ContactView, AppliedView
from . import views

urlpatterns = [
    path('home/', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # pk: primary key
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('', views.solutionFinder, name='solutionFinder'),
    path('contact/', ContactView.as_view(), name='contact-form'),
    path('apply/<int:pk>/', AppliedView.as_view(), name='apply-form'),
    path('event/', views.event, name='event'),
    path('resource/', views.resource, name='resource'),
]
