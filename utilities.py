
# Utilities to convert data str to dictionaries:
# AFM
# LEEM 2024


import ast
import copy
import numpy as np



class Filtro_DLPF:

    def __init__(self, k):
        self.value = 0
        self.k = k

    def get_value(self, value):
        out_value = self.value*(1-self.k) + value*self.k
        self.value = out_value
        return out_value





# BUFFER PORT: Reconvert string to dicionary list:
def decode_str(text):
    starts_dic = [n for n in range(len(text)) if text.find('{', n) == n]
    ends_dic = [n for n in range(len(text)) if text.find('}', n) == n]
    dic_lis = []
    if len(starts_dic) != len(ends_dic):
        raise "Error parsing the data"
    for i in range(len(starts_dic)):
        dict_aux = ast.literal_eval(text[starts_dic[i]:(ends_dic[i]+1)])
        for k, v in dict_aux.items():
            try:
                dict_aux[k] = float(v)
            except:
                dict_aux[k] = v
        dic_lis.append(dict_aux)
    return dic_lis



# map_colors(2000, 100, 3000, "#00FFFF", "#FF0000")
def map_colors(value, value_min, value_max, color_min, color_max):
  cm = (int(color_min[1:3], 16), int(color_min[3:5], 16), int(color_min[5:7], 16))
  cM = (int(color_max[1:3], 16), int(color_max[3:5], 16), int(color_max[5:7], 16))
  i = [value_min, value_max]
  color_out = (np.interp(value, i, [cm[0], cM[0]]), np.interp(value, i, [cm[1], cM[1]]), np.interp(value, i, [cm[2], cM[2]]))
  color_out = [int(color_out[0]), int(color_out[1]), int(color_out[2])]
  return "#" + ''.join('{:02X}'.format(a) for a in color_out)



