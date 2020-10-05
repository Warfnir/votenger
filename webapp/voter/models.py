from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, name, forname, nickname,  password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            forname=forname,
            nickname=nickname
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, forname, nickname, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            forname=forname,
            nickname=nickname
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=30)
    forname = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'forname', 'nickname']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


# Possible game genres
class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    shortcut = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

# Representation of single game in DB


class Game(models.Model):
    name = models.CharField(max_length=30, unique=True)
    minimum_players = models.PositiveSmallIntegerField()
    maximum_players = models.PositiveSmallIntegerField()

    GOG = models.BooleanField(default=False)
    Steam = models.BooleanField(default=False)
    Epic = models.BooleanField(default=False)

    Windows = models.BooleanField(default=False)
    Linux = models.BooleanField(default=False)

    Coach = models.BooleanField(default=False)
    LAN = models.BooleanField(default=False)
    WAN = models.BooleanField(default=False)

    genre = models.ManyToManyField(Genre, blank=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.name


class GamePosition(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    bonus_points = models.PositiveSmallIntegerField(default=0)


class Poll(models.Model):
    owner = models.ForeignKey(
        MyUser, related_name="owner", on_delete=models.CASCADE)
    guests = models.ManyToManyField(MyUser, related_name="guests")
    games_positions = models.ManyToManyField(GamePosition)
    created_at = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)


class Vote(models.Model):
    game_position = models.ForeignKey(GamePosition, on_delete=models.CASCADE)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    value = models.IntegerField()
