# Generated by Django 3.1.3 on 2020-12-14 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20201214_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option', to='question.question'),
        ),
    ]
