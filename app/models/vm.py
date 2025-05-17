\"\"\"
vm.py: definiciÃ³n de la clase VM.
\"\"\"
class VM:
    def __init__(self, name, uuid, status):
        self.name = name
        self.uuid = uuid
        self.status = status

    def __repr__(self):
        return f\"<VM name={self.name} status={self.status}>\"
