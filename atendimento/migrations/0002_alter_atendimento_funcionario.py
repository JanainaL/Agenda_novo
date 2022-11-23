# Generated by Django 4.1.2 on 2022-11-22 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0001_initial'),
        ('atendimento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='funcionario',
            field=models.ForeignKey(help_text='Nome do funcionário', on_delete=django.db.models.deletion.CASCADE, to='funcionario.funcionario', verbose_name='Funcionário'),
        ),
    ]