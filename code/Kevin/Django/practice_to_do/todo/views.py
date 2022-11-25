from django.views.generic import ListView

from .models import ToDo

class ToDoListView(ListView):
    model = ToDo
    template_name = 'home.html'