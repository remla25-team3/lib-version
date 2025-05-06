from libversion.version_util import VersionUtil
import re

def test_get_version_format():
    version = VersionUtil.get_version()
    assert re.match(r'^\d+\.\d+\.\d+$', version), f"Version '{version}' does not match the format 'X.X.X'"
