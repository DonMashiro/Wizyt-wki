from faker import Faker
import random

fake = Faker()
class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
    def contact(self):
        print(f"Wybieram numer +48 {self.phone} i dzwonię do {self.first_name} {self.last_name}.")
    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name)

class BusinessContact(BaseContact):
    """Klasa reprezentująca wizytówkę firmową."""
    def __init__(self, first_name, last_name, phone, email, job_title, company, work_phone):
        super().__init__(first_name, last_name, phone, email)
        self.job_title = job_title
        self.company = company
        self.work_phone = work_phone
    def contact(self):
        print(f"Wybieram numer +48 {self.work_phone} i dzwonię do {self.first_name} {self.last_name}.")

def create_contacts(contact_type, quantity):
    contacts = []
    for _ in range(quantity):
        if contact_type == "BaseContact":
            contact = BaseContact(
                fake.first_name(),
                fake.last_name(),
                fake.phone_number(),
                fake.email()
            )
        elif contact_type == "BusinessContact":
            contact = BusinessContact(
                fake.first_name(),
                fake.last_name(),
                fake.phone_number(),
                fake.email(),
                fake.job(),
                fake.company(),
                fake.phone_number()
            )
        else:
            raise ValueError("Nieprawidłowy typ wizytówki.")
        contacts.append(contact)
    return contacts

if __name__ == "__main__":
    contacts = create_contacts("BaseContact", 3)
    for contact in contacts:
        contact.contact()
        print(f"Długość etykiety: {contact.label_length}")
    contacts = create_contacts("BusinessContact", 2)
    for contact in contacts:
        contact.contact()
        print(f"Długość etykiety: {contact.label_length}")
