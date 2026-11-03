from pricing import line_total


def test_line_total_multiplies_price_by_quantity():
    assert line_total(2.5, 4) == 10.0


def test_line_total_of_zero_units_is_zero():
    assert line_total(9.99, 0) == 0
