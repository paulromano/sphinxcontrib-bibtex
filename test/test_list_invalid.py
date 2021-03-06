# -*- coding: utf-8 -*-
"""
    test_list_invalid
    ~~~~~~~~~~~~~~~~~

    Test invalid ``:list:`` option.
"""

import nose.tools
from StringIO import StringIO
import os.path
import re

from util import *

srcdir = path(__file__).parent.joinpath('list_invalid').abspath()
warnfile = StringIO()

def teardown_module():
    (srcdir / '_build').rmtree(True)

@with_app(srcdir=srcdir, warning=warnfile)
def test_list_invalid(app):
    app.builder.build_all()
    warnings = warnfile.getvalue()
    assert re.search("unknown bibliography list type 'thisisintentionallyinvalid'", warnings)
