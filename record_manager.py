import os
from difficulty import Difficulty

# Path: record_manager.py
class RecordManager:
    def __init__(self) -> None:
        self.FOLDER = "records"
        self.HARD_FILE = "hard.txt"
        self.MEDIUM_FILE = "medium.txt"
        self.EASY_FILE = "easy.txt"

    def add_record(self, difficulty: Difficulty, time: int):
        file_path = self.get_file_path(difficulty)
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                file.write(time + '\n')
                return

        self.update_records(time, file_path)

    def get_file_path(self, difficulty: Difficulty) -> str:
        match difficulty:
            case Difficulty.EASY:
                return os.path.join(self.FOLDER, self.EASY_FILE)
            case Difficulty.MEDIUM:
                return os.path.join(self.FOLDER, self.MEDIUM_FILE)
            case Difficulty.HARD:
                return os.path.join(self.FOLDER, self.HARD_FILE)

    def update_records(self, time : int, file_path : str):
        with open(file_path, 'r+') as file:
            records = file.readlines()
            file.truncate(0)
            records.append(str(time) + '\n')
            records.sort()
            records.pop()
            file.writelines(records)

    def get_records(self, difficulty : Difficulty):
        file_path = self.get_file_path(difficulty)
        if not os.path.exists(file_path):
            return None

        with open(file_path, "r") as file:
            records = file.readlines()
            return records
