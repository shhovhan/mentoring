class Circle:

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        print('Getting radius attribute')
        return self._radius

    @radius.setter
    def radius(self, radius):
        print('Setting radius attribute')
        self._radius = radius

    @radius.deleter
    def radius(self):
        print('Deleting radius attribute')
        del self._radius

    @property
    def diameter(self):
        return 2 * self._radius

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter/2


class A:

    def a(self):
        pass

class B(A)
    def a1(self):
        return 1

    def a2(self):
        return 2

class C(A):
    def a1(self):
        return 2

    def a2(self):
        return 1

class D(B, C):
    pass



d = D()

d.a1()
d.a2()


L(D) = [D] + merge(L(B), L(C), [B,C])

L(B) = [B] + merge(L(A), [A]) = [B] + merge([A, O], [A]) = [B] + [A] + merge([O], []) = [B] + [A] + [O] = [B, A, O]
L(C) = [C] + merge(L(A), [A]) = [C, A, O]

L(A) = [A] + merge(L(O), [O]) = [A] + [O] = [A,O]

L(D) = [D] + merge([B, A, O], [C, A, O], [B, C]) = [D] + [B] + merge([A, O], [C, A, O], [C]) = [D, B] + merge([O], [C, O], [C], [A]) =
[D, B] + merge([C], [C, A, O]) = [D, B] + C + [A, O]

