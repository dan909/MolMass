from tkinter import *
from tkinter import ttk
import re

atomicMass = dict(H=1.01, He=4.00, Li=6.94, Be=9.01, B=10.81, C=12.01,
                  N=14.01, O=16.00, F=19.00, Ne=20.18, Na=22.99, Mg=24.31,
                  Al=26.98, Si=28.09, P=30.97, S=32.07, Cl=35.45, Ar=39.95,
                  K=39.10, Ca=40.08, Sc=44.96, Ti=47.87, V=50.94, Cr=52.00,
                  Mn=54.94, Fe=55.85, Co=58.93, Ni=58.69, Cu=63.55, Zn=65.39,
                  Ga=69.72, Ge=72.61, As=74.92, Se=78.96, Br=79.90, Kr=83.80,
                  Rb=85.47, Sr=87.62, Y=88.91, Zr=91.22, Nb=92.91, Mo=95.94,
                  Tc=98.00, Ru=101.07, Rh=102.91, Pd=106.42, Ag=107.87,
                  Cd=112.41, In=114.82, Sn=118.71, Sb=121.76, Te=127.60,
                  I=126.90, Xe=131.29, Cs=132.91, Ba=137.33, La=138.91,
                  Ce=140.12, Pr=140.91, Nd=144.24, Pm=145.00, Sm=150.36,
                  Eu=151.96, Gd=157.25, Tb=158.93, Dy=162.50, Ho=164.93,
                  Er=167.26, Tm=168.93, Yb=173.04, Lu=174.97, Hf=178.49,
                  Ta=180.95, W=183.84, Re=186.21, Os=190.23, Ir=192.22,
                  Pt=195.08, Au=196.97, Hg=200.59, Tl=204.38, Pb=207.2,
                  Bi=208.98, Po=209.00, At=210.00, Rn=222.00, Fr=223.00,
                  Ra=226.00, Ac=227.00, Th=232.04, Pa=231.04, U=238.03,
                  Np=237.00, Pu=244.00, Am=243.00, Cm=247.00, Bk=247.00,
                  Cf=251.00, Es=252.00, Fm=257.00, Md=258.00, No=259.00,
                  Lr=262.00, Rf=261.00, Db=262.00, Sg=266.00, Bh=264.00,
                  Hs=269.00, Mt=268.00)


def atomic_Mass(dic, value):
    try:
        dic[value]
        return dic[value]
    except KeyError:
        return False


def calculate(*args):
    try:
        element_list = [a for a in re.split(r'([A-Z][a-z]*\d*)', str(Formula.get())) if a]
        cem_mass = 0
        for e in element_list:
            part_cem = re.split('(\d+)', e)
            mol_no = 1
            mol_mass = 0

            for p in part_cem:
                #print p
                if p.isdigit():
                    mol_no += (int(p) - 1)
                else:
                    if atomic_Mass(atomicMass, p) != False:
                        mol_mass = atomic_Mass(atomicMass, p)
            cem_mass += (mol_mass * mol_no)
        #print cem_mass
        mass.set(float(cem_mass))
    except ValueError:
        pass

root = Tk()
root.title("has a molar mass of")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

Formula = StringVar()
mass = StringVar()

Formula_entry = ttk.Entry(mainframe, width=20, textvariable=Formula)
Formula_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=mass).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Formula i.e. H2O or NaCl").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="... has a molar mass of ").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="grams").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

Formula_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()