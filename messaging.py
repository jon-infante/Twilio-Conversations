import os
from twilio.rest import Client
import dotenv
import random
dotenv.load_dotenv('.env')

class MessageInterface():
    def __init__(self,ACCOUNT_SID,AUTH_TOKEN):
        """
        ACCOUNT_SID: str
        AUTH_TOKEN: str
        """
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def sendMessage(self, receiver, sender, text):
        """Sends a message from one endpoint to the next, given two numbers and a message.
        
        from: str
        to: str
        text: str
        """
        return self.client.messages.create(
                                        body=f'{text}',
                                        from_=f'{sender}',
                                        to=f'{receiver}'
        )
    def loopMessage(self, receiver, sender, words, num):
        """Sends a specified number of random words to a phone.
        
        receiver: str
        sender: str
        words: List
        num: int
        """
        for i in range(num):
            r = random.randint(0, len(words)-1)
            self.client.messages.create(
                                        body=f'{i} {words[r]}',
                                        from_=f'{sender}',
                                        to=f'{receiver}'
            )


if __name__ == '__main__':
    cell = os.environ['CELL_PHONE']
    proxy = os.environ['PROXY_PHONE']
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    words = ['banana', 'apple', 'watermelon', 'cherry', 'grape']
    interface = MessageInterface(account_sid, auth_token)
    interface.loopMessage(cell, proxy, words, 200)
