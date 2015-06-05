.. _index:

========================================
qidicom - Quantitative Imaging Utilities
========================================

********
Synopsis
********
qidicom provides a facade for DICOM file interaction.

:API: http://qidicom.readthedocs.org/en/latest/api/index.html

:Git: github.com/ohsu-qin/qidicom


************
Feature List
************
1. Python logging configuration.

2. Common command utility functions.

3. Collection data structures and utilities. 

4. File helper functions.


************
Installation
************
Install the ``qidicom`` package with Python_ pip_::

    pip install qidicom


*****
Usage
*****
Run the following command for the utility options::

    lsdicom --help


***********
Development
***********

Testing is performed with the nose_ package, which must be installed separately.

Documentation is built automatically by ReadTheDocs_ when the project is pushed
to GitHub. Documentation can be generated locally as follows:

* Install Sphinx_, if necessary.

* Run the following in the ``doc`` subdirectory::

    make html

---------

.. container:: copyright


.. Targets:

.. _Knight Cancer Institute: http://www.ohsu.edu/xd/health/services/cancer

.. _license: https://github.com/ohsu-qin/qidicom/blob/master/LICENSE.txt

.. _nose: https://nose.readthedocs.org/en/latest/

.. _pip: https://pypi.python.org/pypi/pip

.. _Python: http://www.python.org

.. _ReadTheDocs: https://www.readthedocs.org

.. _Sphinx: http://sphinx-doc.org/index.html

.. toctree::
  :hidden:

  api/index

