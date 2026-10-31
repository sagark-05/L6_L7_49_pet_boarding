import pytest
from pet_boarding import boarding_fee, admission_ok, checkout_status


# Name: Sagar K
# SRN: PES2UG24CS424
# Lab 6: Code Coverage Tests


def test_unknown_pet_type():
    with pytest.raises(ValueError, match="unknown pet type"):
        boarding_fee("bird", 3, False)


def test_negative_days():
    with pytest.raises(ValueError, match="invalid days"):
        boarding_fee("dog", -1, False)


def test_within_included_days():
    assert boarding_fee("dog", 1, False) == 0


def test_premium_cat():
    # Cat: 3 included days + 1 premium day.
    assert boarding_fee("cat", 5, True) == 20


def test_dog_normal_rate():
    # 4 - 2 = 2 extra days at 30 per day.
    assert boarding_fee("dog", 4, False) == 60


def test_cat_long_stay():
    # 14 - 3 = 11 extra days at 30 per day.
    assert boarding_fee("cat", 14, False) == 330


def test_dog_long_stay():
    # 13 - 2 = 11 extra days at 45 per day.
    assert boarding_fee("dog", 13, False) == 495


def test_senior_admission():
    assert admission_ok(10, 3, True) is True


def test_young_pet_rejected():
    assert admission_ok(0.5, 3, False) is False


def test_regular_admission():
    assert admission_ok(4, 2, False) is True


def test_checkout_open_long_stay_weekend():
    # Long stay cutoff: 30 + 20 = 50 minutes.
    assert checkout_status(50, True, True) == "open"


def test_checkout_late():
    # Regular cutoff: 15; late range: 0 to 14.
    assert checkout_status(10, False, False) == "late"


def test_checkout_closed():
    # Long stay cutoff: 30; below 15 is closed.
    assert checkout_status(14, True, False) == "closed"