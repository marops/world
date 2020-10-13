from django.db import models
from django.contrib.gis.db import models

class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    geom = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

    class Meta:
        managed = False
        ordering=['name']


class States(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states'
        verbose_name_plural = "states"

    def __str__(self):
        return self.name


class Tiles(models.Model):
    name = models.CharField(unique=True,max_length=255, blank=False, null=False)
    note = models.CharField(max_length=255, blank=True, null=True)
    geom = models.PolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tiles'
        verbose_name_plural = "tiles"

    def __str__(self):
        return self.name


class Projects(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects'
        verbose_name_plural = "projects"
