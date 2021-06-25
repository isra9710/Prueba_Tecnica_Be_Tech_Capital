from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.urls import reverse

class Mail:
    
    
    @staticmethod
    def get_absolute_url(url):
        if settings.DEBUG:
            return 'http://127.0.0.1:8000{}'.format(
                reverse(url)
            )
    
    
    
    @staticmethod
    def send_mail(user, user1, user2):
        subject = 'Tu registro se llevó a cabo con éxito'
        template = get_template('emails/email.html')
        content = template.render({
            'user':user,
        
        })
        message = EmailMultiAlternatives(subject,
                                         'Mensaje importante',
                                         settings.EMAIL_HOST_USER,
                                         [user.email])
        message.attach_alternative(content, 'text/html')
        message.send()