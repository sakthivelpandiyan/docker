#!/bin/bash
# -----------------------------------------------------------------------------
# docker-ubuntu-sshd /start script
#
# Authors: Art567
# Updated: Sep 20th, 2015
# -----------------------------------------------------------------------------


# Run OpenSSH server in daemon mode
/sbin/service sshd start

#Run Weblogic Admin Servers
su - oracle -c "/u01/env.sh;/u01/oracle/createAndStartEmptyDomain.sh"
