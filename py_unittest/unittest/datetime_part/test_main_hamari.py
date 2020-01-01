
import unittest

import freezegun


class TestTaskGenerator(unittest.TestCase):

    @freezegun.freeze_time('2019-12-29')
    def test_is_sunday(self):
        """today is sunday"""
        from datetime import datetime
        from datetime_part import main_hamari

        task_generator = main_hamari.TaskGenerator()
        tasks = task_generator.is_sunday()
        self.assertTrue(tasks)

    @freezegun.freeze_time('2019-12-24')
    def test_not_is_sunday(self):
        """today is not sunday"""
        from datetime import datetime
        from datetime_part import main_hamari

        task_generator = main_hamari.TaskGenerator()
        tasks = task_generator.is_sunday()
        self.assertFalse(tasks)

