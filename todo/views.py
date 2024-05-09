from django.shortcuts import redirect, render
from django.views.generic import View, CreateView
from django.urls import reverse_lazy

from todo.forms import TaskForm
from todo.models import Task


class TasksView(View):
    def get(self, *args, **kwargs):
        tasks = Task.objects.filter(user=self.request.user).order_by('-is_done')
        return render(self.request, 'index.html', {'tasks': tasks})

    def post(self, *args, **kwargs):
        task_id = self.request.POST.get('id')
        task = Task.objects.get(id=task_id)
        if(not task.is_done):
            task.is_done = True
        else:
            task.is_done = False
        task.save()
        tasks = Task.objects.filter(user=self.request.user).order_by('-is_done')
        return render(self.request, 'index.html', {'tasks': tasks})


class AddTask(CreateView):
    model = Task
    template_name = 'index.html'
    success_url = reverse_lazy('tasks')
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        print(self.request.user)
        form.save()
        return redirect('tasks')
