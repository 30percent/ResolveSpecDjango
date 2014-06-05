# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Node.parent'
        db.add_column(u'resolvespec_node', 'parent',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['resolvespec.Node']),
                      keep_default=False)

        # Removing M2M table for field parent on 'Node'
        db.delete_table(db.shorten_name(u'resolvespec_node_parent'))


    def backwards(self, orm):
        # Deleting field 'Node.parent'
        db.delete_column(u'resolvespec_node', 'parent_id')

        # Adding M2M table for field parent on 'Node'
        m2m_table_name = db.shorten_name(u'resolvespec_node_parent')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_node', models.ForeignKey(orm[u'resolvespec.node'], null=False)),
            ('to_node', models.ForeignKey(orm[u'resolvespec.node'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_node_id', 'to_node_id'])


    models = {
        u'resolvespec.node': {
            'Meta': {'object_name': 'Node'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'oneormany': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['resolvespec.Node']"})
        }
    }

    complete_apps = ['resolvespec']