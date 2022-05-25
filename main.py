from src.t1.main import main as ex1_main
from src.t2.main import main as ex2_main
from src.t3.main import main as ex3_main


ex_map = {
  1: ex1_main,
  2: ex2_main,
  3: ex3_main
}

if __name__ == '__main__':
  ex_map[int(input('Escolha o trabalho que deseja executar: '))]()