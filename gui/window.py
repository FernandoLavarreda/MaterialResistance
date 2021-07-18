# Fernando Lavarreda
# GUI to control the program

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
from tkinter.font import BOLD, Font


class Main(tk.Tk):
    def __init__(self, functions:dict, loc="media/metal.ico", materials=("car", "sher"), dbloc="") -> None:
        super().__init__()
        self.db = dbloc
        self.functions = functions
        self.title("Beam Selector FerLavarreda")
        self.geometry("+150+100")
        #self.resizable(False, False)
        menu = tk.Menu(self)
        menu.add_command(label="Config")
        menu.add_command(label="Perfiles")
        self.iconbitmap(loc)

        #------------------Objects in GUI----------------------
        lf_color = "#B7D8D6"
        rf_color = "#789E9E"
        bf_color = "#C6C4C4"
        left_frame = tk.LabelFrame(self, text="Plancha", background=lf_color)
        right_frame = tk.LabelFrame(self, text="Viga", background=rf_color)
        bottom_frame = tk.LabelFrame(self, background=bf_color)
        tk.Label(left_frame, text="Material:", pady=10, font=Font(size=8, weight='bold'), background=lf_color).grid(row=0, column=0)
        tk.Label(right_frame, text="Material:", pady=10, font=Font(size=8, weight='bold'), background=rf_color).grid(row=0, column=0)
        
        #--Plancha--
        self.get_planck_tstress = tk.DoubleVar()
        self.get_planck_cstress = tk.DoubleVar()
        self.get_planck_ymodulus = tk.DoubleVar()
        self.select1 = ttk.Combobox(left_frame, values=materials)

        self.select1.bind("<<ComboboxSelected>>", self.material_planck)


        ttk.Label(left_frame, text="Seleccion:", background=lf_color).grid(row=1, column=0, sticky=tk.NE+tk.SW)
        ttk.Label(left_frame, text="Modulo Young:", background=lf_color).grid(row=2, column=0, sticky=tk.NE+tk.SW)
        ttk.Label(left_frame, text="Esfuerzo Compresion:", background=lf_color).grid(row=3, column=0, sticky=tk.NE+tk.SW)
        ttk.Label(left_frame, text="Esfuerzo Tension:", background=lf_color).grid(row=4, column=0, sticky=tk.NE+tk.SW)
        # //
        ttk.Spinbox(left_frame, from_=1, to=300, textvariable=self.get_planck_ymodulus).grid(row=2, column=1, sticky=tk.NE+tk.SW)
        ttk.Spinbox(left_frame, from_=0.1, to=200, textvariable=self.get_planck_cstress).grid(row=3, column=1, sticky=tk.NE+tk.SW)
        ttk.Spinbox(left_frame, from_=0.1, to=200, textvariable=self.get_planck_tstress).grid(row=4, column=1, sticky=tk.NE+tk.SW)
        

        #Rest of variables
        self.get_planck_height = tk.DoubleVar()
        self.get_planck_s = tk.DoubleVar()
        tk.Label(left_frame, text="Propiedades:", font=Font(size=8, weight='bold'), pady=10, background=lf_color).grid(row=5, column=0)
        ttk.Label(left_frame, text="Longitud:", background=lf_color).grid(row=6, column=0, sticky=tk.NE+tk.SW)
        ttk.Label(left_frame, text="Altura:", background=lf_color).grid(row=7, column=0, sticky=tk.NE+tk.SW)
        # //
        ttk.Spinbox(left_frame, from_=0.1, to=200, textvariable=self.get_planck_s).grid(row=6, column=1, sticky=tk.NE+tk.SW)
        ttk.Spinbox(left_frame, from_=0.1, to=200, textvariable=self.get_planck_height).grid(row=7, column=1, sticky=tk.NE+tk.SW)


        #-----------

        #---Viga----
        self.get_beam_tstress = tk.DoubleVar()
        self.get_beam_cstress = tk.DoubleVar()
        self.get_beam_ymodulus = tk.DoubleVar()
        self.profile = tk.StringVar()
        self.select2 = ttk.Combobox(right_frame, values=materials)
        self.select2.bind("<<ComboboxSelected>>", self.material_beam)


        ttk.Label(right_frame, text="Seleccion:", background=rf_color).grid(row=1, column=0, sticky=tk.NE+tk.SW)
        ttk.Label(right_frame, text="Modulo Young:", background=rf_color).grid(row=2, column=0, sticky=tk.NE+tk.SW)
        ttk.Label(right_frame, text="Esfuerzo Compresion:", background=rf_color).grid(row=3, column=0, sticky=tk.NE+tk.SW)
        ttk.Label(right_frame, text="Esfuerzo Tension:", background=rf_color).grid(row=4, column=0, sticky=tk.NE+tk.SW)
        # //
        ttk.Spinbox(right_frame, from_=1, to=300, textvariable=self.get_beam_ymodulus).grid(row=2, column=1, sticky=tk.NE+tk.SW)
        ttk.Spinbox(right_frame, from_=0.1, to=200, textvariable=self.get_beam_cstress).grid(row=3, column=1, sticky=tk.NE+tk.SW)
        ttk.Spinbox(right_frame, from_=0.1, to=200, textvariable=self.get_beam_tstress).grid(row=4, column=1, sticky=tk.NE+tk.SW)

        tk.Label(right_frame, text="Perfiles:", font=Font(size=8, weight='bold'), pady=10, background=rf_color).grid(row=5, column=0)

        ttk.Entry(right_frame, textvariable=self.profile).grid(row=6, column=0)
        ttk.Button(right_frame, text="Agregar", command=self.add).grid(row=7, column=0, sticky=tk.NE+tk.SW)
        
        self.analyze = ttk.Combobox(right_frame, state="readonly", values=())
        ttk.Button(right_frame, text="Borrar seleccion", command=self.eliminate).grid(row=7, column=1, sticky=tk.NE+tk.SW)


        #--------------

        #-----Bottom Frame------
        self.optimal_momentum = tk.BooleanVar()
        self.momentum = tk.DoubleVar()
        ttk.Label(bottom_frame, text="Calcular momento optimo: ",  background=bf_color).grid(row=0, column=0, sticky=tk.NE+tk.SW)
        tk.Checkbutton(bottom_frame, variable=self.optimal_momentum, bg=bf_color).grid(row=0, column=1, sticky=tk.NE+tk.SW)
        ttk.Label(bottom_frame, text="Momento aplicado:", padding=(10, 0, 0, 0), background=bf_color).grid(row=0, column=2, sticky=tk.NE+tk.SW)
        self.mm = ttk.Entry(bottom_frame, textvariable=self.momentum)
        tk.Button(bottom_frame, text="Calcular", command=self.run, bg="#FE615A", relief=tk.FLAT, width=15).grid(row=0, column=4, columnspan=2, sticky=tk.NE+tk.SW)

        self.optimal_momentum.trace("w", self.habilitate)
        #-----------------------
        #-------------------------------------------------


        #---------------Load Objects into screen-----------------------------
        left_frame.grid(row=0, column=0, sticky=tk.NE+tk.SW)
        right_frame.grid(row=0, column=1, sticky=tk.NE+tk.SW)
        bottom_frame.grid(row=1, columnspan=2, sticky=tk.NE+tk.SW)
        self.select1.grid(row=1, column=1)
        self.select2.grid(row=1, column=1)
        self.analyze.grid(row=6, column=1, sticky=tk.NE+tk.SW)
        self.mm.grid(row=0, column=3, sticky=tk.NE+tk.SW)
        self.config(menu=menu, background="black")
        self.resizable(False, False)


    def add(self, *args):
        matches = self.functions['load_profiles'](self.db, self.profile.get().upper())
        for m in matches:
            if m[0] not in self.analyze['values']:
                self.analyze['values']+=(m[0],)

    def material_planck(self, *args):
        ymod, cstress, tstress = self.functions['load_material'](self.db, self.select1.get())
        self.get_planck_ymodulus.set(ymod)
        self.get_planck_cstress.set(cstress)
        self.get_planck_tstress.set(tstress)

    def material_beam(self, *args):
        ymod, cstress, tstress = self.functions['load_material'](self.db, self.select2.get())
        self.get_beam_ymodulus.set(ymod)
        self.get_beam_cstress.set(cstress)
        self.get_beam_tstress.set(tstress)

    def eliminate(self,*args):
        self.analyze.set("")
        self.analyze['values'] = []
    
    def habilitate(self, *args):
        if self.optimal_momentum.get():
            self.momentum.set(0)
            self.mm.config(state=tk.DISABLED)
        else:
            self.mm.config(state=tk.ACTIVE)
    
    def run(self, *args):
        if self.analyze['values']:
            try:
                yplanck = self.get_planck_ymodulus.get()
                csplanck = self.get_planck_cstress.get()
                tsplanck = self.get_planck_tstress.get()
                lens = self.get_planck_s.get()
                height_planck = self.get_planck_height.get()

                ybeam = self.get_beam_ymodulus.get()
                csbeam = self.get_beam_cstress.get()
                tsbeam = self.get_beam_tstress.get()

                mom = self.momentum.get()
                name1 = "plancha"
                name2 = "viga"
                if not self.select1.get() == "":
                    name1 = self.select1.get()
                if not self.select2.get() == "":
                    name2 = self.select2.get()
                mat_1 = self.functions['create_material'](name1, yplanck, csplanck, tsplanck)
                mat_2 = self.functions["create_material"](name2, ybeam, csbeam, tsbeam)
                main_planck = self.functions['create_planck'](height_planck, lens, mat_1)
                beams = []
                for beam in self.analyze['values']:
                    beams.append(self.functions['create_beam'](*self.functions["load_profiles"](self.db, beam)[0], mat_2))
                if self.optimal_momentum.get():
                    self.functions['secondary'](beams, main_planck)
                else:
                    self.functions['main'](beams, main_planck, mom)
            except Exception:
                mb.showerror("Error", "Entrada no numerica")
        else:
            mb.showerror("Error", "No se ha seleccionado al menos un perfil")
    

def foo(*args):
    return 0, 1, 20

def bar(*args):
    return ("W1100X499",)

if __name__ == "__main__":
    load = {'load_material':foo, 'load_profiles':bar}
    cad = Main(load)
    cad.mainloop()