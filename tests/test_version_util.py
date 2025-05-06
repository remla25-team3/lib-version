from libversion.version_util import VersionUtil
import os
import re

def test_get_version_format():
    version_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'VERSION'))
    print("DEBUG - Expected VERSION path:", version_path)
    print("DEBUG - VERSION file exists?", os.path.exists(version_path))

    version = VersionUtil.get_version()
    assert re.match(r'^\d+\.\d+\.\d+$', version), f"Version '{version}' does not match the format 'X.X.X'"
