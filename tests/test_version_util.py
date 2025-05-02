from libversion.version_util import VersionUtil
import os
import re

def test_get_version_format():
    version_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'VERSION'))
    print("DEBUG - Expected VERSION path:", version_path)
    print("DEBUG - VERSION file exists?", os.path.exists(version_path))

    version = VersionUtil.get_version()
    
    # Accepts semantic versioning (e.g., 1.2.3 or 0.1.0), or 'a1', 'a2' for assignment tags
    valid = bool(re.match(r'^(a[0-9]+|[0-9]+\.[0-9]+\.[0-9]+)$', version))
    assert valid, f"Invalid version format: {version}"
