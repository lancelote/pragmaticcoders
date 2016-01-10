import re

from .models import Event, data

PATTERN = re.compile(r'^([\w\s]+) #(\w+) @(\w+)$')


def parse_event(event):
    """Parse event string

    Args:
        event (str): 'I just won a lottery #update @all'

    Returns:
        Event: Event instance
    """
    # ToDo : Multiple categories and persons
    # ToDO : Incorrect input case
    text, category, person = re.match(PATTERN, event).groups()
    return Event(text, category, person)


def add_event_to_storage(event):
    """Adds event to im-memory storage

    Args:
        event (Event): Event instance

    Returns:
        None
    """
    data.append(event)


def get_10_by_category(category):
    """Return list of 10 last events by given category

    Args:
        category (str): Category to search

    Returns:
        list: last 10 events by given category
    """
    last_10_by_category = []
    for i in range(len(data) - 1, -1, -1):
        if len(last_10_by_category) == 10:
            break
        if data[i].category == category:
            last_10_by_category.append(data[i])
    return last_10_by_category


def get_10_by_person(person):
    """Return list of 10 last events by given person

    Args:
        person (str): Person to search

    Returns:
        list: last 10 events by given person
    """
    return person


def get_10_by_time():
    """Return list of 10 last events

    Returns:
        list: last 10 events
    """
    pass
