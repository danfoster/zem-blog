---
title: DIY Lights out Managment
category: sysadmin
tags: serial, lom, centos
---

# CentOS 7 Serial Console configuration.

Configure GRUB2 by adding the following lines to `/etc/default/grub`:

```
GRUB_TERMINAL="serial console"
GRUB_TERMINAL_OUTPUT="serial console"
GRUB_SERIAL_COMMAND="serial --speed=115200 --unit=0 --word=8 --parity=no --stop=1"
```

Then run `grub2-mkconfig -o /boot/grub2/grub.cfg` to rebuild the GRUB config. 
