# Generated by Django 5.0.3 on 2024-03-25 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_type', models.CharField(max_length=50)),
                ('price_small', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_medium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_large', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
