# Generated by Django 2.1 on 2018-08-05 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180805_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='polygon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='core.Polygon'),
        ),
        migrations.AlterField(
            model_name='polygon',
            name='mapathon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='polygon', to='core.Mapathon'),
        ),
    ]
