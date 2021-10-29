import unittest
from app import main, my_good_fun, home_work


class TestClass(unittest.TestCase):
    def setUp(self):
        # Дана функція налаштовує початкові агрументи визначені лише для класу
        self.date_url = 'http://date.jsontest.com/'
        self.ip_url = 'http://ip.jsontest.com/'

    def test_date_work_successfully(self):
        # Перевіряємо чи функція відпрацювала до кінця і повернула True
        self.assertTrue(main(self.date_url))

    def test_empty_url(self):
        # Перевіряємо чи у функцію не було передано жодної URL
        self.assertFalse(main())

    def test_no_date_in_response(self):
        # Перевіряємо що у відповіді відсутнє поле дата (тобто передана неправильна URL)
        with self.assertRaises(Exception):
            main(self.ip_url)

    def test_home_work(self):
        self.assertEqual(home_work("07:03 PM"), "Доброї ночі!")
        self.assertEqual(home_work("07:30 AM"), "Доброго дня!")

    def test_my_fun(self):
        self.assertEqual(my_good_fun(), "success")
