#!/usr/bin/env python3

import datetime
import subprocess

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

def main():
    print((color.green('%s') + ': this is color string test') % "green")
    try:
        output = subprocess.getoutput(
            'ls %s 2>&1'  
            % "./")
        print(output)
    except:
        print((color.red('%s') + ': failed') % "command")

if __name__ == '__main__':
    print(datetime.datetime.now().strftime('Start: %Y-%m-%d %H:%M:%S'))
    main()    
    print(datetime.datetime.now().strftime('End: %Y-%m-%d %H:%M:%S'))
