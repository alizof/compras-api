# Generated by Django 5.0.4 on 2024-04-26 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_cliente_cip_alter_cliente_nome_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
