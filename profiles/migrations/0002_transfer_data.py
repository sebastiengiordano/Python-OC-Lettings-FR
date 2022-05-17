from django.db import migrations

def data_transfer(apps, schema_editor):

    ProfileToTransfert = apps.get_model('oc_lettings_site', 'Profile')
    Profile = apps.get_model('profiles', 'Profile')
    for profile_to_transfert in ProfileToTransfert.objects.all():
        Profile.objects.create(user = profile_to_transfert.user,
                               favorite_city = profile_to_transfert.favorite_city)


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(data_transfer),
    ]
