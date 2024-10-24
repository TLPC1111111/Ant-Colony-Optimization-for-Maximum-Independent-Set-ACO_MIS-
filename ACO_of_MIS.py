import random
import matplotlib.pyplot as plt
import keyboard
import pprint
import tqdm
from Utilize import init_points , init_edges , eta , two_dim_list_calculate_its_j_element , draw_picture , init_SRS_edges
from init_support import AFIT

#random.seed(1)

class ACO(object):

    '''
    Using ACO to solve the Maximum Independent Set problem
    '''

    def __init__(self,ant_num:int , max_iteration:int , alpha:int , beta:int , rho:float , Q:int , points_num:int , max_x:int  , min_x:int
                 , max_y:int , min_y:int , afit_dat):

        '''
        :param ant_num: ---population size
        :param max_iteration:
        :param alpha: ---weight of pheromones
        :param beta: ---weight of heuristic value
        :param rho: ---evaporation coefficient of pheromones
        :param Q: 10
        :param points_num: ---number of nodes in the graph
        :param edges_num: ---Roughly equal to the number of nodes
        '''
        afit = afit_dat('reqlf13')
        self.ant_num = ant_num
        self.max_iteration = max_iteration
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.Q = Q
        self.points_num = afit.calculate_visibility_arcs_length()
        self.max_x = max_x
        self.min_x = min_x
        self.max_y = max_y
        self.min_y = min_y
        self.points = init_points(self.points_num ,self.max_x , self.min_x , self.max_y , self.min_y)
        self.edges_num = len(init_SRS_edges(afit_dat))
        self.edges = init_SRS_edges(afit_dat)
        self.tao = [1 for _ in range(self.points_num)]
        self.eta = eta(self.points , self.edges)


    def init_taboo_list(self):

        '''
        save every ants' position : self.taboo_list is 2 dim list ,
        and such that : self.taboo_list[x][y]  , x means No.x ant , y means step y ,
        so self.taboo_list[x][y] means No.x ant , in its step y , where it is located.
        '''

        self.taboo_list = []
        for i in range(self.ant_num):
            node = random.randint(0 , len(self.points)-1)
            self.taboo_list.append([node])


    def update_taboo_list(self , ant_paths):

        '''
        :param ant_paths:   ant_path is 2 dim list ,
        such that ant_path[x][y] means that the path of No.x ant.
        '''

        for i in range(self.ant_num):
            self.taboo_list[i].append(ant_paths[i][1])


    def init_feasible_list(self):

        '''
        initialize feasible_list : feasible_list[i][j] such that
        ith ant's No.j feasible Node
        feasible_list = {Node_set - taboo_list | (v_i , v_j) not in edges , for all v_i in taboo_list}，
        '''

        self.feasible_list = []
        for i in range(self.ant_num):
            flag = []
            for j in range(self.points_num):
                if j not in self.taboo_list[i]:
                    flag.append(j)
            self.feasible_list.append(flag)
        for i in range(self.ant_num):
            zzy = []
            for j in self.feasible_list[i]:
                for k in self.taboo_list[i]:
                    if [j,k] in self.edges or [k,j] in self.edges:
                        zzy.append(j)
            for p in range(len(zzy)):
                self.feasible_list[i].remove(zzy[p])

    def update_feasible_list(self , ant_id):
        zzy = []
        for j in self.feasible_list[ant_id]:
            for k in self.taboo_list[ant_id]:
                if [j,k] in self.edges or [k,j] in self.edges:
                    #self.feasible_list[ant_id].remove(j)
                    zzy.append(j)
        for i in range(len(zzy)):
            self.feasible_list[ant_id].remove(zzy[i])


    def choose_next_node(self , ant_id):

        '''
        The ant with ID 'ant_id' selects the next node at node 'node_th'
        Use roulette wheel selection and calculated probability to select next node
        '''

        probability_up = []
        for i in range(self.points_num):
            if i in self.feasible_list[ant_id]:
                probability_up.append(self.tao[i]**self.alpha * self.eta[i]**self.beta)
            else:
                probability_up.append(0)
        if max(probability_up) == 0:
            return
        probability = []
        for i in range(len(probability_up)):
            probability.append(probability_up[i] / sum(probability_up))
        n = sum(probability)
        r = random.uniform(0 , n)
        pos = 0
        while True:
            if probability[pos] == 0:
                pos += 1
            elif r - probability[pos] < 0:
                return pos
            else :
                r = r - probability[pos]
                pos += 1


    def update_tao(self):

        '''
        update pheromones
        Some coefficients need to be optimized
        '''

        if max(len(sublist) for sublist in self.feasible_list) == 0:
            for i in range(self.points_num):
                self.tao[i] = (1 - self.rho) * self.tao[i]
            delta_tao = []   ##表示第i只蚂蚁在节点j上留下的信息素
            for i in range(self.ant_num):
                delta = []
                for j in range(self.points_num):
                    if j in self.taboo_list[i]:
                        delta.append(len(self.taboo_list) / self.edges_num * self.Q)
                    else:
                        delta.append(0)
                delta_tao.append(delta)
            for i in range(self.points_num):
                self.tao[i] = self.tao[i] + two_dim_list_calculate_its_j_element(delta_tao , i)


    def run(self):
        for iteration in tqdm.tqdm(range(self.max_iteration) , desc = "Processing"):
            if keyboard.is_pressed('esc'):
                print("------------------A handsome boy pressed his holy esc------------------")
                break
            self.init_taboo_list()
            self.init_feasible_list()
            for i in range(self.points_num):
                ants_path = []
                zzy = []
                for j in range(self.ant_num):
                    pos = self.taboo_list[j][-1]
                    next_node = self.choose_next_node(j)
                    ants_path.append([pos , next_node])
                    if next_node != None:
                        self.taboo_list[j].append(next_node)
                        self.feasible_list[j].remove(next_node)
                        self.update_feasible_list(j)
                self.update_tao()
                if max(len(sublist) for sublist in self.feasible_list) == 0:
                    break
        ###################################################
                    # 找出具有最大独立集的蚂蚁
            max_set_size = 0
            max_ant_id = 0
            for i in range(len(self.taboo_list)):
                if len(self.taboo_list[i]) > max_set_size:
                    max_set_size = len(self.taboo_list[i])
                    max_ant_id = i

                    # 输出最大独立集节点个数
            print(f"循环次数： {iteration + 1}: ACO在afscn数据集上所求出的最大独立集节点个数为 = {max_set_size}")
            pprint.pprint(f"ACO在afscn数据集上所求出的最大独立集为: {sorted(self.taboo_list[max_ant_id])}")
        ####################################################



        #可视化
            #plt.cla()
            #plt.title("Use ACO Solve MIS Problem")
            #draw_picture(self.points , self.edges , iteration , self.taboo_list)
            #if iteration != self.max_iteration - 1:
            #    plt.pause(0.2)
            #elif keyboard.is_pressed('ctrl + p'):
            #    print("------------------A handsome boy pressed his holy p------------------")
            #    plt.show()
            #    break
            #else :
            #    plt.show()
