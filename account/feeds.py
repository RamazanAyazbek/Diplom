from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post
from django.utils import timezone

class LatestPostsFeed(Feed):
    title="My blog"
    # link=reverse_lazy('account:projects')
    link=""
    description="Updating or creating posts"


    def items(self):
        one_day_ago = timezone.now() - timezone.timedelta(days=1)
        updated_posts = Post.objects.filter(updated_at__gte=one_day_ago)
        # posts=Post.objects.order_by('-updated_at')
        return updated_posts
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.description
#   https://simpleisbetterthancomplex.com/feed.xml 
