# Generated by Django 3.2.13 on 2022-11-03 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0016_alter_nota_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='nota',
            field=models.FloatField(),
        ),
    ]