# Generated by Django 2.1.5 on 2019-06-04 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dir_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dir', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'Dir_detail',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Dir_domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=20)),
                ('file_ext', models.CharField(max_length=6)),
                ('createtime', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'Dir_domain',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='dir_detail',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dirscan.Dir_domain'),
        ),
    ]
