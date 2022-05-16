from django.db import migrations, connections

def transfer_data(apps, schema_editor):
        
    ProfileToTransfert = apps.get_model('oc_lettings_site', 'Profile')
    Profile = apps.get_model('profiles', 'Profile')
    for profile_to_transfert in ProfileToTransfert.objects.all():
        Profile.objects.create(ProfileToTransfert)


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(transfer_data),
    ]
