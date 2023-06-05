from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import TemplateView, DetailView, ListView
from .forms import ContactForm
from django.views.static import HttpResponse


# Create your views here.
# def PostView(request):
#     post_list = PostModel.objects.all()
#     context = {
#         'post_list': post_list
#     }
#     return render(request, 'news/home.html', context)
#
# def PostDetail(request, id, status=PostModel.Status.Published):
#     post = get_object_or_404(PostModel, id=id)
#     context = {
#         'post': post
#     }
#     return render(request, 'news/post_detail.html', context)

class PostView(ListView):
    model = PostModel
    template_name = 'news/home.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = PostModel
    template_name = 'single_page.html'
    context_object_name = 'post'


# def IndexView(request):
#     posts = PostModel.objects.all().order_by('-published_time')
#     local_one = PostModel.objects.filter(category__name='Maxalliy')[:1]
#     local_news = PostModel.objects.filter(category__name='Maxalliy')[1:6]
#     context = {
#         'posts': posts,
#         'local_one': local_one,
#         'local_news': local_news
#     }
#     return render(request, 'index.html', context)


def aboutview(request):
    return render(request, 'about.html')


def singleview(request):
    return render(request, 'single_page.html')


# def contact_view(request):
#     print(request.POST)
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse("Biz bilan bog`langaningiz uchun raxmat")
#     context = {
#         'form': form
#     }
#     return render(request, 'contact.html', context=context)

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm
        context = {
            'form': form
        }
        return render(request, 'contact.html', context=context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse('Biz bilan bog`langaningiz uchun tashakkur')
        context = {
            'form': form
        }
        return render(request, 'contact.html', context=context)


class IndexView(ListView):
    model = PostModel
    template_name = 'index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['posts'] = PostModel.objects.all().order_by('-published_time')[:5]
        context['local_one'] = PostModel.objects.filter(category__name='Maxalliy').order_by('-published_time')[:1]
        context['local_news'] = PostModel.objects.filter(category__name='Maxalliy').order_by('-published_time')
        return context


class LocalNewsView(ListView):
    model = PostModel
    template_name = 'local.html'
    context_object_name = 'local_news'

    def get_queryset(self):
        news = self.model.objects.filter(category__name='Maxalliy', status=self.model.Status.Published)
        return news
