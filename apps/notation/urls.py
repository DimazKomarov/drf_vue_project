from django.urls import path
from .views import NoteListCreateView, NoteDetailView

app_name = "notation"

urlpatterns = [
    path("notes/", NoteListCreateView.as_view(), name="note-list-create"),
    path("notes/<int:pk>/", NoteDetailView.as_view(), name="note-detail"),
]
