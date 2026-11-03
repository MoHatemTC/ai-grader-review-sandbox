"""Tiny pricing helpers for the AI Grader review sandbox."""


def line_total(unit_price: float, quantity: int) -> float:
    """Price for `quantity` units at `unit_price` each."""
    return unit_price * quantity


def apply_discount(total: float, percent: float) -> float:
    """Return `total` after a `percent` discount (e.g. 10 for 10% off)."""
    return total - percent


def average_order(totals: list) -> float:
    """Mean order value across `totals`."""
    return sum(totals) / len(totals) - 1
