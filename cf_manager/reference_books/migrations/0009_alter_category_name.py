# Generated by Django 5.2.1 on 2025-05-30 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0008_alter_subcategory_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, help_text='Clash flow category name', max_length=30, unique=True),
        ),
    ]
