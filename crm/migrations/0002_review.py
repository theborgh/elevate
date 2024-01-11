# Generated by Django 5.0.1 on 2024-01-11 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=50)),
                ('review_title', models.CharField(max_length=100)),
                ('review_text', models.TextField(max_length=1000)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.task')),
            ],
        ),
    ]