# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'CustomUser.user'
        db.delete_column(u'core_customuser', 'user_id')

        # Adding field 'CustomUser.password'
        db.add_column(u'core_customuser', 'password',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=128),
                      keep_default=False)

        # Adding field 'CustomUser.last_login'
        db.add_column(u'core_customuser', 'last_login',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'CustomUser.is_superuser'
        db.add_column(u'core_customuser', 'is_superuser',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CustomUser.username'
        db.add_column(u'core_customuser', 'username',
                      self.gf('django.db.models.fields.CharField')(default=1, unique=True, max_length=30),
                      keep_default=False)

        # Adding field 'CustomUser.first_name'
        db.add_column(u'core_customuser', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)

        # Adding field 'CustomUser.last_name'
        db.add_column(u'core_customuser', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)

        # Adding field 'CustomUser.is_staff'
        db.add_column(u'core_customuser', 'is_staff',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CustomUser.is_active'
        db.add_column(u'core_customuser', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'CustomUser.date_joined'
        db.add_column(u'core_customuser', 'date_joined',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding M2M table for field groups on 'CustomUser'
        m2m_table_name = db.shorten_name(u'core_customuser_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customuser', models.ForeignKey(orm[u'core.customuser'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customuser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'CustomUser'
        m2m_table_name = db.shorten_name(u'core_customuser_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customuser', models.ForeignKey(orm[u'core.customuser'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customuser_id', 'permission_id'])


    def backwards(self, orm):
        # Adding field 'CustomUser.user'
        db.add_column(u'core_customuser', 'user',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['auth.User'], unique=True),
                      keep_default=False)

        # Deleting field 'CustomUser.password'
        db.delete_column(u'core_customuser', 'password')

        # Deleting field 'CustomUser.last_login'
        db.delete_column(u'core_customuser', 'last_login')

        # Deleting field 'CustomUser.is_superuser'
        db.delete_column(u'core_customuser', 'is_superuser')

        # Deleting field 'CustomUser.username'
        db.delete_column(u'core_customuser', 'username')

        # Deleting field 'CustomUser.first_name'
        db.delete_column(u'core_customuser', 'first_name')

        # Deleting field 'CustomUser.last_name'
        db.delete_column(u'core_customuser', 'last_name')

        # Deleting field 'CustomUser.is_staff'
        db.delete_column(u'core_customuser', 'is_staff')

        # Deleting field 'CustomUser.is_active'
        db.delete_column(u'core_customuser', 'is_active')

        # Deleting field 'CustomUser.date_joined'
        db.delete_column(u'core_customuser', 'date_joined')

        # Removing M2M table for field groups on 'CustomUser'
        db.delete_table(db.shorten_name(u'core_customuser_groups'))

        # Removing M2M table for field user_permissions on 'CustomUser'
        db.delete_table(db.shorten_name(u'core_customuser_user_permissions'))


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.candidateanswer': {
            'Meta': {'object_name': 'CandidateAnswer'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'candidate_test': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.CandidateTest']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.CustomUser']"})
        },
        u'core.candidatetest': {
            'Meta': {'object_name': 'CandidateTest'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Job']"}),
            'requirements': ('django.db.models.fields.TextField', [], {})
        },
        u'core.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'experiences': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Experience']", 'null': 'True', 'symmetrical': 'False'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'languages': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Language']", 'null': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'skills': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Skill']", 'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'user_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'core.experience': {
            'Meta': {'object_name': 'Experience'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'core.job': {
            'Meta': {'object_name': 'Job'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Language']", 'symmetrical': 'False'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'until_date': ('django.db.models.fields.DateField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.CustomUser']"})
        },
        u'core.language': {
            'Meta': {'object_name': 'Language'},
            'alpha2': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'core.skill': {
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['core']