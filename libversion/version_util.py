import os

class VersionUtil:

    @staticmethod
    def get_version():
        """
        Reads and returns the version string from the VERSION file.
        
        Returns:
            str: The version (e.g., a1) read from the VERSION file.
        """

        # Construct the relative path to the VERSION file
        current_dir = os.path.dirname(__file__)
        version_path = os.path.join(current_dir, '..', 'VERSION')
        #Open the file, read its contents (remove whitespace)
        with open(version_path, 'r') as f:
            return f.read().strip()
