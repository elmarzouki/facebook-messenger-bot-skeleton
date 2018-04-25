import os

from django.conf import settings
from django.conf.urls import url
from django.http import JsonResponse
from django.core.wsgi import get_wsgi_application
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

settings.configure(
    DEBUG=True,
    SECRET_KEY='I_AM_A_DUMMY_KEY_CHANGE_ME',
    ROOT_URLCONF='app.wsgi',
    ALLOWED_HOSTS=['*'],
)


def send_facebook_message(recipient_id, message_text):

        pprint("sending message to {recipient}: {text}".format(
            recipient=recipient_id, text=message_text)
            )

        params = {
            "access_token": os.environ["PAGE_ACCESS_TOKEN"]
        }
        headers = {
            "Content-Type": "application/json"
        }
        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "text": message_text
            }
        })
        result = requests.post(
            "https://graph.facebook.com/v2.6/me/messages",
            params=params, headers=headers, data=data)
        if result.status_code != 200:
            pprint(result.status_code)
            pprint(result.text)


class MessengerBot(View):
    def get(self, request, *args, **kwargs):
        if self.request.GET.get('hub.verify_token') ==\
                os.environ["VERIFY_TOKEN"]:
            return JsonResponse({
                'data': self.request.GET.get('hub.challenge')
                })
        else:
            return JsonResponse({'data': 'Error, invalid token'})

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                # Check to make sure the received call is a message call
                # This might be delivery, optin, postback for other events
                if 'message' in message:
                    # Print the message to the terminal
                    pprint(message)
                    # Assuming the sender only sends text. Non-text messages
                    # like stickers, audio, pictures
                    # are sent as attachments and must be handled accordingly.
                    send_facebook_message(
                        message['sender']['id'], message['message']['text']
                        )
        return JsonResponse({'data': 'ok!'})

urlpatterns = [
    url(r'^$', MessengerBot.as_view()),
]

application = get_wsgi_application()
