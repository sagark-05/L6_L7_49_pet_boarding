from hypothesis import given, strategies as st
from pet_boarding import parse_booking, stay_average, payable_fee


@given(st.text() | st.none())
def test_parse_booking_no_crash(s):
    parse_booking(s)


@given(st.text() | st.none())
def test_stay_average_no_crash(s):
    stay_average(s)


@given(st.text() | st.none())
def test_payable_fee_no_crash(s):
    payable_fee(s)

import pytest


def test_valid_booking():
    assert parse_booking(" dog:5 ") == ("Dog", 5.0)


def test_correct_average():
    assert stay_average("2,5,7") == pytest.approx(14 / 3)


def test_correct_payable_fee():
    assert payable_fee("1500|100") == pytest.approx(1670.0)


def test_discount_exceeds_fee():
    assert payable_fee("100|200") == 0.0


def test_invalid_inputs_rejected():
    assert parse_booking("5") is None
    assert parse_booking("dog:-1") is None
    assert stay_average("1,,3") is None
    assert payable_fee("nan|0") is None