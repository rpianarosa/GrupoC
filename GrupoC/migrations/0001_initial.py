# Generated by Django 4.0.1 on 2022-01-15 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cerveza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, verbose_name='nombre')),
                ('IBU', models.IntegerField()),
                ('grad_alcohol', models.IntegerField()),
            ],
        ),
    ]