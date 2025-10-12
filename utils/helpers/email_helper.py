from abc import ABC, abstractmethod


class BaseEmailService(ABC):
    @abstractmethod
    def send_email(self, *args, **kwargs):
        pass


"""
This assumes it is attached to an email service.
For simplicity an abstract and a dummy concrete class
are implemented with placeholder methods.
"""


class AWSEmailService:
    def __init__(self):
        self.service_provider = "AWS SES"

    def send_email(self, user_info, email_body):
        print(email_body)
        print(
            "Email successfully sent to "
            f"{user_info['email']} "
            f"via {self.service_provider} service"
        )
        return True
