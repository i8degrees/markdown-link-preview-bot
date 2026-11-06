# src/util/version.py:jeff
#

import subprocess

def project_name() -> str:
    """Returns the official name string from the repo's .name"""
    with open(".name", "r", encoding="utf-8") as f:
        name = f.read().strip()
        return name


def project_version() -> str:
    """Returns the official version string from the repo's .version"""
    with open(".version", "r", encoding="utf-8") as f:
        version = f.read().strip()
        return version


def git_revision_hash() -> str:
    """Returns the full git revision hash of the current directory."""
    try:
        # Run the git command to get the output
        commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD'], stderr=subprocess.DEVNULL).decode('utf-8').strip()
        return commit_hash
    except subprocess.CalledProcessError:
        # Handle cases where git is not installed or not in a git repo
        return "Unknown"


def git_revision_short_hash() -> str:
    """Returns the short git revision hash of the current directory."""
    try:
        # Run the git command with the --short option
        commit_hash_short = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], stderr=subprocess.DEVNULL).decode('utf-8').strip()
        return commit_hash_short
    except subprocess.CalledProcessError:
        return "Unknown"


#__gitversion__ = git_revision_short_hash()
__version__ = project_version()
__name__ = project_name()

if __name__ == "__main__":
    pass

