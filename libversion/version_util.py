from importlib.metadata import version, PackageNotFoundError

class VersionUtil:
    """
    A utility class to retrieve the version of the library.
    """

    @staticmethod
    def get_version():
        """
        Retrieves the version of the library. 
        
        Tries to fetch from package metadata (which would include Git tag version).

        Returns:
            str: The version of the library in the format X.X.X or 'unknown' if not found.
        """
        try:
            # Try to get version from package metadata (will reflect Git tag when built)
            return version("libversion")
        except PackageNotFoundError:
            # Fallback to the default version
            return "unknown"
