import sys
import numpy as np
from fractions import Fraction

try:
    import pandas as pd
    pandas_av = True
except ImportError:
    pandas_av = False
    pass

product_names = []
col_values = []
z_equation = []
final_rows = []
solutions = []
x = 'X'
z2_equation = []
removable_vars = []
no_solution = """

            """


def main():
    global decimals
    global const_num, prod_nums
    print("""
    SIMPLEX CALCULADOR
    
SELECCIONE
    1 :MAXIMIZACIÓN (<=).
    2 :MINIMIZACIÓN (>=).
    
    """)
    try:
        prob_type = int(input("INGRESE EL NUMERO: >"))
    except ValueError:
        print("POR FAVOR INGRESAR UN VALOR NUMERICO CORRECTO")
        prob_type = int(input("INGRESE EL NUMERO: >"))
    if prob_type != 2 and prob_type != 1:
        sys.exit("NO ES UN VALOR CORRECTO, VOLVER A EJECUTAR ->" + str(prob_type))
    
        sys.exit()
    print('\n-------------------------------------------------')
    global const_names
    const_num = int(input("INGRESE CANTIDAD DE VARIABLES: >"))
    prod_nums = int(input("INGRESE CANTIDAD DE RESTRICCIONES: >"))
    const_names = [x + str(i) for i in range(1, const_num + 1)]
    for i in range(1, prod_nums + 1):
        prod_val = input("AÑADIR UN NOMBRE A LA RESTRICCIÓN #{} : >".format(i))
        product_names.append(prod_val)
    print("---------------------------------------------------")
    if prob_type == 1:
        for i in const_names:
            try:
                val = float(Fraction(input("INGRESE EL VALOR DE %s EN LA FUNCIÓN PRINCIPAL: >" % i)))
            except ValueError:
                print("POR FAVOR INGRESAR UN NÚMERO")
                val = float(Fraction(input("INGRESE EL VALOR DE %s EN LA FUNCIÓN PRINCIPAL: >" % i)))
            z_equation.append(0 - int(val))
        z_equation.append(0)

        while len(z_equation) <= (const_num + prod_nums):
            z_equation.append(0)
        print("----------------------------------------------")
        for prod in product_names:
            for const in const_names:
                try:
                    val = float(Fraction(input("INGRESE EL VALOR DE %s EN LA ECUACIÓN %s: >" % (const, prod))))
                except ValueError:
                    print("POR FAVOR INGRESAR UN NUMERO")
                    val = float(Fraction(input("INGRESE EL VALOR DE %s EN LA ECUACIÓN %s: >" % (const, prod))))
                col_values.append(val)
            equate_prod = float(Fraction(input('VALOR DE %s ES: >' % prod)))
            col_values.append(equate_prod)

        final_cols = stdz_rows(col_values)
        i = len(const_names) + 1
        while len(const_names) < len(final_cols[0]) - 1:
            const_names.append('X' + str(i))
            solutions.append('X' + str(i))
            i += 1
        solutions.append(' Z')
        const_names.append('Bi')
        final_cols.append(z_equation)
        final_rows = np.array(final_cols).T.tolist()
        print("----------------------------------------------")
        decimals = int(input('¿CUANTOS DECIMALES DESEA AÑADIR? : '))
        print('\n--------------------------------------------')
        maximization(final_cols, final_rows)

    elif prob_type == 2:
        for i in const_names:
            try:
                val = float(Fraction(input("INGRESE EL VALOR DE %s EN LA FUNCIÓN PRINCIPAL: >" % i)))
            except ValueError:
                print("POR FAVOR INGRESAR UN VALOR NUMERICO")
                val = float(Fraction(input("INGRESE EL VALOR DE %s EN LA FUNCIÓN PRINCIPAL: >" % i)))
            z_equation.append(val)
        z_equation.append(0)

        while len(z_equation) <= (const_num + prod_nums):
            z_equation.append(0)
        print("----------------------------------------------")
        for prod in product_names:
            for const in const_names:
                try:
                    val = float(Fraction(input("INGRESE EL VALOR DE %s EN LA ECUACIÓN %s: >" % (const, prod))))
                except ValueError:
                    print("POR FAVOR INGRESAR UN NUMERO")
                    val = float(Fraction(input("INGRESE EL VALOR DE %s EN LA ECUACIÓN %s: >" % (const, prod))))
                col_values.append(val)
            equate_prod = float(Fraction(input('VALOR DE %s ES: >' % prod)))
            col_values.append(equate_prod)

        final_cols = stdz_rows2(col_values)
        i = len(const_names) + 1
        while len(const_names) < prod_nums + const_num:
            const_names.append('X' + str(i))
            solutions.append('X' + str(i))
            i += 1
        solutions.append(' Z')
        solutions[:] = []
        add_from = len(const_names) + 1
        while len(const_names) < len(final_cols[0][:-1]):
            removable_vars.append('X' + str(add_from))
            const_names.append('X' + str(add_from))
            add_from += 1
        removable_vars.append(' Z')
        removable_vars.append('Z1')
        const_names.append('Bi')
        for ems in removable_vars:
            solutions.append(ems)
        while len(z_equation) < len(final_cols[0]):
            z_equation.append(0)
        final_cols.append(z_equation)
        final_cols.append(z2_equation)
        final_rows = np.array(final_cols).T.tolist()
        print("----------------------------------------------")
        decimals = int(input('¿CUANTOS DECIMALES DESEA AÑADIR? : '))
        print('\n----------------------------------------------')
        minimization(final_cols, final_rows)

    else:
        sys.exit("INGRESASTE UN VALOR NO VALIDO ->" + str(prob_type))

#PARA MAXIMIZACIÓN

def maximization(final_cols, final_rows):
    row_app = []
    last_col = final_cols[-1]
    min_last_row = min(last_col)
    min_manager = 1
    print(" 1 TABLA")
    try:
        final_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
        print(final_pd)
    except:
        print('  ', const_names)
        i = 0
        for cols in final_cols:
            print(solutions[i], cols)
            i += 1
    count = 2
    pivot_element = 2
    while min_last_row < 0 < pivot_element != 1 and min_manager == 1 and count < 6:
        print("---------------------------------------------------------")
        last_col = final_cols[-1]
        last_row = final_rows[-1]
        min_last_row = min(last_col)
        index_of_min = last_col.index(min_last_row)
        pivot_row = final_rows[index_of_min]
        index_pivot_row = final_rows.index(pivot_row)
        row_div_val = []
        i = 0
        for _ in last_row[:-1]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        pivot_element = pivot_row[index_min_div_val]
        pivot_col = final_cols[index_min_div_val]
        index_pivot_col = final_cols.index(pivot_col)
        row_app[:] = []
        for col in final_cols:
            if col is not pivot_col and col is not final_cols[-1]:
                form = col[index_of_min] / pivot_element
                final_val = np.array(pivot_col) * form
                new_col = (np.round((np.array(col) - final_val), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col

            elif col is pivot_col:
                new_col = (np.round((np.array(col) / pivot_element), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
            else:
                form = abs(col[index_of_min]) / pivot_element
                final_val = np.array(pivot_col) * form
                new_col = (np.round((np.array(col) + final_val), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
        final_rows[:] = []
        re_final_rows = np.array(final_cols).T.tolist()
        final_rows = final_rows + re_final_rows

        if min(row_div_val) != 10000000000:
            min_manager = 1
        else:
            min_manager = 0
        print('EL ELEMENTO PIVOTE ES: %s' % pivot_element)
        print('NUMEROS DE COLUMNA DEL PIVOTE SON: ', pivot_row)
        print('NUMEROS DE FILA DEL PIVOTE SON: ', pivot_col)
        print("\n")
        solutions[index_pivot_col] = const_names[index_pivot_row]

        print(" %d TABLA" % count)
        try:
            final_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
            print(final_pd)
        except:
            print("%d TABLA" % count)
            print('  ', const_names)
            i = 0
            for cols in final_cols:
                print(solutions[i], cols)
                i += 1
        count += 1
        last_col = final_cols[-1]
        last_row = final_rows[-1]
        min_last_row = min(last_col)
        index_of_min = last_col.index(min_last_row)
        pivot_row = final_rows[index_of_min]
        row_div_val = []
        i = 0
        for _ in last_row[:-1]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        pivot_element = pivot_row[index_min_div_val]
        if pivot_element < 0:
            print(no_solution)
    if not pandas_av:
        print("""
        EN CASO DE QUE NO FUNCIONE UTILIZAR EL COMANDO "pip install pandas" PARA INSTALAR EL COMPLEMENTO
        """)

#PARA MINIMIZACIÓN

def minimization(final_cols, final_rows):
    row_app = []
    last_col = final_cols[-1]
    min_last_row = min(last_col)
    min_manager = 1
    print("1 TABLA")
    try:
        fibal_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
        print(fibal_pd)
    except:
        print('  ', const_names)
        i = 0
        for cols in final_cols:
            print(solutions[i], cols)
            i += 1
    count = 2
    pivot_element = 2
    while min_last_row < 0 < pivot_element and min_manager == 1:
        print("----------------------------------------------")
        last_col = final_cols[-1]
        last_row = final_rows[-1]
        min_last_row = min(last_col[:-1])
        index_of_min = last_col.index(min_last_row)
        pivot_row = final_rows[index_of_min]
        index_pivot_row = final_rows.index(pivot_row)
        row_div_val = []
        i = 0
        for _ in last_row[:-2]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        pivot_element = pivot_row[index_min_div_val]
        pivot_col = final_cols[index_min_div_val]
        index_pivot_col = final_cols.index(pivot_col)
        row_app[:] = []
        for col in final_cols:
            if col is not pivot_col and col is not final_cols[-1]:
                form = col[index_of_min] / pivot_element
                final_form = np.array(pivot_col) * form
                new_col = (np.round((np.array(col) - final_form), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
            elif col is pivot_col:
                new_col = (np.round((np.array(col) / pivot_element), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
            else:
                form = abs(col[index_of_min]) / pivot_element
                final_form = np.array(pivot_col) * form
                new_col = (np.round((np.array(col) + final_form), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
        final_rows[:] = []
        re_final_rows = np.array(final_cols).T.tolist()
        final_rows = final_rows + re_final_rows
        if min(row_div_val) != 10000000000:
            min_manager = 1
        else:
            min_manager = 0
        print('EL ELEMENTO PIVOTE ES: %s' % pivot_element)
        print('NUMEROS DE COLUMNA DEL PIVOTE SON: ', pivot_row)
        print('NUMEROS DE FILA DEL PIVOTE SON: ', pivot_col)
        print("\n")
        removable = solutions[index_pivot_col]
        solutions[index_pivot_col] = const_names[index_pivot_row]
        if removable in removable_vars:
            idex_remove = const_names.index(removable)
            for colms in final_cols:
                colms.remove(colms[idex_remove])
            const_names.remove(removable)
        print("%d TABLA" % count)
        try:
            fibal_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
            print(fibal_pd)
        except:
            print('  ', const_names)
            i = 0
            for cols in final_cols:
                print(solutions[i], cols)
                i += 1
        count += 1
        final_rows[:] = []
        new_final_rows = np.array(final_cols).T.tolist()
        for _list in new_final_rows:
            final_rows.append(_list)

        last_col = final_cols[-1]
        last_row = final_rows[-1]
        min_last_row = min(last_col[:-1])
        index_of_min = last_col.index(min_last_row)
        pivot_row = final_rows[index_of_min]
        row_div_val = []
        i = 0
        for _ in last_row[:-2]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        pivot_element = pivot_row[index_min_div_val]
        if pivot_element < 0:
            print(no_solution)

    if not pandas_av:
        print("""
        EN CASO DE QUE NO FUNCIONE UTILIZAR EL COMANDO pip install pandas PARA INSTALAR EL COMPLEMENTO 
        """)


def stdz_rows2(column_values):
    final_cols = [column_values[x:x + const_num + 1] for x in range(0, len(column_values), const_num + 1)]
    sum_z = (0 - np.array(final_cols).sum(axis=0)).tolist()
    for _list in sum_z:
        z2_equation.append(_list)

    for cols in final_cols:
        while len(cols) < (const_num + (2 * prod_nums) - 1):
            cols.insert(-1, 0)

    i = const_num
    for sub_col in final_cols:
        sub_col.insert(i, -1)
        z2_equation.insert(-1, 1)
        i += 1

    for sub_col in final_cols:
        sub_col.insert(i, 1)
        i += 1

    while len(z2_equation) < len(final_cols[0]):
        z2_equation.insert(-1, 0)

    return final_cols


def stdz_rows(column_values):
    final_cols = [column_values[x:x + const_num + 1] for x in range(0, len(column_values), const_num + 1)]
    for cols in final_cols:
        while len(cols) < (const_num + prod_nums):
            cols.insert(-1, 0)

    i = const_num
    for sub_col in final_cols:
        sub_col.insert(i, 1)
        i += 1

    return final_cols

#none
if __name__ == "__main__":
    main()

