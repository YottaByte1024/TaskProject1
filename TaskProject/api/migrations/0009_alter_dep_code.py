# Generated by Django 4.1.1 on 2022-10-09 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_dep_options_alter_employee_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dep',
            name='code',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]