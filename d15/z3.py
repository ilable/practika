from z1 import parse_cdp_neighbors
from draw_network_graph import *

q1 = parse_cdp_neighbors('sh_cdp_n_r1.txt')
q2 = parse_cdp_neighbors('sh_cdp_n_r2.txt')
q3 = parse_cdp_neighbors('sh_cdp_n_r3.txt')
q4 = parse_cdp_neighbors('sh_cdp_n_sw1.txt')
q = {}
q.update(q1)
q.update(q2)
q.update(q3)
q.update(q4)

s = {}
lists = []

for key, value in q.items():
    dic = {}
    key_str = ''.join(list(key))
    value_str = ''.join(list(value))
    if key_str not in ''.join(lists) or value_str not in ''.join(lists):
        lists.append(key_str)
        lists.append(value_str)
        s[key] = value
    else:
        pass
draw_topology(s)