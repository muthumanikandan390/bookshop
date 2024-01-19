from django.contrib.auth.backends import BaseBackend
from .models import Userprofile

class PlainTextPasswordBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = Userprofile.objects.get(username=username)
            if password == user.password:
                return user
        except Userprofile.DoesNotExist:
            pass
        return None

    def get_user(self, user_id):
        try:
            return Userprofile.objects.get(pk=user_id)
        except Userprofile.DoesNotExist:
            return None