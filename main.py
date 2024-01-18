from Program_1 import div
from Program_2 import interleave
import yaml
class test():
    def __init__(self):
        with open("config/config.yaml", 'r') as file:
            data_load = yaml.safe_load(file)
            print(data_load['n'])
            self.n = data_load['n']
            self.str1 = data_load['str1']
            self.str2 = data_load['str2']
if __name__=='__main__':
    obj= test()
    result= div(obj.n)
    var= list(result)
    assert var == [0, 35, 70]
    final = interleave(obj.str1, obj.str2)
    print (final)
    assert final == 'A1A2A3A4567'