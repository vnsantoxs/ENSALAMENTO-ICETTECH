# Generated by Django 4.2.1 on 2023-06-02 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id_grade', models.IntegerField(primary_key=True, serialize=False)),
                ('ano', models.IntegerField()),
                ('versao', models.CharField(max_length=12)),
                ('codigo', models.CharField(max_length=6)),
            ],
        ),
    ]
