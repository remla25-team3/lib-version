# lib-version

`lib-version` is a version-aware library that can can be asked for the version of the library. This can be useful, for
example, for verbose system information in log messages or data record.

---

## Features

- Exposes the current version using a reusable `VersionUtil` class
- Stores version metadata in a dedicated `VERSION` file
- Automatically sets the version based on the Git tag during release
- Released via GitHub Actions workflow as a Python package artifact
- Can be reused in other repositories via Git URL and tag

---

## How it works

- The current version (e.g., `v1.0.0`) is injected into a `VERSION` file automatically by the GitHub workflow when a tag is pushed.
- The `VersionUtil` class reads the `VERSION` file at runtime.
- This enables services to report or log the exact version they were built from.

---

## Example usage

In another repository (e.g., `model-service`), add this to `requirements.txt`:

    git+https://github.com/remla25-team3/lib-version.git

Then use it in your code (Python):

```python
from libversion.version_util import VersionUtil

print("Running version:", VersionUtil.get_version())
