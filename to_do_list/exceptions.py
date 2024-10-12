"""Module with custom exceptions."""

class DatabaseIntegrityError(Exception):
    """Database Integrity Error trows when an item exists on database."""
    def __init__(self, item_id):
        super().__init__(
            f"Database Integrity Error: An item with {item_id} already exists."
        )
