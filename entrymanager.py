from typing import List
from resouces import Entry
import os


class EntryManager:
    def __init__(self, data_path):
        self.data_path: str = data_path
        self.entries: List[Entry] = []

    def save(self):
        for entry in self.entries:
            entry.save(self.data_path)

    def load(self):
        for data in os.listdir(self.data_path):
            if not data.endswith('.json'):
                continue
            else:
                full_path = os.path.join(self.data_path, data)
                entry = Entry.load(full_path)
                self.entries.append(entry)
            return self

    def add_entry(self, title: str):
        entry = Entry(title)
        self.entries.append(entry)