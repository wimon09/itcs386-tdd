import pytest

from shipping import shipping_fee


# Rule 1: 0 kg ต้องถูกปฏิเสธ
def test_zero_weight_is_rejected():
    with pytest.raises(ValueError, match="more than 0"):
        shipping_fee(0)


def test_negative_weight_is_rejected():
    with pytest.raises(ValueError, match="more than 0"):
        shipping_fee(-1)


@pytest.mark.parametrize("weight_kg, expected_fee", [
    (0.5, 40),   # Rule 2: ภายในช่วงไม่เกิน 1 kg
    (1, 40),     # Rule 2: ขอบบนที่ 1 kg
    (1.1, 60),   # Rule 3: มากกว่า 1 kg
    (5, 60),     # Rule 3: ขอบบนที่ 5 kg
    (5.2, 70),   # Rule 4: เริ่มเกิน 5 kg
    (6, 70),     # Rule 4: เกินมา 1 kg พอดี
    (7, 80),     # Rule 4: เกินมา 2 kg
])
def test_shipping_fee(weight_kg, expected_fee):
    assert shipping_fee(weight_kg) == expected_fee