from django.urls import path
from .views import *

app_name='main'
urlpatterns = [
    path('',main,name="main"),
    path('detail/<int:id>/',detail, name="detail"),
    path('new/', new, name="new"),
    path('create/',create, name="create"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('<int:post_id>/create_comment', create_comment, name="create_comment"),
    path('<int:comment_id>/edit_comment', edit_comment, name="edit_comment"),
    path('delete_comment/<int:comment_id>', delete_comment, name='delete_comment'),
]