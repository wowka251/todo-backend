import json
import os


def print_with_indent(value, indent=0): # wird in der class verwendet in print_entries
    print('\t' * indent + value)
    # for item in value:
    # print_with_indent(item, indent +1 )


def entry_from_json(listik: dict):
    entry = Entry(listik['title'])
    for item in listik.get('entries', []):
        ret = entry_from_json(item)
        entry.add_entry(ret)
    return entry


class Entry:
    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent

    def add_entry(self, entry):  # hier wird ein Objekt entgegen genommen
        self.entries.append(entry)  # die liste bestet aus Objekten
        # alle parents sind None bis hier, hier wird der parent auf das object gesetzt in dem wir sind
        entry.parent = self

    def print_entries(self, indent=0):
        print_with_indent(self.title, indent)
        for i in self.entries:
            i.print_entries(indent=indent + 1)

    def json(self):  # wird in save aufgerufen
        my_dict = {
            'title': self.title,
            'entries': [item.json() for item in self.entries]
        }
        return my_dict

    @classmethod
    def from_json(cls, listik: dict):
        entry = cls(listik['title'])
        for item in listik.get('entries', []):
            ret = cls.from_json(item)
            entry.add_entry(ret)
        return entry

    def save(self, path):  # die datein speichern in json format
        new_datei = f'{self.title}.json'  # erstellen ein titel der datei
        full_path = os.path.join(path, new_datei)  # genaue pfad zur datei erstelle
        with open(full_path, 'w') as datei:  # datei öffnen oder erstellen im write -> alles wir überschrieben
            content = self.json()  # die daten im form von dict holen
            json.dump(content, datei)  # die daten in form von json in die Datei schreiben

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as open_file:
            dicti = json.load(open_file)
            entry = cls.from_json(dicti)
            return entry


def __str__(self):
        return self.title
