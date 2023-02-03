import json
import os
from dataclasses import dataclass

# STORE_PATH = os.path.join(os.path.dirname(__file__), "store.json")
# Find path to Workflow Data folder
# https://www.alfredapp.com/help/workflows/advanced/variables/
STORE_PATH = os.path.join(os.environ["alfred_workflow_data"], "store.json")


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
    # Check if directory exists
    if not os.path.exists(os.path.dirname(STORE_PATH)):
        os.makedirs(os.path.dirname(STORE_PATH))

    # Check if store exists
    if not os.path.exists(STORE_PATH):
        return []

    with open(STORE_PATH, "r") as f:
        return [StoreItem(**item) for item in json.load(f)]


def save_store_item(item: StoreItem):
    """
    Save single store to file.

    Args:
        item (StoreItem): Store item to save.
    """
    store = load_store()
    store.append(item)
    save_store(store)


def save_store(items: list[StoreItem]):
    """
    Save store to file.

    Args:
        items (list[StoreItem]): Store items to save.
    """
    if not os.path.exists(os.path.dirname(STORE_PATH)):
        os.makedirs(os.path.dirname(STORE_PATH))

    with open(STORE_PATH, "w") as f:
        json.dump([item.__dict__ for item in items], f)
