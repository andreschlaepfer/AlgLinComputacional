from src.t1.main import main as t1_main
from src.t2.main import main as t2_main
from src.t3.main import main as t3_main


ex_map = {
  1: t1_main,
  2: t2_main,
  3: t3_main
}

if __name__ == '__main__':
  ex_map[int(input('Qual trabalho deseja executar?: '))]()