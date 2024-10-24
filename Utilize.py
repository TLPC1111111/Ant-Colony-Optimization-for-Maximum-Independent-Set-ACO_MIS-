import random
from init_support import AFIT
import matplotlib.pyplot as plt
import tqdm
def init_points(points_number , max_x , min_x , max_y , min_y):

    '''
    out put the nodes of graph (random) and build a .txt which save these nodes
    '''
    points = []
    while len(points) != points_number:
        x = random.randint(min_x , max_x)
        y = random.randint(min_y , max_y)
        if [x,y] in points:
            continue
        points.append([x,y])
    with open("./points_temp.txt" , 'w') as fp:
        for j in range(points_number):
            fp.write(f'{points[j][0]} {points[j][1]}\n')
    print("points data was saved in file [edges_temp.txt] , rename it if you want to use it again")
    return points

def init_edges(points , edges_num):
    '''

    output the edges of graph (random) and build a .txt to save these edges
    edges such that : [[0,34] , [45,3] , [21 , 24] , .... , [3 , 66]]  ,
    (0,34,45,3,21,24,66) is the index of nodes(points)
    '''
    edges = []
    while len(edges) != edges_num:
        p1 = random.choice(range(0,len(points)-1))
        p2 = random.choice(range(0,len(points)-1))
        if [p1,p2] in edges or p1 == p2 or [p2,p1] in edges:
            continue
        edges.append([p1,p2])
    with open("./edges_temp.txt" , 'w') as fp:
        for j in range(edges_num):
            fp.write(f'{edges[j][0]} {edges[j][1]}\n')
    print("Edges data was saved in file [edges_temp.txt] , rename it if you want to use it again")
    return edges

def eta(points , edges):
    '''
    Computed heuristic value eta:
    such that eta_i = 1/deg(node_i)
    function deg means that the number of edges connecting node i
    Some coefficients need to be optimized
    '''
    deg = []
    for index , value in enumerate(points):
        flag = 0
        for j in range(len(edges)):
            if index in edges[j]:
                flag += 1
        if flag != 0:
            deg.append(1/(flag * 5))
        else:
            deg.append(1)
    return deg

def two_dim_list_calculate_its_j_element(list , j):
    '''
    Computes the sum of the elements in column i of the list
    '''
    flag = 0
    for i in range(len(list)):
        flag += list[i][j]
    return flag

def draw_picture(points , edges , iteration , path):
    ant_num = len(path)
    #这里的path相当于完成全部旅程后的路径，即独立集。
    x = []
    y = []
    for i in range(len(points)):
        x.append(points[i][0])
        y.append(points[i][1])
    plt.scatter(x , y , s = 80)


    for i in range(len(edges)):
        x_1 = []
        y_1 = []
        for j in range(len(edges[i])):
            x_1.append(points[edges[i][j]][0])
            y_1.append(points[edges[i][j]][1])
        plt.plot(x_1 , y_1 , color = 'blue')
        #plt.plot(x_1 , y_1)

    max_independent_set_length = max(len(subset) for subset in path)

    plt.text(0, 0, f'iteration:{iteration + 1} max_length = {max_independent_set_length}', family='fantasy',
             fontsize=12,
             style='italic', color='mediumvioletred')

    flag = 0
    for index in range(len(path)):
        if len(path[index]) == max(len(subset) for subset in path):
            flag = index

    x_2 = []
    y_2 = []

    for i in range(len(path[flag])):
        x_2.append(points[path[flag][i]][0])
        y_2.append(points[path[flag][i]][1])
    plt.scatter(x_2 , y_2 , color = 'red' , s = 100)
    print(path[flag])


def init_SRS_edges(little_class):
    afit = little_class('reqlf13')
    afit.read_support_id()
    afit.read_RTS_antenna_id()
    afit.read_time_of_visibility_window()
    afit.read_antenna_turnaround_time()
    afit.calculate_visibility_arcs_length()
    edges = []
    for i in tqdm.tqdm(range(afit.visibility_arcs_length) , desc = "processing"):
        for j in range(i+1 , afit.visibility_arcs_length):
            if afit.support_id_list[i] == afit.support_id_list[j]:
                edges.append([i,j])
            if afit.RTS_antenna_ID_list[i] == afit.RTS_antenna_ID_list[j] and \
                    afit.visibility_window[i][1] + afit.antenna_turnaround_time[i] > \
                    afit.visibility_window[j][0]:
                edges.append([i , j])
    with open('SRS_edges.txt', 'w') as fp:
        for i in range(len(edges)):
            fp.write(f'{edges[i][0]} {edges[i][1]}\n')
    return edges


