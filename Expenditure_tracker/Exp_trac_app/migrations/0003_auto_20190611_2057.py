# Generated by Django 2.1.1 on 2019-06-11 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Exp_trac_app', '0002_auto_20190604_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expenditure',
            old_name='Comments',
            new_name='comments',
        ),
    ]
