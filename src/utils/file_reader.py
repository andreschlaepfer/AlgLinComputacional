def getMatrixA(file_path):
  matrixA = []
  with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
      new_line = line.replace('\n', '').split()
      new_line = [float(x) for x in new_line]
      matrixA.append(new_line)

  return matrixA

def getVectorB(file_path):
  vectorB = []
  with open(file_path, 'r') as file:
    lines = file.readlines()
    vectorB = [float(x) for x in lines]

  return vectorB