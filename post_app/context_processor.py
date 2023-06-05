from .models import PostModel, Category

def latest_news(request):
    news = PostModel.objects.filter(status=PostModel.Status.Published).order_by('-published_time')[:10]
    categories = Category.objects.all()

    context = {
        'news': news,
        'categories': categories
    }
    return context