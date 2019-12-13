
import unittest


class TestTaskGenerator(unittest.TestCase):

    def setUp(cls):
        from datetime_part import main
        cls.task_generator = main.TaskGenerator()

    def tearDown(cls):
        pass

    def test_is_sunday(self):
        """today is sunday"""
        from datetime import datetime
        sunday_datetime = datetime.strptime(
            '2019/12/15 12:00:00', '%Y/%m/%d %H:%M:%S')
        tasks = self.task_generator.is_sunday(sunday_datetime)
        self.assertTrue(tasks)

    def test_not_is_sunday(self):
        """today is not sunday"""
        from datetime import datetime
        sunday_datetime = datetime.strptime(
            '2019/12/13 12:00:00', '%Y/%m/%d %H:%M:%S')
        tasks = self.task_generator.is_sunday(sunday_datetime)
        self.assertFalse(tasks)

