# Generated by Django 2.2.7 on 2019-11-06 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='edAuditTrace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_id', models.IntegerField(unique=True)),
                ('act_user', models.CharField(max_length=10)),
                ('act_staffid', models.CharField(max_length=10)),
                ('act_descr', models.CharField(max_length=100)),
                ('act_datetime', models.DateField()),
                ('act_other', models.CharField(max_length=30)),
            ],
        ),
    ]