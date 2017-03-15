#! /usr/bin/python
# coding:utf-8
try:
    import cmd2 as cmd
except ImportError:
    import cmd

class ui(cmd.Cmd):
    intro = ''
    def do_show(self):
        pass

    def do_guide(self):
        pass

    def do_select(self):
        '''Select by number/path/tag'''
        pass

    def do_run(self):
        pass

    def do_add(self):
        '''Add cases after select'''
        pass

    def do_remove(self):
        '''Remove cases after select'''
        pass

    def do_report(self): #design how to report
        ''''''
        pass

    def do_aslr(self):
        pass

    def do_attach(self):
        pass

    def do_q(self):
        '''Quit'''
        return True

    def do_info(self):
        '''Show info of cases'''



CSTEui = ui()

# delete unused command (make command list clear)
for attr in ['do_list', 'do_r', 'do_cmdenvironment', 'do_history', 'do_hi', 'do_save',
             'do_pause', 'do_ed', 'do_edit', 'do_EOF', 'do_eof', 'do_li', 'do_l', 'do_quit']:
    if hasattr(cmd.Cmd, attr): delattr(cmd.Cmd, attr)

CSTEui.cmdloop()