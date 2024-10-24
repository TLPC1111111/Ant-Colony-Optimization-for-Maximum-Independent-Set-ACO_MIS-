
import argparse
from ACO_of_MIS import ACO
import random
from init_support import AFIT

def Default_arguments():

    '''
    input parameters that can be provided directly
    The maximum and minimum values of x and y will confine the set of nodes in the graph to a certain interval
    '''

    parser = argparse.ArgumentParser(description = "use ACO solve Max Independent Set")
    parser.add_argument("--points_num" , type = int , default = 20 , help = "the number of points")
    parser.add_argument("--ants_num" , type = int , default = 6 , help = "the number of ants")
    parser.add_argument("--max_iteration" , type = int , default = 150)
    parser.add_argument("--rho" , type = float , default = 0.3 , help = "evaporation coefficient of pheromones")
    parser.add_argument("--alpha" , type = int, default = 3 ,help = "weight of pheromones")
    parser.add_argument("--beta" , type = int , default = 5 , help="weight of heuristic value")
    parser.add_argument("-Q" , type = float , default = 10)
    parser.add_argument("--max_x" , type = int , default = 300)
    parser.add_argument("--min_x" , type = int , default = 0)
    parser.add_argument("--max_y" , type = int , default = 300)
    parser.add_argument("--min_y" , type = int , default = 0)
    return parser

def main():
    args = Default_arguments().parse_args()
#    points = init_points(points_number = args.points_num , max_x = args.max_x , min_x = args.min_x , max_y = args.max_y , min_y = args.min_y)
    aco = ACO(ant_num = args.ants_num,
              max_iteration = args.max_iteration,
              alpha = args.alpha,
              beta = args.beta,
              rho = args.rho,
              Q = args.Q,
              points_num = args.points_num,
              max_x = args.max_x,
              min_x = args.min_x,
              max_y = args.max_y,
              min_y = args.min_y,
              afit_dat = AFIT)
    aco.run()


if __name__ == '__main__':
    main()

