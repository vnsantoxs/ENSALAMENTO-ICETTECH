# Generated by Django 4.2.3 on 2023-07-16 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alocacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alocacao',
            name='tipo_alocacao',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]