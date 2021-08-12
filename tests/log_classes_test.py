from src.log_classes import SpecialChar


def test_answer():
    assert SpecialChar('#').convert_ordinal() == 36
