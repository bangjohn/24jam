# Generated by Django 4.1.4 on 2022-12-30 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_transaksitopup_invoice_alter_transaksitopup_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaksitopup',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
