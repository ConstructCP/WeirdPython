"""
   A
  / \
B    C
|   / \
D   E F
|  /\/\
G H I J
\ | | /
   X
"""

class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B):
    pass
class E(C):
    pass
class F(C):
    pass
class G(D):
    pass
class H(E):
    pass
class I(E, F):
    pass
class J(F):
    pass
class X(G, H, I, J):
    pass
class Y(X):
    pass


def mro(obj):
    obj_cls = obj.__class__
    parents = {}
    to_trace_parents = list(obj_cls.__bases__)
    while to_trace_parents:
        cls = to_trace_parents.pop(0)
        parents[cls] = cls.__bases__
        for base_cls in cls.__bases__:
            if base_cls is object:
                continue
            if base_cls not in parents and base_cls not in to_trace_parents:
                to_trace_parents.append(base_cls)

    def get_base_class(c):
        if c is object:
            return []
        bases = []
        for base in c.__bases__:
            bases.append(base)
            bases.extend(get_base_class(base))
        return bases

    chain = [obj_cls]
    for base_cls in obj_cls.__bases__:
        base_cls_chain = get_base_class(base_cls)
        chain.extend([base_cls] + base_cls_chain)

    mro = []
    for el in reversed(chain):
        if el not in mro:
            mro.insert(0, el)
    return mro


# x = X()
# print(' '.join(c.__name__ for c in x.__class__.__mro__))
# x_mro = mro(x)
# print(' '.join(c.__name__ for c in x_mro))

y = Y()
print(' '.join(c.__name__ for c in y.__class__.__mro__))
y_mro = mro(y)
print(' '.join(c.__name__ for c in y_mro))
