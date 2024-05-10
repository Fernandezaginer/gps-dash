
# Utilities to convert data str to dictionaries:
# AFM
# LEEM 2024


import ast
import copy


# Reconvert string to dicionary list:
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



# Method sort elements of a list at first:
def sort_list(original_list, elements_at_beginning):
    result_list = copy.deepcopy(original_list)
    for i in elements_at_beginning:
        if i in original_list:
            result_list.remove(i)
            result_list.insert(0, i)
    return result_list



# Class to get available parameters from a dictionary
class Parameter_processor():


    # Init class:
    def __init__(self, dic_available):
        self.available_dic = dic_available
        setattr(self, "none", [])
        for key, value in dic_available.items():
            setattr(self, str(value), [])


    # Read available parameters:
    def read_available_param(self, dic):
        if "pt" in list(dic.keys()):

            # Get and update parameters available
            pt = dic["pt"]
            new_param = list(dic.keys())
            new_param.remove("pt")
            if "ssrc_identifier" in new_param:
                new_param.remove("ssrc_identifier")
            old_param = getattr(self, str(pt))
            old_param.extend(new_param)
            old_param = list(dict.fromkeys(old_param))

            # Sort parameters
            if str(pt) == "201.0":
                old_param = sort_list(old_param, ["ssrc_cum_num", "ssrc_fraction", "ssrc_jitter", "rtt"])
            if str(pt) == "200.0":
                old_param = sort_list(old_param, ["sender_packetcount", "sender_octetcount"])

            # Update specific pt name:
            setattr(self, str(pt), old_param)

            # Update non pt filter:
            all_param = getattr(self, "none")
            all_param.extend(old_param)
            all_param = sort_list(all_param, ["ssrc_cum_num", "ssrc_fraction", "ssrc_jitter", "rtt", "sender_packetcount", "sender_octetcount"])
            all_param = list(dict.fromkeys(all_param))
            setattr(self, "none", all_param)


    # Get parameters according to the filter key:
    def get_param(self, key):
        if getattr(self, str(key)) == []:
            return ["receiver_timestamp"]
        else:
            return getattr(self, str(key))



