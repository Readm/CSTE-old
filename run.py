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




CSTEui = ui()

# delete unused command (make command list clear)
for attr in ['do_list', 'do_r', 'do_cmdenvironment', 'do_history', 'do_hi', 'do_save',
             'do_pause', 'do_ed', 'do_edit', 'do_EOF', 'do_eof', 'do_li', 'do_l', 'do_quit']:
    if hasattr(cmd.Cmd, attr): delattr(cmd.Cmd, attr)

CSTEui.cmdloop()