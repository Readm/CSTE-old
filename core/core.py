#! /usr/bin/python
# coding:utf-8
import os
import subprocess
import time
from script_tools import new_terminal_exit,new_terminal


class Case():
    '''Class of test cases
        path: abs path
        intro: introduction  (optional)
        run_vul: cmd
        run_exp: cmd         (optional)
        run_check: cmd
        compile: cmd
        aslr: bool
        dep: bool
        stack: bool          (optional)
        tag: tags
        release: bool
    '''
    def __init__(self,abs_path):
        try:
            self.path = abs_path
            self.load_info()
        except:
            print '[Error]: Load %s failed. Please check it.' % abs_path

    def load_info(self):
        '''Load info file'''
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
                setattr(self,k,v)

    def check_define(self,check_optional=False):
        '''Check info file and config file.'''
        # required
        for item in ['run_vul','run_check','compile','aslr','dep','tag','release']:
            if (not hasattr(self,item)) or (getattr(self,item)==None):
                print "[Error]: Failed in checking definition of %s, attribute %s not found." % (self.path, item)
                return False
        for item in ['exp_delay','check_delay']:
            if hasattr(self, item) and not isinstance(getattr(self,item), int):
                print "[Error]: Failed in checking definition of %s, attribute %s :type error." % (self.path, item)
                return False

        # optional
        if check_optional:
            for item in ['intro','run_exp','log']:
                if (not hasattr(self,item)):
                    print "[Warning]: Missing optional attribute %s, in %s." % (item,self.path)

        return True  # Succeed

    def run(self, attack=True, attach=False):
        if not self.check_define():
            print '[Error]: Failed check the info file. Stop.'
        with open(self.path+'/default.cfg','r') as default_f:
            lines = default_f.readlines()
            with open(self.path+'/run.cfg','w') as run_f:

                for line in lines:
                    if line.strip().lower().startswith('act'):
                        if attack : run_f.writelines(['act: attack'])
                        else: run_f.writelines(['act: normal'])
                    elif line.strip().lower().startswith('attach'):
                        if attach : run_f.writelines(['attach: yes'])
                        else: run_f.writelines(['act: no'])
                    else:
                        run_f.writelines([line])

        os.chdir(self.path)
        os.popen(new_terminal_exit(self.run_vul+' run.cfg'))

        if hasattr(self, 'run_exp'):
            if hasattr(self, 'exp_delay'):
                time.sleep(self.exp_delay)
            os.popen(new_terminal_exit(self.run_exp))



    def compile(self,dep=None,stack=None):  # TODO did compile finish? we may run it in current process to make sure.
        if hasattr(self, 'run_exp'):
            os.popen(new_terminal_exit(self.compile))


    def check(self):
        '''Return check answer.'''
        p = subprocess.Popen(self.run_check, stdout=subprocess.PIPE, shell= True)
        res = p.stdout.read().strip()
        return res


    def log(self):
        '''Return string in log file'''
        pass

    @property
    def tag(self):
        '''Return list of tags'''
        return []
        pass

    @property
    def release(self):
        '''Return True or False'''
        return

def list_cases(path):
    '''Find all cases in the path'''
    lst = []
    case_lst = []
    def find(path):
        if 'info' in os.listdir(path) and os.path.isfile(path+'/info'):
            lst.append(path)
        else:
            for sub_path in os.listdir(path):
                if not os.path.isfile(sub_path):
                    find(path+'/'+sub_path)
    find(path)
    for i in lst:
        case = Case(i)
        case_lst.append(case)
    return case_lst



#if __name__=='__main__':
    #pass
    #c = Case("/home/readm/CSTE/testcases/sample")
    #c.run()
    #c.check_define(check_optional=True)
    #print list_cases('/home/readm/CSTE/testcases')