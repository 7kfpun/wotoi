# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CandidateAnswer'
        db.create_table(u'core_candidateanswer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('answer', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.CustomUser'])),
            ('candidate_test', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.CandidateTest'])),
        ))
        db.send_create_signal(u'core', ['CandidateAnswer'])

        # Adding model 'Language'
        db.create_table(u'core_language', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'core', ['Language'])

        # Adding model 'CandidateTest'
        db.create_table(u'core_candidatetest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('requirements', self.gf('django.db.models.fields.TextField')()),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Job'])),
        ))
        db.send_create_signal(u'core', ['CandidateTest'])

        # Adding model 'Experience'
        db.create_table(u'core_experience', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'core', ['Experience'])

        # Adding model 'Job'
        db.create_table(u'core_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('until_date', self.gf('django.db.models.fields.DateField')()),
            ('is_approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.CustomUser'])),
        ))
        db.send_create_signal(u'core', ['Job'])

        # Adding M2M table for field languages on 'Job'
        m2m_table_name = db.shorten_name(u'core_job_languages')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('job', models.ForeignKey(orm[u'core.job'], null=False)),
            ('language', models.ForeignKey(orm[u'core.language'], null=False))
        ))
        db.create_unique(m2m_table_name, ['job_id', 'language_id'])

        # Adding model 'Skill'
        db.create_table(u'core_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'core', ['Skill'])

        # Adding field 'CustomUser.is_approved'
        db.add_column(u'core_customuser', 'is_approved',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CustomUser.description'
        db.add_column(u'core_customuser', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'CustomUser.email'
        db.add_column(u'core_customuser', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True),
                      keep_default=False)

        # Adding field 'CustomUser.url'
        db.add_column(u'core_customuser', 'url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'CustomUser.phone'
        db.add_column(u'core_customuser', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True),
                      keep_default=False)

        # Adding field 'CustomUser.skills'
        db.add_column(u'core_customuser', 'skills',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Skill'], null=True),
                      keep_default=False)

        # Adding field 'CustomUser.languages'
        db.add_column(u'core_customuser', 'languages',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Language'], null=True),
                      keep_default=False)

        # Adding M2M table for field experiences on 'CustomUser'
        m2m_table_name = db.shorten_name(u'core_customuser_experiences')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customuser', models.ForeignKey(orm[u'core.customuser'], null=False)),
            ('experience', models.ForeignKey(orm[u'core.experience'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customuser_id', 'experience_id'])


        # Changing field 'CustomUser.user_type'
        db.alter_column(u'core_customuser', 'user_type', self.gf('django.db.models.fields.CharField')(max_length=20))

    def backwards(self, orm):
        # Deleting model 'CandidateAnswer'
        db.delete_table(u'core_candidateanswer')

        # Deleting model 'Language'
        db.delete_table(u'core_language')

        # Deleting model 'CandidateTest'
        db.delete_table(u'core_candidatetest')

        # Deleting model 'Experience'
        db.delete_table(u'core_experience')

        # Deleting model 'Job'
        db.delete_table(u'core_job')

        # Removing M2M table for field languages on 'Job'
        db.delete_table(db.shorten_name(u'core_job_languages'))

        # Deleting model 'Skill'
        db.delete_table(u'core_skill')

        # Deleting field 'CustomUser.is_approved'
        db.delete_column(u'core_customuser', 'is_approved')

        # Deleting field 'CustomUser.description'
        db.delete_column(u'core_customuser', 'description')

        # Deleting field 'CustomUser.email'
        db.delete_column(u'core_customuser', 'email')

        # Deleting field 'CustomUser.url'
        db.delete_column(u'core_customuser', 'url')

        # Deleting field 'CustomUser.phone'
        db.delete_column(u'core_customuser', 'phone')

        # Deleting field 'CustomUser.skills'
        db.delete_column(u'core_customuser', 'skills_id')

        # Deleting field 'CustomUser.languages'
        db.delete_column(u'core_customuser', 'languages_id')

        # Removing M2M table for field experiences on 'CustomUser'
        db.delete_table(db.shorten_name(u'core_customuser_experiences'))


        # Changing field 'CustomUser.user_type'
        db.alter_column(u'core_customuser', 'user_type', self.gf('django.db.models.fields.CharField')(max_length=1))

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
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'experiences': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Experience']", 'null': 'True', 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'languages': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Language']", 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'skills': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Skill']", 'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'user_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'core.skill': {
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['core']