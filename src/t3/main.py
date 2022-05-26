from src.t3.methods.interpolation import Interpolation
from src.t3.methods.regression import Regression
from src.utils.file_reader import getMatrixA

def main():
    icod = int(input('ICOD: '))
    # n = int(input('Número de pontos: '))
    matrix_A_file_path = input('Arquivo de entrada de pontos X, Y: ')
    points = getMatrixA(matrix_A_file_path)

    ##points = []
    ##for i in range(n):
       ## x, y = map(float, input("Pontos X e Y: ").split())
        ##points.append([x,y])

    xp = float(input('Para qual X deseja calcular o valor Y?: '))
    
    if(icod == 1):
        interpolation_solution = Interpolation(points)
        result = interpolation_solution.get_lagrangian_interpolation_yp_from_xp(xp)
        feedback = interpolation_solution.feedback

    elif(icod == 2):
        regression_solution = Regression(points)
        result = regression_solution.linear_regression(xp)
        feedback = regression_solution.feedback

    output_file_path = input('Arquivo de saída: ')
    if(output_file_path == ""):
        output_file_path = "out.txt"

    with open(output_file_path, 'w') as output_file:
        output_file.write(f"Valor de y: {result}\n")
        output_file.write(f"Feedback: {feedback}\n")

        


