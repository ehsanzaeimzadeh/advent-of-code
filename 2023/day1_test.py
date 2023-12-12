from day1 import part_1


def test_1():
    assert part_1(["1ksjd34hdkj23hd0", "kasdh2jkhd75", "sad532asd10"]) == 85, "Failed: should be 85"


def test_2():
    assert part_1(["5jshadjh28dajh14"]) == 54, "Failed: should be 54"
