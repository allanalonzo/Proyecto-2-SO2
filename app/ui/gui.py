import tkinter as tk
from tkinter import ttk, messagebox
from config.config import get_libvirt_uri
from controllers.vm_controller import VMController

class VMManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cliente de Virtualización")
        self.geometry("900x600")
        # Controlador de VMs
        self.vm_ctrl = VMController(get_libvirt_uri())

        # Construcción de la UI
        self._create_menu()
        self._create_toolbar()
        self._create_main_panes()
        self._create_status_bar()

        # Carga inicial de VMs
        self._load_vms()

    def _create_menu(self):
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Importar...", command=self.on_import)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.quit)
        menubar.add_cascade(label="Archivo", menu=filemenu)
        # TODO: Máquina, Ver, Ayuda...
        self.config(menu=menubar)

    def _create_toolbar(self):
        toolbar = tk.Frame(self, bd=1, relief=tk.RAISED)
        btn_new = tk.Button(toolbar, text="Nuevo", command=self.on_new_vm)
        btn_start = tk.Button(toolbar, text="Iniciar", command=self.on_start_vm)
        btn_stop = tk.Button(toolbar, text="Detener", command=self.on_stop_vm)
        btn_refresh = tk.Button(toolbar, text="Actualizar", command=self.on_refresh)
        btn_cfg = tk.Button(toolbar, text="⚙️", command=self.on_configure_vm)
        for btn in (btn_new, btn_start, btn_stop, btn_refresh, btn_cfg):
            btn.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

    def _create_main_panes(self):
        paned = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        # Izquierda: lista de VMs
        frame_list = ttk.Frame(paned, width=200)
        self.tree = ttk.Treeview(
            frame_list,
            columns=("Nombre", "Estado"),
            show="headings"
        )
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Estado", text="Estado")
        self.tree.pack(fill=tk.BOTH, expand=True)
        frame_list.pack(fill=tk.BOTH, expand=True)
        paned.add(frame_list, weight=1)

        # Derecha: notebook de detalles
        frame_details = ttk.Frame(paned)
        self.notebook = ttk.Notebook(frame_details)
        for tab in ("General", "Sistema", "Pantalla", "Almacenamiento", "Red"):
            f = ttk.Frame(self.notebook)
            self.notebook.add(f, text=tab)
            # Aquí luego añadiremos widgets de cada pestaña
        self.notebook.pack(fill=tk.BOTH, expand=True)
        frame_details.pack(fill=tk.BOTH, expand=True)
        paned.add(frame_details, weight=3)

        paned.pack(fill=tk.BOTH, expand=True)

    def _create_status_bar(self):
        self.status = tk.Label(
            self,
            text="0 VMs — Listo",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def _load_vms(self):
        """
        Carga la lista de VMs en el Treeview.
        """
        # Limpiar el tree
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Obtener VMs del controlador
        try:
            vms = self.vm_ctrl.get_all_vms()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar las VMs: {e}")
            return

        # Poblar el tree
        for vm in vms:
            self.tree.insert(
                "",
                tk.END,
                iid=vm.uuid,
                values=(vm.name, vm.status)
            )
        self.status.config(text=f"{len(vms)} VMs — Listo")

    # Callbacks
    def on_import(self):
        # TODO: implementar importación de config o VM
        pass

    def on_new_vm(self):
        # TODO: abrir diálogo de creación
        pass

    def on_start_vm(self):
        # TODO: iniciar VM seleccionada
        pass

    def on_stop_vm(self):
        # TODO: detener VM seleccionada
        pass

    def on_refresh(self):
        self._load_vms()

    def on_configure_vm(self):
        # TODO: abrir pestañas de configuración para VM seleccionada
        pass

if __name__ == "__main__":
    app = VMManagerApp()
    app.mainloop()