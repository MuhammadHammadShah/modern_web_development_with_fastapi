from models.creature import Creatures
import service.creature as code

sample = Creatures(name="khanbabatest", country="USA",
                   area="LosAngeles", description="not a king", aka="nothing")


def test_create():
    resp = code.create(sample)
    assert resp == sample


def test_get_exists():
    resp = code.get_one("khanbabatest")
    assert resp == sample


def test_get_missing():
    resp = code.get_one("khanbaba2")
    assert resp == sample
