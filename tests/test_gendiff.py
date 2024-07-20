from difference_calculator.scripts import gendiff

import pytest                                                                                                               


@pytest.fixture
def json_files():
    return 'json_files_dir/file1.json', 'json_files_dir/file2.json', 'json_files_dir/right_answer.txt'


def test_gendiff(json_files):
    path_file1, path_file2, path_right_file = json_files
    with open(path_right_file) as file:
        result = file.read().strip()
    assert gendiff.generate_diff(path_file1, path_file2) == result 
