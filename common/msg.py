import json


class Message:
    def __init__(self, kind: str, **kwargs):
        self.kind = kind
        self.information = kwargs

    def encode(self) -> bytes:
        message_dict = {
            'kind': self.kind,
            'information': self.information
        }
        message_json = json.dumps(message_dict)
        return message_json.encode('utf-8')

    @staticmethod
    def decode(data: bytes):
        message_json = data.decode('utf-8')
        message_dict = json.loads(message_json)
        return Message(kind=message_dict['kind'], **message_dict['information'])
