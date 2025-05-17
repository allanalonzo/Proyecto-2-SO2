
import os

def get_libvirt_uri():
    return os.environ.get('LIBVIRT_URI', 'qemu:///system')
