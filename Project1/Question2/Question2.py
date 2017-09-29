#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''

import copy
import json
import sys
sys.path.append("..")
import Start
import BFS
import DFS
import ASTAR_MHT
import ASTAR_EUC

if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argument", i, sys.argv[i]
    print ('start initialize')
    f1 = open('data.js', 'w')
    # f1.write('hello boy!')
    dfs = DFS.DFS()
    size = 10
    start = Start.Start(size, 0.3)
    start.paint_random()
    start.print_matrix()
    # test map
    while dfs.dfs_route(start.get_matrix(), size)[0] == 0:
        start = Start.Start(size, 0.3)
        start.paint_random()
    map = copy.copy(start.get_matrix())
    data = dict()
    original = {"size": size, "map": map}# [[1,1,1],[1,1,1],[1,1,1]]}
    data["original"] = original
    # DFS
    result = dfs.dfs_route(start.get_matrix(), size)
    route = dfs.print_optimal(copy.deepcopy(map))
    # print result
    data["DFS"] = {"size": size, "map": route}
    # BFS
    bfs = BFS.BFS()
    result = bfs.bfs_init(start.get_matrix(), size)
    route = copy.deepcopy(map)
    for node in result[1]:
        route[node[0]][node[1]] = 2
    # for i in range(0,size):
    #     for j in range(0, size):
    #         print route[i][j],
    #     print '\n',
    data["BFS"] = {"size": size, "map": route}
    print result
    # A-MHT
    astar = ASTAR_MHT.ASTAR()
    result = astar.find_path(start.get_matrix(), size)
    route = copy.deepcopy(map)
    for node in result[1]:
        route[node[0]][node[1]] = 2
    data["MHT"] = {"size": size, "map": route}
    print result
    # A-Eud
    astar = ASTAR_EUC.ASTAR()
    result = astar.find_path(start.get_matrix(), size)
    route = copy.deepcopy(map)
    for node in result[1]:
        route[node[0]][node[1]] = 2
    data["EUC"] = {"size": size, "map": route}
    print result
    json = json.dumps(data)
    f1.write("var json_data = " + json + ";")
    f1.flush()
    f1.close()
    print "end"