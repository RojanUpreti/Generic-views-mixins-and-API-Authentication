from django.urls import path
# from .views import article_list,article_detail
# from .views import ArticleAPIView,ArticleDetails
from .views import GenericAPIView

# urlpatterns=[
#     path('article/',article_list),
#     path('detail/<int:pk>/',article_detail),
# ]

urlpatterns=[
    path('generic/article/<int:id>/',GenericAPIView.as_view()),
]

# urlpatterns=[
#     path('article/',ArticleAPIView.as_view()),
#     path('detail/<int:id>/',ArticleDetails.as_view())
# ]