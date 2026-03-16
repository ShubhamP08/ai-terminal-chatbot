import os
import platform
import subprocess


def is_windows():
    """Check if the OS is Windows."""
    return platform.system() == 'Windows'


def is_mac():
    """Check if the OS is macOS."""
    return platform.system() == 'Darwin'


def is_linux():
    """Check if the OS is Linux."""
    return platform.system() == 'Linux'


def command_exists(command):
    """Check if a command exists in the system."""
    return subprocess.call(['which', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0


def get_package_manager():
    """Get the platform-specific package manager."""
    if is_windows():
        return 'choco'  # Chocolatey
    elif is_mac():
        return 'brew'  # Homebrew
    elif is_linux():
        return 'apt'  # APT for Debian/Ubuntu
    return None