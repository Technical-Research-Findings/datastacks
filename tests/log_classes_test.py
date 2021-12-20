from src.log_classes import SpecialChar


def test_answer() -> None:
    """
    Testing the ordinal function to ensure it is working as expected
    :return:
    """
    assert SpecialChar('#').ordinal_value() == 35
