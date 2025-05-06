from importlib.metadata import version, PackageNotFoundError

class VersionUtil:
    """
    A utility class to retrieve the version of the library.
    """

    @staticmethod
    def get_version():
        """
        Retrieves the version of the library from package metadata.

        Returns:
            str: The version of the library.
        """
        try:
            # Dynamically fetch the version from package metadata
            return version("libversion")
        except PackageNotFoundError:
            # Fallback if the package metadata is not found
            return "unknown"
