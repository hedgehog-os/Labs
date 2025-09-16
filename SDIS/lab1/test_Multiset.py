import pytest
from Multiset import Multiset

def test_atomic_elements():
    m = Multiset('{a, b, a}')
    assert m.cardinality() == 3
    assert m.multiset == {'a': 2, 'b': 1}
    assert 'a' in m
    assert 'b' in m
    assert 'c' not in m

def test_nested_multisets():
    m = Multiset('{a, {b, b}, a}')
    nested = Multiset('{b, b}')
    assert m.cardinality() == 3
    assert m.multiset == {'a': 2, nested: 1}
    assert nested in m
    assert 'a' in m
    assert Multiset('{b}') not in m

def test_empty_multiset():
    m = Multiset('{}')
    assert m.is_empty()
    assert m.cardinality() == 0
    assert repr(m) == "Multiset({})"

def test_delete_and_ndelete():
    m = Multiset('{x, x, y}')
    m.ndelete('x', 1)
    assert m.multiset == {'x': 1, 'y': 1}
    m.ndelete('x', 1)
    assert 'x' not in m
    m.delete('y')
    assert m.is_empty()

def test_union_and_addition():
    m1 = Multiset('{a, b}')
    m2 = Multiset('{b, c}')
    union = m1 & m2
    expected = Multiset('{a, b, b, c}')
    assert union == expected
    m1 += m2
    assert m1 == expected

def test_subtraction():
    m1 = Multiset('{a, b, b}')
    m2 = Multiset('{b}')
    result = m1 - m2
    expected = Multiset('{a, b}')
    assert result == expected
    m1 -= m2
    assert m1 == expected

def test_intersection():
    m1 = Multiset('{a, b, b}')
    m2 = Multiset('{b, b, c}')
    inter = m1 * m2
    expected = Multiset('{b, b}')
    assert inter == expected
    m1 *= m2
    assert m1 == expected

def test_bolean():
    m = Multiset('{x, x}')
    bolean = m.bolean()
    expected = [
        Multiset('{}'),
        Multiset('{x}'),
        Multiset('{x, x}')
    ]
    for subset in expected:
        assert subset in bolean
    assert len(bolean) == 3
    assert all(isinstance(sub, Multiset) for sub in bolean)

def test_repr_and_eq_and_hash():
    m1 = Multiset('{a, b}')
    m2 = Multiset('{a, b}')
    assert repr(m1) == repr(m2)
    assert m1 == m2
    assert hash(m1) == hash(m2)
    assert m1 != Multiset('{a, b, b}')

def test_empty_nested_multiset():
    m = Multiset('{{}}')
    inner = Multiset('{}')
    assert m.cardinality() == 1
    assert inner in m
    assert not m.is_empty()

def test_mixed_nested_and_atomic():
    m = Multiset('{a, {b}, a, {}}')
    assert m.cardinality() == 4
    assert 'a' in m
    assert Multiset('{b}') in m
    assert Multiset('{}') in m

def test_redundant_nesting():
    m = Multiset('{{a}}')
    inner = Multiset('{a}')
    assert inner in m
    assert m.cardinality() == 1
    assert 'a' not in m

def test_multiple_empty_sets():
    m = Multiset('{{}, {}, {}}')
    empty = Multiset('{}')
    assert m.cardinality() == 3
    assert m.multiset[empty] == 3
    assert not m.is_empty()

def test_whitespace_and_commas():
    m = Multiset('{  a ,   b , {  c ,  } , }')
    assert 'a' in m
    assert 'b' in m
    assert Multiset('{c}') in m
    assert m.cardinality() == 3

def test_invalid_but_tolerated_structure():
    m = Multiset('{a, {b, {}}}')
    assert 'a' in m
    assert Multiset('{b, {}}') in m
    assert m.cardinality() == 2

def test_hash_and_repr():
    ms = Multiset('{a, b, a}')
    assert isinstance(hash(ms), int)
    assert repr(ms) == f"Multiset({ms.multiset})"

def test_contains_and_eq():
    ms1 = Multiset('{x, y}')
    ms2 = Multiset('{x, y}')
    assert 'x' in ms1
    assert ms1 == ms2

def test_iadd_isub_imul():
    ms1 = Multiset('{a, b, b}')
    ms2 = Multiset('{b, b, c}')
    ms1 += ms2
    assert ms1.cardinality() == 6
    ms1 -= Multiset('{b, b}')
    assert ms1.multiset['b'] == 2
    ms1 *= Multiset('{b, b, b}')
    assert ms1.multiset['b'] == 2

def test_delete_ndelete():
    ms = Multiset('{a, a, b}')
    ms.ndelete('a', 1)
    assert ms.multiset['a'] == 1
    ms.delete('a')
    assert 'a' not in ms.multiset

def test_is_empty_and_bolean():
    ms = Multiset('{}')
    assert ms.is_empty()
    ms2 = Multiset('{x, x}')
    subsets = ms2.bolean()
    assert any(isinstance(sub, Multiset) for sub in subsets)
