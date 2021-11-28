import csv


class PhoneCatalog:
    """
    Implement Phone catalog class. It should be able to add, edit, delete, search contacts.
    Stores all data into csv file
    """
    def __init__(self, catalog_file):
        self.catalog_file = catalog_file
        self.field_names = ['id', 'phone_number', 'first_name', 'last_name', 'additional_info']
        with open(self.catalog_file, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=self.field_names)
            writer.writeheader()

    # Add contact to catalog
    def add_contact(self, contact):
        with open(self.catalog_file, 'a') as f:
            writer = csv.DictWriter(f, fieldnames=self.field_names)
            writer.writerow(contact)

    # edit existing contact from catalog
    def edit_contact(self, new_contact):
        contacts = []
        with open(self.catalog_file, 'r+') as f:
            reader = csv.DictReader(f)
            for contact in reader:
                if int(contact['id']) == new_contact['id']:
                    contact.update(new_contact)

                contacts.append(contact)
        self.write_in_file(contacts)

    # delete contact from catalog
    def delete_contact(self, contact):
        contacts = []
        with open(self.catalog_file, 'r+') as f:
            reader = csv.DictReader(f)
            for item in reader:
                if int(item['id']) != contact['id']:
                    contacts.append(item)

        self.write_in_file(contacts)

    # Show full contact list
    def show_all_contacts(self):
        with open(self.catalog_file, 'r') as f:
            reader = csv.DictReader(f)
            return [contact for contact in reader]

    # Search contact in catalog
    def search_contact(self, number=None, name=None):
        with open(self.catalog_file, 'r') as f:
            reader = csv.DictReader(f)
            return [contact for contact in reader if int(contact['phone_number']) == number or name in (contact['first_name'], contact['last_name'])]

    # Write data in file
    def write_in_file(self, contacts):
        with open(self.catalog_file, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=self.field_names)
            writer.writeheader()
            for contact in contacts:
                writer.writerow(contact)


if __name__ == '__main__':
    catalog = PhoneCatalog('contacts.csv')

    catalog.add_contact({
        'id': 1,
        'first_name': 'Shushan',
        'last_name': 'Hovhannisyan',
        'phone_number': '123456',
        'additional_info': 'hello'
    })

    catalog.add_contact({
        'id': 2,
        'first_name': 'Anna',
        'last_name': 'Karapetyan',
        'phone_number': '54565',
        'additional_info': 'second contact'
    })


    print(catalog.show_all_contacts())
    print(catalog.search_contact(123456))
    print(catalog.search_contact(name='Anna'))
    catalog.add_contact({
        'id': 3,
        'first_name': 'Anna',
        'last_name': 'Smith',
        'phone_number': '245458',
        'additional_info': 'third contact'
    })

    catalog.edit_contact({
        'id': 3,
        'first_name': 'Anna',
        'last_name': 'Smith',
        'phone_number': '8888888',
        'additional_info': 'updated third contact'
    })
    print(catalog.search_contact(name='Anna'))

    catalog.delete_contact({'id': 3})
    print(catalog.show_all_contacts())
