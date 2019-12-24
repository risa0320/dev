
from datetime import datetime


class TaskGenerator(object):

    def generate_tasks(self, work_datetime):
        if self.is_sunday(work_datetime):
            return False
        return ['Meeting', 'development']

    def is_sunday(self):
        week_day = datetime.now().weekday()
        return week_day == 6


def main():
    tasks = TaskGenerator().generate_tasks()
    print(tasls)

if __name__ == '__main__':
    main()
