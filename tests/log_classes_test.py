from src.log_classes import SpecialChar


def test_answer():
    assert SpecialChar('#').convertordinal() == 36
