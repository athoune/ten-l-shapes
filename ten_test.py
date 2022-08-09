from ten import L


def test_start_5():
    l = L(10)
    l.start(5)
    assert l.size == 0


def test_len_2():
    l = L(2)
    l.start(0)
    assert l.size == 2

def test_len_3():
    l = L(3)
    l.start(0)
    assert l.size == 6, "second jumps are both tall"
