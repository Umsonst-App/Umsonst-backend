from django.urls import re_path
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/unread_messages_count/$', consumers.UnreadMessagesCountConsumer.as_asgi()),
    re_path(r'ws/all_unread_messages_count/$', consumers.UnreadMessagesGeneralCountConsumer.as_asgi()),
    re_path(r"chat/(?P<room_name>[-\w]+)/$", consumers.ChatConsumer.as_asgi()),
]
