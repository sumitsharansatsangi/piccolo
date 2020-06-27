import datetime
from unittest import TestCase

from piccolo.table import Table
from piccolo.columns.column_types import Time


class MyTable(Table):
    created_on = Time()


class TestTime(TestCase):
    def setUp(self):
        MyTable.create_table().run_sync()

    def tearDown(self):
        MyTable.alter().drop_table().run_sync()

    def test_timestamp(self):
        created_on = datetime.datetime.now().time()
        row = MyTable(created_on=created_on)
        row.save().run_sync()

        result = MyTable.objects().first().run_sync()
        self.assertEqual(result.created_on, created_on)