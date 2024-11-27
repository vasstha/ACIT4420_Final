import os
import pytest
from sorter import organize_files

@pytest.fixture
def setup_test_directory(tmp_path):
    files = ["test.txt", "image.jpg", "music.mp3", "code.py"]
    for file in files:
        (tmp_path / file).write_text("dummy content")
    return tmp_path

def test_organize_files(setup_test_directory):
    organize_files(setup_test_directory)
    assert (setup_test_directory / "Documents").exists()
    assert (setup_test_directory / "Images").exists()
    assert (setup_test_directory / "Audio").exists()
    assert (setup_test_directory / "Code").exists()
