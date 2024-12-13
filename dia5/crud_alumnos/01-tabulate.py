from tabulate import tabulate

data = [
    ["100","cesar mayta","cesar@gmail.com"],
    ["200","jose perales","jose@gmail.com"],
    ["300","ana hinojoza","ana@gmail.com"],
]

columnas = ["DNI","NOMBRE","EMAIL"]

tabla = tabulate(data,headers=columnas,tablefmt="simple_grid")

print(tabla)