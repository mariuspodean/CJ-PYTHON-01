import unittest

from lesson_14.mihai_farcas import homework_polygons


def test_triangle():
    s1, s2, s3 = 3, 4, 5

    test_triangle = Triangle(s1, s2, s3)

    assert hasattr(test_triangle, 's1'), "dd"
    assert hasattr(test_triangle, s2), "doi"
    assert hasattr(test_triangle, s3), "trei"


test_triangle()
