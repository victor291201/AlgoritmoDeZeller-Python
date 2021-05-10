dia = int(input("ingrese el dia: "))
mes = int(input("ingrese el mes: "))
año = int(input("ingrese el año: "))

a = (14 - mes) // 12
y = año - a
m = mes + 12 * a - 2

ds = (dia + y + y//4 - y//100 + y//400 + (31*m)//12)%7

dia_s = ["domingo", "lunes", "martes", "miercoles", "jueves", "viernes","sabado"]

print(str(dia_s[ds]))
