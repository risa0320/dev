
import os 

import dataset


class MySQLOperator(object):

    def __init__(self):
        self.db = dataset.connect('mysql://root:{0}@mysql/unittest'.format(
            os.environ['MYSQL_ROOT_PASSWORD']))


class DataFetcher(MySQLOperator):

    def __init__(self):
        MySQLOperator.__init__(self)
        self.test_table = self.db['test_1']

    def count_data(self, **kwargs):
        return self.test_table.count(**kwargs)

    def start(self):
        invalid_data_count = self.count_data(invalid=1)
        if not invalid_data_count:
            return False
        return True


if __name__ == '__main__':
    fetcher = DataFetcher()
    fetcher.start()
