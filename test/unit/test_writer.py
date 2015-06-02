import os
import glob
import shutil
from nose.tools import (assert_true, assert_equal)
from qidicom import (reader, writer)
from .. import ROOT
from ..helpers.logging import logger


FIXTURE = os.path.join(ROOT, 'fixtures', 'dicom')
"""The test fixture."""

RESULTS = os.path.join(ROOT, 'results', 'dicom')
"""The test results directory."""

TEST_BIRTH_DATE = '20010101'


class TestWriter(object):
    """
    The dicom meta unit tests.
    
    :Note: these tests also indirectly test the writer module.
    """

    def setUp(self):
        shutil.rmtree(RESULTS, True)
        os.makedirs(RESULTS)

    def tearDown(self):
        shutil.rmtree(RESULTS, True)


    def test_writer(self):
        # The destination file name function.
        file_namer = self._target_file_location
        # Change the birth dates.
        for ds in writer.edit(FIXTURE, dest=file_namer):
            ds.PatientsBirthDate = TEST_BIRTH_DATE

        # Verify the result.
        for ds in reader.iter_dicom(RESULTS):
            assert_true(ds.filename.startswith(RESULTS),
                        "Edit result file location incorrect: %s" % ds.filename)
            actual_bd = ds.PatientsBirthDate
            assert_equal(actual_bd, TEST_BIRTH_DATE,
                         "Writer edit result is incorrect: %s" % actual_bd)

    def _target_file_location(self, in_file):
        _, fname = os.path.split(in_file)
        
        return os.path.join(RESULTS, fname)

if __name__ == "__main__":
    import nose
    nose.main(defaultTest=__name__)
