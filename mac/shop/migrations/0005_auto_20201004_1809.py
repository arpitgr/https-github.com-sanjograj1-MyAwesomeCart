# Generated by Django 3.0.8 on 2020-10-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='id',
        ),
        migrations.AddField(
            model_name='contact',
            name='msg_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.CharField(default='', max_length=50),
        ),
    ]