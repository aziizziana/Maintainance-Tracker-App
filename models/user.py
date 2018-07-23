import json

class User:
    def __init__(self, first_name, last_name, email_address, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.password = password

Aziiz = User('Aziiz', 'Ziana', 'aziizziana@gmail.com', 'devziana')
Lorna = User('Lorna', 'Tumuhairwe','lornatumuhairwe@gmail.com', 'l@qyue')
Dorothy = User('Dorothy', 'Kabarozi', 'dorothykiz@gmail.com', 'dee@qw')
  
def jsonDefault(object):
    return object.__dict__

jsonAziiz = json.dumps(Aziiz, default=jsonDefault)
jsonLorna = json.dumps(Lorna, default=jsonDefault)
jsonDorothy = json.dumps(Dorothy, default=jsonDefault)

print jsonAziiz
print jsonLorna
print jsonDorothy