import csv
class PhoneContact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Phone:
    def __init__(self):
        self.contacts = []
    
    def load_contacts_from_csv(self, csv_file):
        with open('contact.csv' , 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip header row
            for row in reader:
                name, phone = row
                self.contacts.append(PhoneContact(name, phone))
def search_contacts(self, query):
        found_contacts = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query.lower() in contact.phone.lower():
                found_contacts.append(contact)
        if len(found_contacts) == 0:
            print("Aucun contact trouvé")
        else:
            print(found_contacts)