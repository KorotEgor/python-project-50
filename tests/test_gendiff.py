from difference_calculator.scripts import gendiff

import pytest                                                                                                               

_TESTS = (
	('test_files/file1.json', 'test_files/file2.json', 'test_files/right_file1_file2.txt'),
	('test_files/file1.yml', 'test_files/file2.yml', 'test_files/right_file1_file2.txt'),
)


@pytest.mark.parametrize('path_file1,path_file2,path_right_file', _TESTS)
def test_gendiff(path_file1, path_file2, path_right_file):
    with open(path_right_file) as file:
        result = file.read().strip()
    assert gendiff.generate_diff(path_file1, path_file2) == result 
