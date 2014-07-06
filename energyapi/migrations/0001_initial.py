# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Building'
        db.create_table(u'energyapi_building', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('buildingId', self.gf('django.db.models.fields.IntegerField')()),
            ('numUnits', self.gf('django.db.models.fields.IntegerField')()),
            ('numStories', self.gf('django.db.models.fields.IntegerField')()),
            ('decadeBuilt', self.gf('django.db.models.fields.IntegerField')()),
            ('grossFloorArea', self.gf('django.db.models.fields.IntegerField')()),
            ('totalEleckWh', self.gf('django.db.models.fields.IntegerField')()),
            ('totalkWhNoWeather', self.gf('django.db.models.fields.IntegerField')()),
            ('totalElecBill', self.gf('django.db.models.fields.IntegerField')()),
            ('totalVolume', self.gf('django.db.models.fields.IntegerField')()),
            ('totalGaskWh', self.gf('django.db.models.fields.IntegerField')()),
            ('totalGasBill', self.gf('django.db.models.fields.IntegerField')()),
            ('elecBaseNormAvgConsumption', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
        ))
        db.send_create_signal(u'energyapi', ['Building'])


    def backwards(self, orm):
        # Deleting model 'Building'
        db.delete_table(u'energyapi_building')


    models = {
        u'energyapi.building': {
            'Meta': {'object_name': 'Building'},
            'buildingId': ('django.db.models.fields.IntegerField', [], {}),
            'decadeBuilt': ('django.db.models.fields.IntegerField', [], {}),
            'elecBaseNormAvgConsumption': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'grossFloorArea': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numStories': ('django.db.models.fields.IntegerField', [], {}),
            'numUnits': ('django.db.models.fields.IntegerField', [], {}),
            'totalElecBill': ('django.db.models.fields.IntegerField', [], {}),
            'totalEleckWh': ('django.db.models.fields.IntegerField', [], {}),
            'totalGasBill': ('django.db.models.fields.IntegerField', [], {}),
            'totalGaskWh': ('django.db.models.fields.IntegerField', [], {}),
            'totalVolume': ('django.db.models.fields.IntegerField', [], {}),
            'totalkWhNoWeather': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['energyapi']