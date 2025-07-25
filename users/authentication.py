from django.contrib.auth.backends import BaseBackend
from users.models import User

class Auth(BaseBackend):
    def authenticate(self, request, phone_number=None, password=None):
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None