
from datetime import datetime


class TaskGenerator(object):

    def generate_tasks(self, work_datetime):
        if self.is_sunday(work_datetime):
            return False
        return ['Meeting', 'development']

    def is_sunday(self, work_datetime):
        week_day = work_datetime.weekday()
        return week_day == 6


def main():
    today = datetime.now()
    tasks = TaskGenerator().generate_tasks(today)
    print(tasks)

if __name__ == '__main__':
    main()
