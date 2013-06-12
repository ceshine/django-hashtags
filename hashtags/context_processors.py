from django.db.models import Count
from models import HashtaggedItem

def tagcount(request):
    return { 'tagcount': HashtaggedItem.objects.values('hashtag__name').order_by().annotate(Count('hashtag__name')) } 
#    print result
     
