from datetime import datetime

from django.contrib import auth
from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericRelation, GenericForeignKey

User = auth.get_user_model()


class ModelBase(models.Model):
    creator     = models.ForeignKey(User)
    created     = models.DateTimeField()
    updated     = models.DateTimeField()

    @property
    def is_creator(self, user):
        if self.creator == user:
            return True
        return False

    def update(self, *args, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)
        self.updated = datetime.utcnow()
        self.save()
        return self

    def save(self, *args, **kwargs):
        if self.pk is None:
            now = datetime.utcnow()
            self.created = now
            self.updated = now
        super(ModelBase, self).save(*args, **kwargs)


class Game(ModelBase):
    ACTIVE      = 'A'
    COMPLETE    = 'A'
    DELETED     = 'D'

    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (COMPLETE, 'Complete'),
        (DELETED, 'Deleted')
    )

    status  = models.CharField(max_length=1, choices=STATUS_CHOICES, default=ACTIVE)
    stage   = models.IntegerField(max_length=2, default=1)

    lastCard = models.ForeignKey('Card')


class Card(ModelBase):
    game    = models.ManyToManyField('Game')
    order   = models.IntegerField(max_length=2)

    content_type    = models.ForeignKey(ContentType)
    object_id       = models.PositiveIntegerField()
    content_object  = GenericForeignKey('content_type', 'object_id')

    def is_image(self):
        if self.order % 2 == 0:
            return True
        return False

    class Meta:
        ordering = ('order',)


class CardImage(ModelBase):
    card    = GenericRelation('Card')
    image   = models.ImageField(upload_to="cards/")


class CardText(ModelBase):
    card    = GenericRelation('Card')
    text    = models.CharField(max_length=200)