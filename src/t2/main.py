from src.t2.methods.power_method import PowerMethod
from src.t2.methods.eigen_jacobi import EigenJacobi
from src.utils.file_reader import getMatrixA
import numpy as np

def main():

    order = int(input('Ordem N da matriz A: '))  
    matrix_A_file_path = input('Arquivo de entrada da matriz A: ')
    mA = getMatrixA(matrix_A_file_path)
    icod = int(input('ICOD: '))
    idet = int(input('IDET: '))
    tol = float(input('TOLm: '))
    return_det = False
    if(idet>0):
        return_det = True
    if(icod == 1):
        power_method_solution = PowerMethod()
        autovalores = np.array(power_method_solution[0])
        autovetores = np.array(power_method_solution[1])
        det = power_method_solution[2]
        feedback = power_method_solution.feedback
    if(icod == 2):
        eigen_jacobi_solution = EigenJacobi(return_det)
        full_result = eigen_jacobi_solution.eigenJacobiMethod(mA, tol)
        autovalores = np.diag(np.array(full_result[0]))
        print(np.matrix(autovalores))
        autovetores = full_result[1]
        det = full_result[2]
        feedback = eigen_jacobi_solution.feedback

    output_file_path = input('Arquivo de saída: ')
    if(output_file_path == ""):
        output_file_path = "out.txt"

    with open(output_file_path, 'w') as output_file:
        output_file.write(f"Autovetor: {autovetores}\n")
        output_file.write(f"Autovalor: {autovalores}\n")
        output_file.write(f"Determinante: {det}")
        output_file.write(f"Feedback: {feedback}")
