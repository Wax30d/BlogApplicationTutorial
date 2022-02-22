from django.contrib import admin
from .models import Post


# This decorator performs the same function as the admin.site.register()
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    """You can see that the ﬁelds displayed on the post list page are the
ones you speciﬁed in the list_display attribute."""
    list_display = ('title', 'slug', 'author', 'publish', 'status')

    """The list page now includes a right sidebar that allows you to ﬁlter the results by the
ﬁelds included in the list_filter attribute."""
    list_filter = ('status', 'created', 'publish', 'author')

    """A search bar has appeared on the page."""
    search_fields = ('title', 'body')

    """
    Next, click on the ADD POST link. You will also note some changes
here. As you type the title of a new post, the slug ﬁeld is ﬁlled in
automatically. You have told Django to prepopulate the slug ﬁeld
with the input of the title ﬁeld using the prepopulated_fields
attribute.
    """
    prepopulated_fields = {'slug': ('title',)}

    """You can also see that the posts are
ordered by STATUS and PUBLISH columns by default. You have
speciﬁed the default sorting criteria using the ordering attribute."""
    ordering = ('status', 'publish')

    """Also, the author ﬁeld is now displayed with a lookup widget that
can scale much be er than a drop-down select input when you have
thousands of users. This is achieved with the raw_id_fields attribute"""
    raw_id_fields = ('author',)

    """Just below the search bar, there are navigation links to navigate
    through a date hierarchy; this has been deﬁned by the
    date_hierarchy attribute."""
    date_hierarchy = 'publish'
