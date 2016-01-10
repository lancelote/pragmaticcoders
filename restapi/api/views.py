from .models import Event


def parse_event(event):
    """Parse event string

    Args:
        event (str): 'I just won a lottery #update @all'

    Returns:
        Event: Event instance
    """
    # ToDo : Multiple categories and persons
    # ToDO : Incorrect input case
    pass


def add_event_to_storage(event):
    """Adds event to im-memory storage

    Args:
        event (Event): Event instance

    Returns:
        None
    """
    pass


def get_10_by_category(category):
    """Return list of 10 last events by given category

    Args:
        category (str): Category to search

    Returns:
        list: last 10 events by given category
    """
    pass


def get_10_by_person(person):
    """Return list of 10 last events by given person

    Args:
        person (str): Person to search

    Returns:
        list: last 10 events by given person
    """
    pass


def get_10_by_time():
    """Return list of 10 last events

    Returns:
        list: last 10 events
    """
    pass
