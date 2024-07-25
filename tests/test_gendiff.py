from gendiff.scripts import gendiff

import pytest

_TESTS = (
    (
        "tests/fixtures/file1.json",
        "tests/fixtures/file2.json",
        "tests/fixtures/right_standart_file1_file2.txt",
        "stylish",
    ),
    (
        "tests/fixtures/file1.yml",
        "tests/fixtures/file2.yml",
        "tests/fixtures/right_standart_file1_file2.txt",
        "stylish",
    ),
    (
        "tests/fixtures/comp1.yaml",
        "tests/fixtures/comp2.yaml",
        "tests/fixtures/right_standart_comp1_comp2.txt",
        "stylish",
    ),
    (
        "tests/fixtures/comp1.json",
        "tests/fixtures/comp2.json",
        "tests/fixtures/right_standart_comp1_comp2.txt",
        "stylish",
    ),
    (
        "tests/fixtures/comp1.json",
        "tests/fixtures/comp2.json",
        "tests/fixtures/right_plain_comp1_comp2.txt",
        "plain",
    ),
    (
        "tests/fixtures/comp1.yaml",
        "tests/fixtures/comp2.yaml",
        "tests/fixtures/right_plain_comp1_comp2.txt",
        "plain",
    ),
)


@pytest.mark.parametrize("path_file1,path_file2,path_right_file,style", _TESTS)
def test_gendiff(path_file1, path_file2, path_right_file, style):
    with open(path_right_file) as file:
        result = file.read().strip()
    assert gendiff.generate_diff(path_file1, path_file2, style) == result
