from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    # This is the ﬁeld for the post title. This ﬁeld is CharField ,
    # which translates into a VARCHAR column in the SQL database.
    title = models.CharField(max_length=250)

    # This is a ﬁeld intended to be used in URLs.
    # You have added the unique_for_date parameter to this ﬁeld
    # to prevent multiple posts from having the same slug for a given date.
    slug = models.SlugField(max_length=250, unique_for_date='publish')

    # This ﬁeld deﬁnes a many-to-one relationship
    # a user can write any number of posts.
    # In this case, you are relying on the User model of the Django authentication system.
    # when the referenced user is deleted, the database will also delete all related blog posts.

    # You specify the name of the reverse relationship,
    # from User to Post , with the related_name a attribute.
    # This will allow you to access related objects easily.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    # Since you are using auto_now_add here,
    # the date will be saved automatically when creating an object.
    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    # You use a choices parameter,
    # so the value of this ﬁeld can only be set to one of the given choices.
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    """The Meta class inside the model contains metadata. You tell Django
to sort results by the publish ﬁeld in descending order by default
when you query the database. You specify the descending order
using the negative preﬁx. By doing this, posts published recently
will appear ﬁrst."""
    class Meta:
        ordering = ('-publish',)

    """The __str__() method is the default human-readable representation
of the object. Django will use it in many places, such as the
administration site."""
    def __str__(self):
        return self.title

    # used the get_absolute_url() method in your templates to link to speciﬁc posts.
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])
