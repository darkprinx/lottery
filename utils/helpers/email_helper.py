from abc import ABC, abstractmethod


class BaseEmailService(ABC):
    @abstractmethod
    def send_email(self, *args, **kwargs):
        pass


"""This is defined assuming that it is attached to an email service. For simplicity just abstract and dummy
concreate class is implemented with dummy methods
"""


class AWSEmailService:
    def __init__(self):
        self.service_provider = "AWS SES"

    def send_email(self, user_info, email_body):
        print(email_body)
        print(
            f"Email successfully sent to {user_info['email']} via {self.service_provider} service"
        )
        return True
