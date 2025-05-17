from libvirt_client.client import LibvirtClient
from models.vm import VM

class VMController:
    def __init__(self, uri):
        self.client = LibvirtClient(uri)
        self.conn = self.client.connect()

    def get_all_vms(self):
        domains = self.client.list_vms()
        vms = []
        for d in domains:
            name = d.name()
            uuid = d.UUIDString()
            state, _ = d.state()  # estado numérico
            # traducimos el estado a texto simple
            status_map = {
                libvirt.VIR_DOMAIN_RUNNING: "Running",
                libvirt.VIR_DOMAIN_SHUTOFF: "Shut off",
                libvirt.VIR_DOMAIN_PAUSED:  "Paused",
                # añadir más si lo deseas
            }
            status = status_map.get(state, str(state))
            vms.append(VM(name, uuid, status))
        return vms
