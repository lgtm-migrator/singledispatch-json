# this package
import sdjson


def test_default() -> None:
	assert sdjson.dumps(type, default=repr) == sdjson.dumps(repr(type))
