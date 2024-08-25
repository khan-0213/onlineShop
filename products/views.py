from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Products
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


class ProductListView(LoginRequiredMixin, ListView):
    model = Products
    template_name = 'product_list.html'


class ProductDetailView(DetailView):
    model = Products
    template_name = 'product_detail.html'


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Products
    template_name = 'product_edit.html'
    fields = ('product_photo', 'product_name', 'product_summary', 'product_about')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Products
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Products
    fields = ('product_photo', 'product_name', 'product_summary', 'product_about')
    template_name = 'product_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def user_profile(request):
    return render(request, 'profile.html', {'user': request.user})