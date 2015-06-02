import os
import glob
import shutil
from nose.tools import (assert_equal, assert_true)
from qidicom import (reader, writer, meta)
from .. import ROOT
from ..helpers.logging import logger

FIXTURE = os.path.join(ROOT, 'fixtures', 'dicom')
"""The test fixture."""

RESULTS = os.path.join(ROOT, 'results', 'dicom')
"""The test results directory."""


class TestMeta(object):
    """
    The dicom meta unit tests.
    
    :Note: these tests also indirectly test the writer module.
    """

    def setUp(self):
        shutil.rmtree(RESULTS, True)

    def tearDown(self):
        shutil.rmtree(RESULTS, True)

    def test_editor(self):
        # A trivial edit function.
        bd_func = lambda bd: '20000101'
        # The tag name => value edit dictionary.
        edits = dict(PatientID='Test Patient', BodyPartExamined='HIP',
                     PatientsBirthDate=bd_func)
        # Make the editor.
        editor = meta.Editor(**edits)
        # An array to collect the input files.
        in_files = []
        # Edit the headers.
        for ds in writer.edit(FIXTURE, dest=RESULTS):
            editor.edit(ds)
            in_files.append(ds.filename)

        # Verify the result.
        targets = set((self._target_file_location(f) for f in in_files))
        results = set((ds.filename for ds in reader.iter_dicom(*targets)))
        assert_equal(targets, results, "Result files are incorrect: %s" %
                                       results)
        for ds in reader.iter_dicom(*targets):
            for tag in ['PatientID', 'BodyPartExamined']:
                expected = edits[tag]
                actual = getattr(ds, tag)
                assert_equal(actual, expected, "Edited DICOM tag %s incorrect:"
                                               " %s" % (tag, actual))
            expected_bd = bd_func(None)
            actual_bd = ds.PatientsBirthDate
            assert_equal(actual_bd, expected_bd,
                         "Edited DICOM tag %s incorrect: %s" %
                         ('PatientsBirthDate', actual))


    def _target_file_location(self, in_file):
        _, fname = os.path.split(in_file)
        
        return os.path.join(RESULTS, fname)

if __name__ == "__main__":
    import nose
    nose.main(defaultTest=__name__)
