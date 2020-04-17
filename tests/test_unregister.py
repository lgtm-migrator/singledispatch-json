# stdlib
from decimal import Decimal

# 3rd party
import pytest

# this package
import sdjson


def test_unregister():
	# Create and register a custom encoder for Decimal that turns it into a string
	@sdjson.encoders.register(Decimal)
	def encode_str(obj):
		return str(obj)
	
	# Test that we get the expected output from the first encoder
	assert sdjson.dumps(Decimal(1)) == '"1"'
	
	# Unregister that encoder
	sdjson.unregister_encoder(Decimal)
	
	# We should now get an error
	with pytest.raises(TypeError) as e:
		sdjson.dumps(Decimal(2))
	assert e.type is TypeError
	assert str(e.value) == 'Object of type Decimal is not JSON serializable'

