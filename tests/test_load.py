"""
Test dumping and loading some objects
"""

# stdlib
import pathlib
from tempfile import TemporaryDirectory

# 3rd party
import pytest

# this package
import sdjson


def write_then_read(obj):
	with TemporaryDirectory() as tmpdir:
		tmpfile = pathlib.Path(tmpdir) / "output.json"

		with open(tmpfile, 'w') as fp:
			sdjson.dump(obj, fp)

		with open(tmpfile) as fp:
			return sdjson.load(fp)


def test_bools() -> None:
	assert write_then_read(True) is True
	assert str(write_then_read(True)) == "True"  # Double check with string

	assert write_then_read(False) is False
	assert str(write_then_read(False)) == "False"  # Double check with string


def test_none() -> None:
	assert write_then_read(None) is None
	assert str(write_then_read(None)) == "None"  # Double check with string


def test_int() -> None:
	assert write_then_read(1) == 1
	assert write_then_read(1234) == 1234
	assert write_then_read(12340000000) == 12340000000
	assert write_then_read(-1) == -1
	assert write_then_read(-1234) == -1234
	assert write_then_read(-12340000000) == -12340000000


def test_float() -> None:
	assert write_then_read(1.0) == 1.0
	assert write_then_read(1234.0) == 1234.0
	assert write_then_read(12340000000.0) == 12340000000.0
	assert write_then_read(-1.0) == -1.0
	assert write_then_read(-1234.0) == -1234.0
	assert write_then_read(-12340000000.0) == -12340000000.0

	assert write_then_read(1.005) == 1.005
	assert write_then_read(1234.005) == 1234.005
	assert write_then_read(12340000000.005) == 12340000000.005
	assert write_then_read(-1.005) == -1.005
	assert write_then_read(-1234.005) == -1234.005
	assert write_then_read(-12340000000.005) == -12340000000.005


def test_string() -> None:
	for string in ["egg and bacon", "egg sausage and bacon", "egg and spam", "egg bacon and spam"]:
		print(string)
		assert write_then_read(string) == string


@pytest.mark.xfail
def test_dict_failure() -> None:
	"""
	This test will fail because the boolean dictionary keys get read back in a lowercase strings
	"""

	assert write_then_read({True: False, False: True}) == {True: False, False: True}
	assert write_then_read({2: 3.0, 4.0: 5, False: 1, 6: True}) == {2: 3.0, 4.0: 5, False: 1, 6: True}


def test_dict() -> None:
	data = {"True": True, "False": False, "String": "spam", "Integer": 1, "Float": 2.5}
	assert write_then_read(data) == data


def test_list() -> None:
	data = [True, False, 1, 2.5, "spam"]
	assert write_then_read(data) == data


@pytest.mark.xfail
def test_tuple_failure() -> None:
	"""
	This test will fail because the tuple gets loaded back in as a list
	"""

	assert write_then_read((True, False, 1, 2.5, "spam")) == (True, False, 1, 2.5, "spam")


def test_tuple_success() -> None:
	assert write_then_read((True, False, 1, 2.5, "spam")) == [True, False, 1, 2.5, "spam"]
