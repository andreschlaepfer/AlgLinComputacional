from src.utils.file_reader import getMatrixA, getVectorB
from src.t1.methods.lu import LU
from src.t1.methods.cholesky import Cholesky
from src.t1.methods.jacobi import Jacobi
from src.t1.methods.gauss_seidel import GaussSeidel


def main():

    order = int(input('Ordem do sistema de equações: ')) 
    matrix_A_file_path = input('Arquivo de entrada da matriz A: ')
    mA = getMatrixA(matrix_A_file_path)
    vector_B_file_path = input('Arquivo de entrada do vetor B: ')
    vB = getVectorB(vector_B_file_path)
    icod = int(input('ICOD: '))
    idet = int(input('IDET: '))
    isIterative = False
    if(icod == 1):
        if(idet == 0):
            lu_solution = LU(False)
        elif (idet > 0):
            lu_solution = LU(True)
        full_result = lu_solution.solve(mA,vB)
        result = full_result[0]
        det = full_result[1]
        feedback = lu_solution.feedback
    elif(icod == 2):
        cholesky_solution = Cholesky()
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

    print(f"A: {mA}")
    print(f"B: {vB}")
    print(f"Vetor Solucao: {result}")

    output_file_path = input('Arquivo de saída: ')
    if(output_file_path == ""):
        output_file_path = "out.txt"

    with open(output_file_path, 'w') as output_file:
        output_file.write(f"Vetor Solução: {result}\n")
        if(not isIterative):
            output_file.write(f"Determinante: {det}\n")
        if(isIterative):
            output_file.write(f"Número de iterações para convergência: {counter}\n")
            output_file.write(f"Variação do erro nas iterações: {logs}\n")
        output_file.write(f"Feedback: {feedback}\n")


