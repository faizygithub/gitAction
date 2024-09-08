from src.math_op import add,sub 

def add_test():
    assert add(3, 5) == 8
    assert add(-1, 2) == 1
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0
    assert add(1000000, 2000000) == 3000000
    print("All add tests passed")


def sub_test():
    assert sub(5, 3) == 2
    assert sub(-1, 2) == -3
    assert sub(0, 0) == 0
    assert sub(2.5, 1.5) == 1.0
    assert sub(2000000, 1000000) == 1000000
    print("All sub tests passed")