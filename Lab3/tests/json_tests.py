import unittest

from tests.data import my_func, my_decorator, for_dec, A, B, C
from sir_Bychko_serializer.json_serializer import json_serializer


class JsonTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.js = json_serializer()

    def test_int(self):
        ser_obj = self.js.dumps(12)
        des_obj = self.js.loads(ser_obj)

        self.assertEqual(des_obj, 12)

    def test_list(self):
        ser_obj = self.js.dumps(["noch", "ulitsa", ("f", 0, "nar apteka"), {"bessmislenny i": "tuskliy svet"} ])
        des_obj = self.js.loads(ser_obj)

        self.assertEqual(des_obj, ["noch", "ulitsa", ("f", 0, "nar apteka"), {"bessmislenny i": "tuskliy svet"} ])

    def test_func(self):
        ser_obj = self.js.dumps(my_func)
        des_obj = self.js.loads(ser_obj)

        self.assertEqual(des_obj("1"), my_func("1"))

    def test_decorator(self):
        answ = my_decorator(for_dec)
        ser_obj = self.js.dumps(my_decorator)
        des_obj = self.js.loads(ser_obj)
        dec = des_obj(for_dec)

        self.assertEqual(answ(), dec())

    def test_lambda(self):
        l = lambda rg: [i for i in range(1, rg)]
        ser_obj = self.js.dumps(l)
        des_ob = self.js.loads(ser_obj)

        self.assertEqual(l(3),des_ob(3))

    def test_static_method(self):
        ser_obj = self.js.dumps(A)
        des_obj = self.js.loads(ser_obj)

        self.assertEqual(des_obj.ret_jivi(), A.ret_jivi())

    def test_decorated_static_method(self):
        obj = B()
        ser_obj = self.js.dumps(obj)
        des_obj = self.js.loads(ser_obj)

        self.assertEqual(obj.another_method(5), des_obj.another_method(5))

    def test_method(self):
        obj = C()
        ser_obj = self.js.dumps(obj)
        des_obj = self.js.loads(ser_obj)

        self.assertEqual(obj.sus(12), des_obj.sus(12))

    def test_init(self):
        obj = C()
        ser_obj = self.js.dumps(obj)
        des_obj = self.js.loads(ser_obj)

        self.assertEqual(obj.chetvert, des_obj.chetvert)


if __name__ == "__main__":
    unittest.main()
