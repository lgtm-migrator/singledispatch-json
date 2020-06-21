# stdlib
from collections import OrderedDict

# this package
import sdjson


def test_ordered_dict() -> None:
	# See issue 6105
	items = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5)]
	s = sdjson.dumps(OrderedDict(items))
	assert s == '{"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}'


def test_sorted_dict() -> None:
	items = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5)]
	s = sdjson.dumps(dict(items), sort_keys=True)
	assert s == '{"five": 5, "four": 4, "one": 1, "three": 3, "two": 2}'
