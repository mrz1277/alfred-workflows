#!/usr/bin/python
# encoding: utf-8

import sys
import subprocess
import re

from workflow import Workflow, web

def main(wf):

    vbox = "VBoxManage" if os.path.exists("VBoxManage") else "/usr/local/bin/VBoxManage"

    output = subprocess.check_output([vbox, "list", "vms"])

    for line in output.splitlines():
        matches = re.match(r'\"(.*)\" \{(.*)\}', line, re.M)

        vm_info = subprocess.check_output([vbox, "showvminfo", matches.group(2)])
        if "Genymotion" in vm_info:
            tokens = matches.group(1).split(' - ')

            wf.add_item(
                title = tokens.pop(0),
                subtitle = ' - '.join(str(x) for x in tokens) if len(tokens) > 0 else None,
                arg = matches.group(2),
                valid = True,
                uid = matches.group(2)
            )

    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))