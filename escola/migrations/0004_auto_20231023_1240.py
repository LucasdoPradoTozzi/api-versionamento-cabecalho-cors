# Generated by Django 3.1.3 on 2023-10-23 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_auto_20231023_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='celular',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]