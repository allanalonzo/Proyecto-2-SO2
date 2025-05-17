import libvirt

class LibvirtClient:
    def __init__(self, uri='qemu:///system'):
        self.uri = uri
        self.conn = None

    def connect(self):
        if self.conn is None:
            try:
                self.conn = libvirt.open(self.uri)
            except libvirt.libvirtError as e:
                raise RuntimeError(f"No pude conectar a libvirt: {e}")
        return self.conn

    def list_vms(self):
        # Obtiene todos los dominios (activos e inactivos)
        domains = self.conn.listAllDomains(0)
        return domains
