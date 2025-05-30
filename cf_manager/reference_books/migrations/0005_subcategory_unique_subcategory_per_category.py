# Generated by Django 5.2.1 on 2025-05-28 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0004_alter_category_name'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='subcategory',
            constraint=models.UniqueConstraint(fields=('name', 'category'), name='unique_subcategory_per_category'),
        ),
    ]
