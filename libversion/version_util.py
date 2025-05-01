import os

class VersionUtil:

    @staticmethod
    def get_version():
        """
        Expose version information
        """

        # Construct the relative path to the VERSION file
        current_dir = os.path.dirname(__file__)
        version_path = os.path.join(current_dir, '..', '..', 'VERSION')

        #Open the file, read its contents (remove whitespace)
        with open(version_path, 'r') as f:
            return f.read().strip()
