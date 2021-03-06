# Generated by Django 3.0.3 on 2020-04-23 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Terme',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('terme', models.CharField(max_length=100)),
                ('raffinement', models.CharField(max_length=100)),
                ('importe', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RelationAVerifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.CharField(max_length=100)),
                ('poids', models.IntegerField()),
                ('terme1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ter1', to='chatbot.Terme')),
                ('terme2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ter2', to='chatbot.Terme')),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=3)),
                ('poids', models.IntegerField()),
                ('terme1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terme1', to='chatbot.Terme')),
                ('terme2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terme2', to='chatbot.Terme')),
            ],
        ),
    ]
