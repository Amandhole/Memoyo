from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.utils import timezone

#### This class is used to customized default user model in django
class MyCustomManager(BaseUserManager) :
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields) :
        if not email : 
            raise ValueError("Email is required")
        now = timezone.now()
        email = email 
        user = self.model(
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            last_login = now,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password,**extra_fields) :
        return self._create_user(email, password,False,False,**extra_fields)

    def create_superuser(self, email, password,**extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        return user