# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table(u'game_game', (
            (u'modelbase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['game.ModelBase'], unique=True, primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='A', max_length=1)),
            ('stage', self.gf('django.db.models.fields.IntegerField')(default=1, max_length=2)),
        ))
        db.send_create_signal(u'game', ['Game'])

        # Adding model 'ModelBase'
        db.create_table(u'game_modelbase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'game', ['ModelBase'])

        # Adding model 'CardImage'
        db.create_table(u'game_cardimage', (
            (u'modelbase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['game.ModelBase'], unique=True, primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'game', ['CardImage'])

        # Adding model 'CardText'
        db.create_table(u'game_cardtext', (
            (u'modelbase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['game.ModelBase'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'game', ['CardText'])

        # Adding model 'Card'
        db.create_table(u'game_card', (
            (u'modelbase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['game.ModelBase'], unique=True, primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'game', ['Card'])

        # Adding M2M table for field game on 'Card'
        m2m_table_name = db.shorten_name(u'game_card_game')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('card', models.ForeignKey(orm[u'game.card'], null=False)),
            ('game', models.ForeignKey(orm[u'game.game'], null=False))
        ))
        db.create_unique(m2m_table_name, ['card_id', 'game_id'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table(u'game_game')

        # Deleting model 'ModelBase'
        db.delete_table(u'game_modelbase')

        # Deleting model 'CardImage'
        db.delete_table(u'game_cardimage')

        # Deleting model 'CardText'
        db.delete_table(u'game_cardtext')

        # Deleting model 'Card'
        db.delete_table(u'game_card')

        # Removing M2M table for field game on 'Card'
        db.delete_table(db.shorten_name(u'game_card_game'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'game.card': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Card', '_ormbases': [u'game.ModelBase']},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'game': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['game.Game']", 'symmetrical': 'False'}),
            u'modelbase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['game.ModelBase']", 'unique': 'True', 'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {'max_length': '2'})
        },
        u'game.cardimage': {
            'Meta': {'object_name': 'CardImage', '_ormbases': [u'game.ModelBase']},
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'modelbase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['game.ModelBase']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'game.cardtext': {
            'Meta': {'object_name': 'CardText', '_ormbases': [u'game.ModelBase']},
            u'modelbase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['game.ModelBase']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'game.game': {
            'Meta': {'object_name': 'Game', '_ormbases': [u'game.ModelBase']},
            u'modelbase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['game.ModelBase']", 'unique': 'True', 'primary_key': 'True'}),
            'stage': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '2'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '1'})
        },
        u'game.modelbase': {
            'Meta': {'object_name': 'ModelBase'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['game']