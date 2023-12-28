
from Exception.Exception import AuthenticationException, AuthorizationException


class SecurityManager:
    def authenticate_user(self, user):
        try:
            raise AuthenticationException("Authentication failed.")
        except AuthenticationException as e:
            print(f"Authentication Error: {e}")

    def authorize_user(self, user, resource):
        try:
            raise AuthorizationException("Unauthorized access.")
        except AuthorizationException as e:
            print(f"Authorization Error: {e}")