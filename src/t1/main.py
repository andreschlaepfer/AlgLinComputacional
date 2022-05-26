from src.utils.file_reader import getMatrixA, getVectorB
from src.t1.methods.lu import LU
from src.t1.methods.cholesky import Cholesky
from src.t1.methods.jacobi import Jacobi
from src.t1.methods.gauss_seidel import GaussSeidel
import numpy as np

def main():

    order = int(input('Ordem do sistema de equações: ')) 
    matrix_A_file_path = input('Arquivo de entrada da matriz A: ')
    mA = getMatrixA(matrix_A_file_path)
    vector_B_file_path = input('Arquivo de entrada do vetor B: ')
    vB = getVectorB(vector_B_file_path)
    icod = int(input('ICOD: '))
    idet = int(input('IDET: '))
    return_det = False
    if(idet > 0):
        return_det = True
    isIterative = False
    if(icod == 1):
        lu_solution = LU(return_det)
        full_result = lu_solution.solve(mA,vB)
        result = full_result[0]
        det = full_result[1]
        feedback = lu_solution.feedback
    elif(icod == 2):
        cholesky_solution = Cholesky(return_det)
        full_result = cholesky_solution.solve(mA,vB)
        result = full_result[0]
        det = full_result[1]
        feedback = cholesky_solution.feedback
    elif(icod == 3):
        isIterative = True
        jacobi_solution = Jacobi()
        tol = float(input('Valor de TOLm: '))
        full_it_result = jacobi_solution.procedimento_iterativo_Jacobi(mA,vB, tol)
        feedback = jacobi_solution.feedback
        result = full_it_result[0]
        counter = full_it_result[1]
        logs = full_it_result[2]
    elif(icod == 4):
        isIterative = True
        jacobi_solution = GaussSeidel()
        tol = float(input('Valor de TOLm: '))
        full_it_result = jacobi_solution.procedimento_iterativo_GaussSeidel(mA,vB, tol)
        feedback = jacobi_solution.feedback
        result = full_it_result[0]
        counter = full_it_result[1]
        logs = full_it_result[2]

    print(f"A: {np.matrix(mA)}")
    print(f"B: {np.array(vB)}")
    print(f"Vetor Solucao: {result}")

    output_file_path = input('Arquivo de saída: ')
    if(output_file_path == ""):
        output_file_path = "out.txt"

    with open(output_file_path, 'w') as output_file:
        output_file.write(f"Vetor Solucao: {np.array(result)}\n")
        if(not isIterative):
            output_file.write(f"Determinante: {det}\n")
        if(isIterative):
            output_file.write(f"Numero de iteracoes para convergencia: {counter}\n")
            output_file.write(f"Variacao do erro nas iteracoes: {logs}\n")
        output_file.write(f"Feedback: {feedback}\n")


