from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdateView, DeleteArticleView, AddCategoryView, categoryView, categoryListView, contactView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_article/', AddPostView.as_view(), name='add-article'),
    path('add_category/', AddCategoryView.as_view(), name='add-category'),
    path('article/edit/<int:pk>', UpdateView.as_view(), name='update-article'),
    path('article/delete/<int:pk>', DeleteArticleView.as_view(), name='delete-article'),
    path('category/<str:cats>/', categoryView, name='category'),
    path('category-list/', categoryListView, name='category-list'),
    path('contact/', contactView , name='contact'),
]