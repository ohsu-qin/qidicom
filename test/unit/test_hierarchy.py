import os
import glob
from nose.tools import (assert_equal, assert_true)
from qidicom import hierarchy
from qiutil.logging import logger
from .. import ROOT

FIXTURE = os.path.join(ROOT, 'fixtures', 'dicom')
"""The test image parent directory."""

SBJ_ID = 'Sarcoma002'
"""The Subject ID."""

STUDY_ID = '1'
"""The test image Study ID."""

STUDY_UID = '1.3.12.2.1107.5.2.32.35139.30000010011316342567100000106'
"""The test image Study UID."""

SERIES_NBR = 11
"""The test image Series Number."""

SERIES_UID = '1.3.12.2.1107.5.2.32.35139.2010011914134225154552501.0.0.0'
"""The test image Series UID."""

INSTANCE_NUMBERS = [6, 7]
"""The test image Instance Numbers."""


class TestHierarchy(object):
    """The dicom hierarchy unit tests."""

    def test_hierarchy(self):
        paths = list(hierarchy.read_hierarchy(FIXTURE))
        assert_equal(len(paths), len(INSTANCE_NUMBERS),
                     "The image hierarchy path count is incorrect: %d" %
                     len(paths))
        for path in paths:
            assert_equal(len(path), 4,
                         "The image hierarchy depth is incorrect: %d" %
                         len(paths))
            sbj_id, study_uid, series_uid, inst_nbr = path
            assert_equal(sbj_id, SBJ_ID, "Subject ID incorrect: %s" % sbj_id)
            assert_equal(study_uid, STUDY_UID,
                         "Study UID incorrect: %s" % study_uid)
            assert_equal(series_uid, SERIES_UID,
                         "Series UID incorrect: %s" % series_uid)
            assert_true(inst_nbr in INSTANCE_NUMBERS,
                        "Instance Number incorrect: %s" % inst_nbr)

    def test_group_by(self):
        groups = hierarchy.group_by('InstanceNumber', FIXTURE)
        assert_equal(len(groups), len(INSTANCE_NUMBERS),
                     "The group count is incorrect: %d" % len(groups))
        assert_equal(set(groups.keys()), set(INSTANCE_NUMBERS),
                     "The group keys are incorrect: %s" % groups.keys())
        for tag, images in groups.iteritems():
            assert_equal(len(images), 1, "The group %d image count is"
                                         " incorrect" % len(images))


if __name__ == "__main__":
    import nose
    nose.main(defaultTest=__name__)
