# Generated by Django 4.1.1 on 2022-10-10 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_dep_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dep',
            name='head',
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_appointment', models.DateTimeField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_change', models.DateTimeField(auto_now=True)),
                ('dep', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointments', to='api.dep')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointments', to='api.employee')),
            ],
            options={
                'verbose_name': 'appointment',
                'verbose_name_plural': 'appointments',
            },
        ),
    ]