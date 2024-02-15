import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from record_manager import RecordManager
import unittest.mock as mock

TEST_FILE_PATHS = "../tests/test_file.txt"


@mock.patch("record_manager.RecordManager.get_file_path", return_value=TEST_FILE_PATHS)
class TestRecordManager:
    def setup_method(self):
        self.record_manager = RecordManager()

    def test_record_manager_creates_file(self, _):
        self.record_manager.add_record(_, 1)
        assert os.path.exists(TEST_FILE_PATHS)

    def test_adds_record(self, _):
        self.record_manager.add_record(_, 2)
        with open(TEST_FILE_PATHS, "r") as file:
            assert file.read() == "1\n2\n"

    def test_records_sorted(self, _):
        self.record_manager.add_record(_, 4)
        self.record_manager.add_record(_, 3)
        self.record_manager.add_record(_, 6)
        self.record_manager.add_record(_, 3)
        with open(TEST_FILE_PATHS, "r") as file:
            assert file.read() == "1\n2\n3\n3\n4\n6\n"

    def test_last_record_deleted(self, _):
        self.record_manager.add_record(_, 7)
        self.record_manager.add_record(_, 9)
        self.record_manager.add_record(_, 8)
        self.record_manager.add_record(_, 11)
        self.record_manager.add_record(_, 10)
        with open(TEST_FILE_PATHS, "r") as file:
            assert file.read() == "1\n2\n3\n3\n4\n6\n7\n8\n9\n10\n"

    def test_number_of_records(self, _):
        records = self.record_manager.get_records(_)
        assert len(records) == 10
        os.remove(TEST_FILE_PATHS)
