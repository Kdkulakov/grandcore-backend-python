from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class AccountGroup(models.Model):
    name = models.CharField(
        blank=False,
        verbose_name='группа',
        null=False,
        max_length=50
    )

    def __str__(self):
        return self.name or 'Some group'


class Account(AbstractUser):

    username = None
    email = models.EmailField(_('email address'), unique=True)

    group = models.ForeignKey(
        AccountGroup,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    occupation = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='род деятельности'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name='avatar',
    )

    avatar_thumbnail = ImageSpecField(
        source='avatar',
        processors=[ResizeToFill(100, 100)],
        format='JPEG',
        options={'quality': 60}
    )

    second_name = models.CharField(
        blank=True,
        verbose_name='отчество',
        null=True,
        max_length=50
    )

    about = models.TextField(
        blank=True,
        verbose_name='описание',
        null=True,
        max_length=350
    )

    skills = TaggableManager()

    phone = models.CharField(
        max_length=11,
        null=True,
        blank=True,
        verbose_name='phone'
    )

    is_deleted = models.BooleanField(
        default=False,
        verbose_name='deleted'
    )

    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated'
    )

    objects = UserManager()  ## This is the new line in the User model. ##

    def __str__(self):
        return ' '.join([
            self.first_name,
            self.last_name,
        ])

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_self = Account.objects.get(pk=self.pk)
            if old_self.avatar_thumbnail and self.avatar_thumbnail != old_self.avatar_thumbnail:
                old_self.avatar_thumbnail.delete(False)
            if old_self.avatar and self.avatar != old_self.avatar:
                old_self.avatar.delete(False)
        return super(Account, self).save(*args, **kwargs)
