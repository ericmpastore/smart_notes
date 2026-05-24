from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, ListView, DetailView

# Create your views here.
from .models import Notes

class NotesCreateView(CreateView):
    model = Notes
    fields = ['title','note']
    success_url = '/smart/notes'

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class PopularNotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    queryset = Notes.objects.filter(count_likes__gte=1)

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

def detail(request,pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Object does not exist.")
    return render(request, 'notes/notes_detail.html',{'note':note})