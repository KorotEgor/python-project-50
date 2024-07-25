from gendiff.scripts import gendiff

import pytest                                                                                                               

_TESTS = (
	('test_files/file1.json', 'test_files/file2.json', 'test_files/right_standart_file1_file2.txt', 'stylish'),
	('test_files/file1.yml', 'test_files/file2.yml', 'test_files/right_standart_file1_file2.txt', 'stylish'),
    ('test_files/comp1.yaml', 'test_files/comp2.yaml', 'test_files/right_standart_comp1_comp2.txt', 'stylish'),
    ('test_files/comp1.json', 'test_files/comp2.json', 'test_files/right_standart_comp1_comp2.txt', 'stylish'),
    ('test_files/comp1.json', 'test_files/comp2.json', 'test_files/right_plain_comp1_comp2.txt', 'plain'),
    ('test_files/comp1.yaml', 'test_files/comp2.yaml', 'test_files/right_plain_comp1_comp2.txt', 'plain'),
)


@pytest.mark.parametrize('path_file1,path_file2,path_right_file,style', _TESTS)
def test_gendiff(path_file1, path_file2, path_right_file, style):
    with open(path_right_file) as file:
        result = file.read().strip()
    assert gendiff.generate_diff(path_file1, path_file2, style) == result 
