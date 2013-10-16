# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContactModel'
        db.create_table(u'landingpage_contactmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'landingpage', ['ContactModel'])


    def backwards(self, orm):
        # Deleting model 'ContactModel'
        db.delete_table(u'landingpage_contactmodel')


    models = {
        u'landingpage.contactmodel': {
            'Meta': {'object_name': 'ContactModel'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['landingpage']