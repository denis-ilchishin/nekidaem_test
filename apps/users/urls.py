from django.urls import include, path

from .views import (AccountView, MarkAsSeen, PostCreateView, SubscribeView,
                    UnsubscribeView)

urlpatterns = [
    path('', AccountView.as_view(), name='account'),
    path('post-create/', PostCreateView.as_view(), name='post-create'),
    path(
        'api/',
        include(
            [
                path('subscribe/', SubscribeView.as_view(), name='api-subscribe'),
                path('unsubscribe/', UnsubscribeView.as_view(), name='api-unsubscribe'),
                path('seen/', MarkAsSeen.as_view(), name='api-seen'),
            ]
        ),
    ),
]
