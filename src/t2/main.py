from src.t2.methods.power_method import PowerMethod
from src.t2.methods.eigen_jacobi import EigenJacobi
from src.utils.file_reader import getMatrixA

def run():

    order = int(input('Ordem N da matriz A: '))  
    matrix_A_file_path = input('Arquivo de entrada da matriz A: ')
    matrix_A = getMatrixA(matrix_A_file_path)
    icod = int(input('ICOD: '))
    idet = int(input('IDET: '))
    tol = float(input('TOLm: '))
    if(icod == 1):
        power_method_solution = PowerMethod()
    if(icod == 2):
        eigen_jacobi_solution = EigenJacobi()

    output_file_path = input('Arquivo de saída: ')

    with open(output_file_path, 'w') as output_file:
        output_file.write(f"Autovetor: {autovetor}\n")
        output_file.write(f"Autovalor: {autovalor}\n")
        output_file.write(f"Determinante: {det}")
        output_file.write(f"Feedback: {feedback}")
