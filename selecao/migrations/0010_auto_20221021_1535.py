# Generated by Django 3.2.13 on 2022-10-21 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0009_alter_candidato_deficiencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='autodeclaracao',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', max_length=1, verbose_name='O candidato é autodeclarado preto, pardo ou indígena'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='deficiencia',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', max_length=1, verbose_name='Possui deficiência?'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='ensino_fundamental_publico',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', max_length=1, verbose_name='O candidato cursou o ensino fundamental integralmente em escola pública?'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='ensino_medio_publico',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', max_length=1, verbose_name='O candidato cursou o ensino médio integralmente em escola pública?'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='renda_bruta',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', max_length=1, verbose_name='O candidato possui renda bruta mensal igual ou inferior a 1,5 salários mínimos per capita?'),
        ),
    ]