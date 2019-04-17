import requests
import traceback
from src.utils import constant


class MessageInfo(object):
    # class contains information about a message.
    def __init__(self, sender_id=None, recipient_id=None, text_message=None):
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.text_message = text_message

    def is_message_empty(self):
        """
        Check message empty or not.

        :return: True if message is empty, otherwise, return false.
        """
        return True if self.text_message is None or self.text_message == '' else False


def verify_token(request):
    """
    Verify token from facebook.

    :param config: appconfig
    :param request: get request from facebook
    :return: verify_token if facebook verify token equals with app verify token, otherwise, return "invalid app_code"
    """
    try:
        if request.args.get("hub.verify_token") == constant.FB_AT_WORK_VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return "invalid app_code"
    except:
        print('Error when verify token: \n', traceback.format_exc())
        return "invalid app_code"


def message_info_from_request(json_from_fb):
    """
    Get message info and pack to MessageInfo object in a json_request from facebook.

    :param json_from_fb: json_request from facebook.
    :return: MessageInfo if have text message, otherwise, return None.
    """
    try:
        entries = json_from_fb['entry']
        list_message_info = []
        for entry in entries:
            list_of_message = entry['messaging']
            for message in list_of_message:
                sender_id = message['sender']['id']
                recipient_id = message['recipient']['id']
                text_message = message['message']['text']
                list_message_info.append(MessageInfo(sender_id, recipient_id, text_message))

        return list_message_info
    except:
        print('Error when get question from facebook \n', traceback.format_exc())
        return None


def response_answer_to_fb(recipient_id, message):
    """
    Request Messenger API to response an message to user.

    :param recipient_id: recipient_id
    :param message: text message
    :return: status code of request.
    """

    payload = {"statusCode": 200, "recipient": {"id": recipient_id}, "message": {"text": message}}
    headers = {"statusCode": "200", 'content-type': 'application/json'}
    response = requests.post(
        url=constant.FB_AT_WORK_API + '?access_token=' + constant.FB_AT_WORK_ACCESS_TOKEN, json=payload,
        headers=headers)
    if response.status_code == 200:
        print('response_answer_to_fb success ', response.json())
    else:
        print('response_answer_to_fb error code: ', response.status_code, ' json: ', response.json())
    return response.status_code
