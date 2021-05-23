# Generated by Django 3.2 on 2021-05-23 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_auto_20210523_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='children',
        ),
        migrations.AddField(
            model_name='tag',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='item.tag'),
        ),
    ]
