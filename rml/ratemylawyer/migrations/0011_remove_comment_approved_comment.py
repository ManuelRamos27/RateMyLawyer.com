

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratemylawyer', '0010_alter_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
    ]
