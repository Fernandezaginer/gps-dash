
# Utilities to convert data str to dictionaries:
# AFM
# LEEM 2024


import ast
import copy


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






