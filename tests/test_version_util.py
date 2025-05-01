from libversion.version_util import VersionUtil
import os

def test_get_version_format():
    version_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'VERSION'))
    print("DEBUG - Expected VERSION path:", version_path)
    print("DEBUG - VERSION file exists?", os.path.exists(version_path))

    version = VersionUtil.get_version()
    assert version.count('.') == 2
