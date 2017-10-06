
"""Genius backend API"""

# [START imports]
import endpoints
from protorpc import message_types
from protorpc import messages
from protorpc import remote
# [END imports]


# [START messages]
class Click(messages.Message):
    button = messages.StringField(1)
    timestamp = messages.StringField(1)
# [END messages]


# [START click_api]
@endpoints.api(name='click', version='v1')
class ClickApi(remote.Service):

    @endpoints.method(
        message_types.VoidMessage,
        Click,
        path='register',
        http_method='POST',
        name='register')
    def register(self, request):
        return Click(button=request.button, timestamp=request.timestamp)


# [START api_server]
api = endpoints.api_server([ClickApi])
# [END api_server]