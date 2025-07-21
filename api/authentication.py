from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import requests
from django.contrib.auth.models import AnonymousUser

class TokenNoopUser(AnonymousUser):
    """
    Django Rest Framework needs an user to consider authenticated
    """

    def __init__(self, user_info):
        super().__init__()
        self.user_info = user_info

    @property
    def is_authenticated(self):
        return True

class KeycloakAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = request.headers.get('Authorization')
        if not auth or not auth.startswith('Bearer '):
            return None

        token = auth.split(' ')[1]

        print("token ", token)

        # Inserisci i tuoi dati
        client_id = 'django-backend'
        client_secret = 'cITWGgFW01Y5F03EP4we8xsIA3krRi0T'
        realm = 'master'
        url = f'http://localhost:8080/realms/{realm}/protocol/openid-connect/token/introspect'

        data = {
            'token': token,
            'client_id': client_id,
            'client_secret': client_secret,
        }

        print("data ", data)

        response = requests.post(url, data=data)
        result = response.json()

        print("result ", result)

        if not result.get('active'):
            raise AuthenticationFailed('Token non valido o scaduto')

        return (TokenNoopUser(user_info=result), None)
