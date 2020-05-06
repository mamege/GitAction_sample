#!/usr/bin/env python3

import datetime
import subprocess
from subprocess import Popen

class color:
    def _wrap_with(code):
        def inner(text, bold=False):
            c = code
            if bold:
                c = "1;%s" % c
            return "\033[%sm%s\033[0m" % (c, text)
        return inner  
    red     = _wrap_with('31')
    green   = _wrap_with('32')
    yellow  = _wrap_with('33')
    blue    = _wrap_with('34')
    magenta = _wrap_with('35')
    cyan    = _wrap_with('36')
    white   = _wrap_with('37')

class Nqsv:
    def __init__(self):
        self.times=0
    
    def qstat(self):
        if (self.times < 3):
            self.times += 1
            return self.running()
        else:
            self.times = 0
            return self.done()
        
    def running(self):
        string="""RequestID       ReqName  UserName Queue     Pri STT S   Memory      CPU   Elapse R H M Jobs
--------------- -------- -------- -------- ---- --- - -------- -------- -------- - - - ----
444211.nqsv     SMI_Qsub kashino  fpga        0 RUN -  925.64M     0.97       23 N Y Y    1"""
        return string
    def done(self):
        string=""
        return string


def testQstat():
    nqsv = Nqsv()
    for i in range(4):
        print(nqsv.qstat())



def execCommand():
    try:
        mock = "Request 444204.nqsv submitted to queue: fpga."
        p = Popen(["echo",mock], 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, errors = p.communicate()
        print(output)
    except:
        print((color.red('%s') + ': failed') % "command")
    return output

def main():
    print((color.green('%s') + ': this is color string test') % "green")
    execCommand()
    testQstat()



if __name__ == '__main__':
    print(datetime.datetime.now().strftime('Start: %Y-%m-%d %H:%M:%S'))
    main()    
    print(datetime.datetime.now().strftime('End: %Y-%m-%d %H:%M:%S'))
