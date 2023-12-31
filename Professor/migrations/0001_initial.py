# Generated by Django 4.2.1 on 2023-06-02 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id_professor', models.IntegerField(primary_key=True, serialize=False)),
                ('nome_professor', models.CharField(default='NULL', max_length=60)),
                ('email_professor', models.EmailField(default='NULL', max_length=254)),
                ('senha_professor', models.CharField(default='NULL', max_length=20)),
                ('siape_professor', models.CharField(default='NULL', max_length=8)),
                ('area_atuacao_professor', models.CharField(default='NULL', max_length=15)),
                ('comorbidade', models.BooleanField(default=False)),
                ('estado_professor', models.BooleanField(default=False)),
            ],
        ),
    ]
