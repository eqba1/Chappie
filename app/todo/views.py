from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from cms.ajax_views import (AjaxDetailView, AjaxCreateView , AjaxUpdateView, AjaxDeleteView)
from cms.mixins import ModelMixin
from cms.views import CoreListView
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.mixins import LoginRequiredMixin

class OwnedMixin(LoginRequiredMixin):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            owner=self.request.user
        )
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TodoList(OwnedMixin, CoreListView):
    model = Todo


class TodoDetail(OwnedMixin, AjaxDetailView):
    model = Todo


class TodoCreate(OwnedMixin, AjaxCreateView):
    model = Todo
    form_class = TodoForm


class TodoUpdate(OwnedMixin, AjaxUpdateView):
    model = Todo
    form_class = TodoForm


class TodoDelete(OwnedMixin, AjaxDeleteView):
    model = Todo
