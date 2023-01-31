import json
import os
from dataclasses import dataclass

STORE_PATH = os.path.join(os.path.dirname(__file__), "store.json")


@dataclass
class StoreItem:
    """
    Store item. Includes keyword used to query the URL and the URL itself.
    """

    keyword: str
    url: str


def load_store() -> list[StoreItem]:
    """
    Load store from file.

    Returns:
        list[StoreItem]: Store.
    """
    # Check if store exists
    if not os.path.exists(STORE_PATH):
        return []

    with open(STORE_PATH, "r") as f:
        return [StoreItem(**item) for item in json.load(f)]


def save_store(item: StoreItem):
    """
    Save store to file.

    Args:
        item (StoreItem): Store item to save.
    """
    store = load_store()
    store.append(item)
    with open(STORE_PATH, "w") as f:
        json.dump([item.__dict__ for item in store], f)
