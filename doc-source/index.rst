****************
sdjson
****************


.. start short_desc

**Custom JSON Encoder for Python utilising functools.singledispatch to support custom encoders for both Python's built-in classes and user-created classes, without as much legwork.**

.. end short_desc

Based on https://treyhunner.com/2013/09/singledispatch-json-serializer/ and Python's ``json`` module.

.. start shields 

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs|
	* - Tests
	  - |travis| |requires| |coveralls| |codefactor|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Anaconda
	  - |conda-version| |conda-platform|
	* - Other
	  - |license| |language| |commits-since| |commits-latest| |maintained| 

.. |docs| image:: https://readthedocs.org/projects/singledispatch-json/badge/?version=latest
	:target: https://singledispatch-json.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status

.. |travis| image:: https://img.shields.io/travis/com/domdfcoding/singledispatch-json/master?logo=travis
	:target: https://travis-ci.com/domdfcoding/singledispatch-json
	:alt: Travis Build Status

.. |requires| image:: https://requires.io/github/domdfcoding/singledispatch-json/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/singledispatch-json/requirements/?branch=master
	:alt: Requirements Status

.. |coveralls| image:: https://coveralls.io/repos/github/domdfcoding/singledispatch-json/badge.svg?branch=master
	:target: https://coveralls.io/github/domdfcoding/singledispatch-json?branch=master
	:alt: Coverage

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/singledispatch-json
	:target: https://www.codefactor.io/repository/github/domdfcoding/singledispatch-json
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/sdjson.svg
	:target: https://pypi.org/project/sdjson/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/sdjson.svg
	:target: https://pypi.org/project/sdjson/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/sdjson
	:target: https://pypi.org/project/sdjson/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/sdjson
	:target: https://pypi.org/project/sdjson/
	:alt: PyPI - Wheel

.. |conda-version| image:: https://img.shields.io/conda/v/domdfcoding/sdjson
	:alt: Conda - Package Version
	:target: https://anaconda.org/domdfcoding/sdjson

.. |conda-platform| image:: https://img.shields.io/conda/pn/domdfcoding/sdjson?label=conda%7Cplatform
	:alt: Conda - Platform
	:target: https://anaconda.org/domdfcoding/sdjson

.. |license| image:: https://img.shields.io/github/license/domdfcoding/singledispatch-json
	:alt: License
	:target: https://github.com/domdfcoding/singledispatch-json/blob/master/LICENSE

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/singledispatch-json
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/singledispatch-json/v0.2.5
	:target: https://github.com/domdfcoding/singledispatch-json/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/singledispatch-json
	:target: https://github.com/domdfcoding/singledispatch-json/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2020
	:alt: Maintenance

.. end shields



|

Installation
-------------

.. start installation

.. tabs::

	.. tab:: from PyPI

		.. prompt:: bash

			pip install sdjson

	.. tab:: from Anaconda

		First add the required channels

		.. prompt:: bash

			conda config --add channels http://conda.anaconda.org/domdfcoding
			conda config --add channels http://conda.anaconda.org/conda-forge

		Then install

		.. prompt:: bash

			conda install sdjson

	.. tab:: from GitHub

		.. prompt:: bash

			pip install git+https://github.com//singledispatch-json@master

.. end installation


.. toctree::
	:hidden:

	Home<self>

.. toctree::
	:maxdepth: 3
	:caption: Documentation

	API Reference<docs>
	Source
	Building


.. start links

View the :ref:`Function Index <genindex>` or browse the `Source Code <_modules/index.html>`__.

`Browse the GitHub Repository <https://github.com/domdfcoding/singledispatch-json>`__

.. end links
