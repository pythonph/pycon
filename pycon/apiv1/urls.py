from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    KeynoteListAPIView,
    NormalSpeakerListAPIView,
)

speaker_patterns = format_suffix_patterns([
    path(
        'keynote/list/',
        KeynoteListAPIView.as_view(),
        name='keynote_list'
    ),
    path(
        'normal/list/',
        NormalSpeakerListAPIView.as_view(),
        name='normal_list'
    ),
])

app_name = 'apiv1'
urlpatterns = [
    path('speakers/', include(speaker_patterns)),
]
