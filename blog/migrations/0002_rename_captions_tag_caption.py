# Generated by Django 4.1.3 on 2022-12-11 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("blog", "0001_initial")]

    operations = [migrations.RenameField(model_name="tag", old_name="captions", new_name="caption")]
