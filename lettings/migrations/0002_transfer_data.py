from django.db import migrations

def data_transfer(apps, schema_editor):

    AddressToTransfert = apps.get_model('oc_lettings_site', 'Address')
    Address = apps.get_model('lettings', 'Address')
    for address_to_transfert in AddressToTransfert.objects.all():
        Address.objects.create(number = address_to_transfert.number,
                               street = address_to_transfert.street,
                               city = address_to_transfert.city,
                               state = address_to_transfert.state,
                               zip_code = address_to_transfert.zip_code,
                               country_iso_code = address_to_transfert.country_iso_code)

    LettingToTransfert = apps.get_model('oc_lettings_site', 'Letting')
    Letting = apps.get_model('lettings', 'Letting')
    for letting_to_transfert in LettingToTransfert.objects.all():
        address = get_lettings_address(letting_to_transfert.address,
                                       Address)
        Letting.objects.create(title = letting_to_transfert.title,
                               address = address)


def get_lettings_address(letting_address_to_transfert, lettings_model_Address):
    for letting_address in lettings_model_Address.objects.all():
        address_match = (
            letting_address_to_transfert.number == letting_address.number
            and
            letting_address_to_transfert.street == letting_address.street
            and
            letting_address_to_transfert.city == letting_address.city
            and
            letting_address_to_transfert.state == letting_address.state
            and
            letting_address_to_transfert.zip_code == letting_address.zip_code
            and
            letting_address_to_transfert.country_iso_code == letting_address.country_iso_code)
        if address_match:
            return letting_address


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(data_transfer),
    ]
