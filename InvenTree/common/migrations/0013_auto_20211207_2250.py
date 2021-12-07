# Generated by Django 3.2.5 on 2021-12-07 22:50

from django.db import migrations


def delete_task(apps, schema_editor):
    """
    Remove scheduled task to delete old user sessions.

    Ref: https://github.com/inventree/InvenTree/issues/2429
    """

    Task = apps.get_model('django_q', 'schedule')

    Task.objects.filter(func='InvenTree.tasks.delete_expired_sessions').delete()


def ksat_eteled(apps, schema_editor):
    """
    Dummy function provided for reverse migrations
    """
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0012_notificationentry'),
    ]

    operations = [
        migrations.RunPython(
            delete_task,
            reverse_code=ksat_eteled,
        )
    ]
