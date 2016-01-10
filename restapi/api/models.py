from datetime import datetime

# ToDo : Switch to normal DB
data = []  # In-memory temporary storage


class Event(object):

    def __init__(self, text, category, person):
        self.text = text
        self.category = category
        self.person = person
        self.time = datetime.now()
