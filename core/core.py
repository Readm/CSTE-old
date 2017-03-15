#! /usr/bin/python
# coding:utf-8

class Case():
    '''Class of test cases
        path: abs path
        intro: introduction  (optional)
        run_vul: cmd
        run_exp: cmd         (optional)
        check: cmd
        compile: cmd
        aslr: bool
        dep: bool
        stack: bool          (optional)
        tag: tags
        release: bool
    '''
    def __init__(self,abs_path):
        self.path = abs_path
        self.load_info()

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
        for item in ['run_vul','check','compile','aslr','dep','tag','release']:
            if (not hasattr(self,item)) or (getattr(self,item)==None):
                print "[Error]: Failed in checking definition of %s, attribute %s not found." % (self.path, item)
                return False
        # optional
        if check_optional:
            for item in ['intro','run_exp']:
                if (not hasattr(self,item)):
                    print "[Warning]: Missing optional attribute %s, in %s." % (item,self.path)

        return True  # Succeed

    def run(self):
        pass

    def run_vul(self):
        pass

    def run_exp(self):
        pass

    def compile(self,dep=None,stack=None):
        pass

    def check(self):
        '''Return (bool,info), bool for success or not.'''
        pass

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


if __name__=='__main__':
    c = Case("/home/readm/CSTE/testcases/sample")
    c.load_info()
    c.check_define(check_optional=True)