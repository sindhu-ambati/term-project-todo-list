# Generated by Django 3.1.2 on 2020-12-21 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('1', '1️⃣'), ('2', '2️⃣'), ('3', '3️⃣'), ('4', '4️⃣'), ('5', '5️⃣'), ('6', '6️⃣'), ('7', '7️⃣'), ('8', '8️⃣'), ('9', '9️⃣'), ('10', '🔟')], max_length=2),
        ),
    ]
