import unittest
from mypage import MyPage
import time


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.pg = MyPage()
        cls.pg.start_session()

    @classmethod
    def tearDownClass(cls):
        cls.pg.stop_session()

    def tearDown(self):
        if hasattr(self._outcome, 'failures'):
            result = self.defaultTestResult()
            self._feedErrorsToResult(result, self._outcome.failures)
        else:
            result = self._outcome.result

        if result.failures or result.errors:
            self.pg.get_screenshot()

    def test_1(self):
        res = self.pg.open_list()
        self.assertEqual(res, 3)

    def test_2(self):
        res = self.pg.go_to_table()
        self.assertEqual(res, "Расписания")
        self.pg.checking_schedule()

    def test_3(self):
        WEEKDAYS = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        res = self.pg.check_color()
        now = time.localtime()
        weekday_index = now.tm_wday
        self.assertEqual(res, WEEKDAYS[weekday_index])


if __name__ == '__main__':
    unittest.main(warnings='ignore', failfast=True)
