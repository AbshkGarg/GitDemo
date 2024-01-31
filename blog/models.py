from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.user',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    
#     We can follow Django’s suggestion and add a get_absolute_url to our model. This is a
# best practice that you should always do. It sets a canonical URL for an object so even if
# the structure of your URLs changes in the future, the reference to the specific object
# is the same. In short, you should add a get_absolute_url() and __str__() method to
# each model you write.
    
# That means in order for this route to work we must also pass in an argument with the
# pk or primary key of the object. Confusingly, pk and id are interchangeable in Django
# though the Django docs recommend using self.id with get_absolute_url . So we’re
# telling Django that the ultimate location of a Post entry is its post_detail view which
# is posts/<int:pk>/ so the route for the first entry we’ve made will be at posts/1 .