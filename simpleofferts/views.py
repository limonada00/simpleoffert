from django.shortcuts import render, redirect
from .models import Categories, SimpleOfert
#from .forms import SimpleOfertCreateModelForm
from django.urls import reverse,reverse_lazy
from . import services
from django.contrib.auth.models import User
from django.db.models import Count
from django.views.generic import ListView,DetailView,DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import ContextMixin, TemplateResponseMixin, View,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class index_view(ListView):
    #queryset = SimpleOfert.objects.all()
    template_name = 'simpleofferts/index.html'
    # def dispatch(self, request, *args, **kwargs):
    #     import ipdb; ipdb.set_trace()
    #
    #     return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(index_view, self).get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        return context

    def get_queryset(self):
        sel_category = self.request.GET.get('category', None)
        query = SimpleOfert.objects.select_related('category', 'author')
        if sel_category:
            return query.filter(category=sel_category)
        return query



"""
def index_view(request):
    if request.method == 'GET':
        sel_category = request.GET.get('category', None)
        if sel_category:
            oferts = SimpleOfert.objects.select_related('category', 'author').filter(category=sel_category)
            categories = Categories.objects.all()
            return render(request, 'simpleofferts/index.html', locals())
    oferts = SimpleOfert.objects.select_related('category', 'author')
    categories = Categories.objects.all()

    return render(request, 'simpleofferts/index.html', locals())


def create_offert(request):
    if request.method == 'POST':
        form = SimpleOfertCreateModelForm(request.POST, request.FILES)
        if form.is_valid():
            services.create_offert(**form.cleaned_data)
            return redirect(reverse('simpleofferts:index'))

    form = SimpleOfertCreateModelForm()
    return render(request, 'simpleofferts/create_offer.html', locals())
"""

class CreateOfferView(LoginRequiredMixin, CreateView):
    model = SimpleOfert
    fields = ("title", "content", "category", "image_field", "price")
    template_name = 'simpleofferts/create_offer.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('simpleofferts:index')


class UpdateOfferView(LoginRequiredMixin, UpdateView):
    model = SimpleOfert
    pk_url_kwarg = 'offer'
    fields = ("title", "content", "category", "price")
    template_name = 'simpleofferts/create_offer.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('simpleofferts:index')


class DetailOfferView(DetailView):
    pk_url_kwarg = 'offer'
    template_name = 'simpleofferts/detail_form.html'
    queryset = SimpleOfert.objects.all()


class DeleteOfferView(LoginRequiredMixin,DeleteView):
    model = SimpleOfert
    template_name = 'simpleofferts/delete_confirm.html'
    success_url = reverse_lazy('simpleofferts:index')


class StatsView(TemplateView):
    template_name = "simpleofferts/stats.html"

    def get_context_data(self, **kwargs):
        context = super(StatsView, self).get_context_data(**kwargs)
        context['top_categories'] = Categories.objects.all().annotate(number_of_oferts=Count('categorys__id')).order_by('-number_of_oferts')[:3]
        context['top_authors'] = SimpleOfert.objects.values("author__username").annotate(number_of_oferts=Count('author__id')).annotate(number_of_categorys=Count('category__id' ,distinct=True)).order_by('-number_of_oferts')[:3]
        return context
"""
def stats_view(request):
    top_categories = Categories.objects.all().annotate(number_of_oferts=Count('categorys__id')).order_by('-number_of_oferts')[:3]
    top_authors = SimpleOfert.objects.values("author__username").annotate(number_of_oferts=Count('author__id')).annotate(number_of_categorys=Count('category__id' ,distinct=True)).order_by('-number_of_oferts')[:3]
    return render(request, 'simpleofferts/stats.html', locals())
"""