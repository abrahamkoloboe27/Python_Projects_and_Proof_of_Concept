"""
This application is using TKinter, GUI package of python, to create
a graphic interface to  make conversions
"""

"""
Cette application utilise la bibliothèque GUI Tkinter de Python pour 
créer une interface qui permette de faire des conversions.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#Temperature function converter
# Fonction de conversion pour la température
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value + 459.67) * 5/9
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value * 9/5) - 459.67
    raise ValueError("Conversion de température non prise en charge.")

#Weight function converter
# Fonction de conversion pour le poids
def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilogramme": 1,
        "Gramme": 0.001,
        "Livre": 0.453592,
        "Once": 0.0283495,
        "Tonne": 1000,
    }
    if from_unit in weight_units and to_unit in weight_units:
        return value * weight_units[to_unit] / weight_units[from_unit]
    raise ValueError("Conversion de poids non prise en charge.")

#Strengh function converter
# Fonction de conversion pour la force
def convert_force(value, from_unit, to_unit):
    force_units = {
        "Newton": 1,
        "Kilonewton": 1000,
        "Livres-force": 4.44822,
        "Kilogramme-force": 9.80665,
    }
    if from_unit in force_units and to_unit in force_units:
        return value * force_units[to_unit] / force_units[from_unit]
    raise ValueError("Conversion de force non prise en charge.")

#Pression function converter 
# Fonction de conversion pour la pression
def convert_pressure(value, from_unit, to_unit):
    pressure_units = {
        "Pascal": 1,
        "Bar": 100000,
        "Atmosphère": 101325,
        "Psi": 6894.76,
        "Torr": 133.322,
    }
    if from_unit in pressure_units and to_unit in pressure_units:
        return value * pressure_units[to_unit] / pressure_units[from_unit]
    raise ValueError("Conversion de pression non prise en charge.")

#Mass function converter
# Fonction de conversion pour la masse
def convert_mass(value, from_unit, to_unit):
    return convert_weight(value, from_unit, to_unit)  # La conversion est identique pour la masse et le poids

# Time's function converter
# Fonction de conversion pour le temps
def convert_time(value, from_unit, to_unit):
    time_units = {
        "Seconde": 1,
        "Minute": 60,
        "Heure": 3600,
        "Jour": 86400,
        "Semaine": 604800,
    }
    if from_unit in time_units and to_unit in time_units:
        return value * time_units[to_unit] / time_units[from_unit]
    raise ValueError("Conversion de temps non prise en charge.")

#Distance's function converter
# Fonction de conversion pour la distance
def convert_distance(value, from_unit, to_unit):
    distance_units = {
        "Mètre": 1,
        "Kilomètre": 1000,
        "Mile": 1609.34,
        "Pouce": 0.0254,
        "Pied": 0.3048,
    }
    if from_unit in distance_units and to_unit in distance_units:
        return value * distance_units[to_unit] / distance_units[from_unit]
    raise ValueError("Conversion de distance non prise en charge.")



# Function that's call when we'll press 'Convert'
# Fonction appelée lorsque le bouton "Convertir" est cliqué
def on_convert_click():
    try:
        value = float(entry_value.get())
        from_unit = unit_var.get()
        to_unit = convert_var.get()
        result_label.config(text="Résultat : Calcul en cours...")

        # Effectuer la conversion en fonction du type de mesure choisi
        if type_var.get() == "Température":
            result = convert_temperature(value, from_unit, to_unit)
        elif type_var.get() == "Poids":
            result = convert_weight(value, from_unit, to_unit)
        elif type_var.get() == "Force":
            result = convert_force(value, from_unit, to_unit)
        elif type_var.get() == "Pression":
            result = convert_pressure(value, from_unit, to_unit)
        elif type_var.get() == "Masse":
            result = convert_mass(value, from_unit, to_unit)
        elif type_var.get() == "Temps":
            result = convert_time(value, from_unit, to_unit)
        elif type_var.get() == "Distance":
            result = convert_distance(value, from_unit, to_unit)
        else:
            raise ValueError("Type de mesure non pris en charge.")
        
        result_label.config(text=f"Résultat : {result:.3f} {to_unit}")
    except ValueError:
        messagebox.showerror("Erreur", "Valeur non valide. Veuillez saisir un nombre.")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

#Creating graphic interface 
# Créer l'interface graphique
root = tk.Tk()
root.title("Convertisseur d'unités et de change")


#Main frame
# Cadre principal
main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=10)

#TKinter's variables
# Variables Tkinter
type_var = tk.StringVar()
unit_var = tk.StringVar()
convert_var = tk.StringVar()

#Measurements's list
# Liste des mesures par type
measurements = {
    " " : [""],
    "Température": ["Celsius", "Fahrenheit", "Kelvin"],
    "Poids": ["Kilogramme", "Gramme", "Livre", "Once", "Tonne"],
    "Force": ["Newton", "Kilonewton", "Livres-force", "Kilogramme-force"],
    "Pression": ["Pascal", "Bar", "Atmosphère", "Psi", "Torr"],
    "Masse": ["Kilogramme", "Gramme", "Livre", "Once", "Tonne"],
    "Temps": ["Seconde", "Minute", "Heure", "Jour", "Semaine"],
    "Distance": ["Mètre", "Kilomètre", "Mile", "Pouce", "Pied"],
}


#Drop-dow menu to choose mesure's type
# Menu déroulant pour choisir le type de mesure
type_label = ttk.Label(main_frame, text="Choisissez le type de mesure :")
type_label.grid(row=0, column=0, sticky="w")
type_menu = ttk.OptionMenu(main_frame, type_var, *measurements.keys())
type_menu.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

#Drop-dow menu to choose conversion mesure
# Menu déroulant pour choisir la mesure de conversion
convert_label = ttk.Label(main_frame, text="De :")
convert_label.grid(row=1, column=0, sticky="w")
convert_menu = ttk.OptionMenu(main_frame, convert_var, "")
convert_menu.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

#Drop-dow menu to choose to choose principal meusure
# Menu déroulant pour choisir la mesure principale
unit_label = ttk.Label(main_frame, text="En :")
unit_label.grid(row=2, column=0, sticky="w")
unit_menu = ttk.OptionMenu(main_frame, unit_var, "")
unit_menu.grid(row=2, column=1, padx=5, pady=5, sticky="ew")


#Value to convert
# Champ d'entrée pour la valeur à convertir
value_label = ttk.Label(main_frame, text="Entrez la valeur :")
value_label.grid(row=3, column=0, sticky="w")
entry_value = ttk.Entry(main_frame)
entry_value.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

#Convert button
# Bouton pour convertir
convert_button = ttk.Button(main_frame, text="Convertir", command=on_convert_click)
convert_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

#Convertion result
# Label pour afficher le résultat de la conversion
result_label = ttk.Label(main_frame, text="Résultat :")
result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Drop-dow menu to update measurements
# Mettre à jour les menus déroulants lorsque le type de mesure change
def update_measurements(*args):
    unit_menu['menu'].delete(0, 'end')
    convert_menu['menu'].delete(0, 'end')
    for unit in measurements[type_var.get()]:
        unit_menu['menu'].add_command(label=unit, command=lambda value=unit: unit_var.set(value))
        convert_menu['menu'].add_command(label=unit, command=lambda value=unit: convert_var.set(value))
    unit_var.set(measurements[type_var.get()][0])
    convert_var.set(measurements[type_var.get()][0])

type_var.trace('w', update_measurements)

root.mainloop()
