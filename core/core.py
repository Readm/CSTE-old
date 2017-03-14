#! /usr/bin/python
# coding:utf-8

class Case():
    '''Class of test cases
        path: abs path
        run_vul: cmd
        run_exp: cmd
        check: cmd
        compile: cmd
        aslr: bool
        dep: bool
        stack: bool
    '''
    def __init__(self,abs_path):
        self.path = abs_path

    def load_info(self):
        with open (self.path+'/info','r') as f:
            lines = f.readlines()
            k_v = {}
            # read all
            for line in lines:
                line = line.strip().split('#',1)[0]
                if line :
                    [k,v] =line.split(':',1)
                    k_v[k.strip()] = v.strip()
            # bool convert
            for item in ['aslr','dep','stack','release']:
                if k_v[item].lower() in ['on','yes']:
                    k_v[item]=True
                elif k_v[item].lower() in ['off','no']:
                    k_v[item]=False
                else:
                    k_v[item]=None
            # assignment
            for (k,v) in k_v.items():
                print k,v





if __name__=='__main__':
    c = Case("/home/readm/CSTE/testcases/sample")
    c.load_info()