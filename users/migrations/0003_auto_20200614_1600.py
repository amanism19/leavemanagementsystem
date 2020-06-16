# Generated by Django 2.2 on 2020-06-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200614_0531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentor_id', models.IntegerField()),
                ('student_id', models.IntegerField()),
                ('purpose', models.TextField()),
                ('duration', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'Leave_Info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MenStu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_id', models.IntegerField()),
                ('mentor_id', models.IntegerField()),
            ],
            options={
                'db_table': 'ment_stu',
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='role',
            table='roles',
        ),
        migrations.AlterModelTable(
            name='userrole',
            table='users_role',
        ),
    ]