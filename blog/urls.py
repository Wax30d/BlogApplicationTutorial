from django.urls import path
from . import views

# This allows you to organize URLs by
# application and use the name when referring to them.
app_name = "blog"

urlpatterns = [
    # mapped to the post_list view.
    path('', views.post_list, name='post_list'),

    # Pattern takes the following 4 arguments and is
    # mapped to the post_detail view.
    # Use angle brackets to capture the values from the URL. Any
    # value speciﬁed in the URL pattern as <parameter> is captured as a
    # string. You use path converters, such as <int:year> , to speciﬁcally
    # match and return an integer and <slug:post> to speciﬁcally match a slug.
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
]
