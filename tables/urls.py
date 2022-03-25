from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="table"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='table-content'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='tables_post_like'),
]
