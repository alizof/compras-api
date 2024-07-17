# Generated by Django 5.0.4 on 2024-04-26 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cliente_tipo_alter_cliente_cip_alter_cliente_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipo',
            field=models.CharField(blank='false', choices=[('F', 'Fisica'), ('J', 'Juridica')], default='F', max_length=1),
        ),
    ]
