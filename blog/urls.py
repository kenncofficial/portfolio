from django.urls import path
from .views import BlogListView, CategoryDetailView, BlogPostDetailView, tagged_view, UpdateCommentView, DeleteCommentView

urlpatterns = [
    path('blog_list/', BlogListView.as_view(), name='bloglist'),
    path('article/<slug:slug>/', BlogPostDetailView.as_view(), name='BlogPost-details'),
    path('tag/<slug:slug>/', tagged_view, name="tagged"),
    path('category/<slug:slug>/', CategoryDetailView, name='category_detail'),
    path('article/<int:pk>/update_comment', UpdateCommentView.as_view(), name='Update_comment'),
    path('article/<int:pk>/delete_comment', DeleteCommentView.as_view(), name='Delete_comment'),


]