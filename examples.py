#WEBSERVER

[root@localhost ~]# docker run -d  nginx
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
2a72cbf407d6: Already exists
fefa2faca81f: Pull complete
080aeede8114: Pull complete
Digest: sha256:ccdb5fdf47709493f9fc5af32478c0d86b3cbee0c306e3f04a0d3e640a50ea2d
Status: Downloaded newer image for nginx:latest
766c51e1759dac794de1034e19939a26a96a8d7748085bffd784fb84b1c8cc82

[root@localhost ~]# docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
766c51e1759d        nginx               "nginx -g 'daemon of…"   39 seconds ago      Up 38 seconds       80/tcp              objective_kowalevski
[root@localhost ~]#
[root@localhost ~]# docker container inspect -f {{.NetworkSettings.IPAddress}} 766c51e1759d
172.17.0.2
[root@localhost ~]# curl http://172.17.0.2
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
[root@localhost ~]#


-------------------------------------------------------------------------------------
#PORT FORWARDING
[root@localhost ~]# docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
766c51e1759d        nginx               "nginx -g 'daemon of…"   27 minutes ago      Up 27 minutes       80/tcp              objective_kowalevski
[root@localhost ~]# docker stop 766c51e1759d
766c51e1759d
[root@localhost ~]# docker rm 766c51e1759d
766c51e1759d
[root@localhost ~]# docker run -d -p 8000:80  nginx
cb03b34a1fed0bcc9b2405e8f97d5791546c3a813e6929f085f22ed6926488a2
[root@localhost ~]# docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
cb03b34a1fed        nginx               "nginx -g 'daemon of…"   9 seconds ago       Up 8 seconds        0.0.0.0:8000->80/tcp   agitated_edison
[root@localhost ~]# docker container inspect -f {{.NetworkSettings.IPAddress}} cb03b34a1fed
172.17.0.2
[root@localhost ~]# curl http://172.17.0.2
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
[root@localhost ~]# ifconfig ens33 |head -2
ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 203.0.113.129  netmask 255.255.255.0  broadcast 203.0.113.255
[root@localhost ~]# curl http://203.0.113.129:8000/
<!DOCTYPE html>
[root@localhost ~]# iptables -L -t nat |grep -i 'tcp dpt:irdmi'
DNAT       tcp  --  anywhere             anywhere             tcp dpt:irdmi to:172.17.0.2:80
[root@localhost ~]#
-------------------------------------------------------------------------------------
Creating image using Dockerfile

[root@localhost vimImage]# docker build -t sakthi/vimeditor .
Sending build context to Docker daemon  2.048kB
Step 1/4 : FROM ubuntu:16.04
16.04: Pulling from library/ubuntu
Digest: sha256:e348fbbea0e0a0e73ab0370de151e7800684445c509d46195aef73e090a49bd6
Status: Downloaded newer image for ubuntu:16.04
 ---> f975c5035748
Step 2/4 : MAINTAINER Ponraj, Sakthivel Pandiyan <sakthi.cyril@gmail.com>
 ---> Running in b8e99b5e08d5
Removing intermediate container b8e99b5e08d5
 ---> 9394edd0dbbf
Step 3/4 : RUN apt-get update && apt-get -y install vim
 ---> Running in 700553be93dd
Get:1 http://archive.ubuntu.com/ubuntu xenial InRelease [247 kB]
Get:2 http://security.ubuntu.com/ubuntu xenial-security InRelease [102 kB]
.
.
Get:19 http://archive.ubuntu.com/ubuntu xenial-updates/multiverse amd64 Packages [18.5 kB]
Get:20 http://archive.ubuntu.com/ubuntu xenial-backports/main amd64 Packages [5153 B]
Get:21 http://archive.ubuntu.com/ubuntu xenial-backports/universe amd64 Packages [7734 B]
Fetched 25.1 MB in 1min 59s (209 kB/s)
Reading package lists...
Reading package lists...
Building dependency tree...
Reading state information...
The following additional packages will be installed:
  file libexpat1 libgpm2 libmagic1 libmpdec2 libpython3.5 libpython3.5-minimal
  libpython3.5-stdlib libsqlite3-0 libssl1.0.0 mime-support vim-common
  vim-runtime
Suggested packages:
  gpm ctags vim-doc vim-scripts vim-gnome-py2 | vim-gtk-py2 | vim-gtk3-py2
  | vim-athena-py2 | vim-nox-py2
The following NEW packages will be installed:
  file libexpat1 libgpm2 libmagic1 libmpdec2 libpython3.5 libpython3.5-minimal
  libpython3.5-stdlib libsqlite3-0 libssl1.0.0 mime-support vim vim-common
  vim-runtime
0 upgraded, 14 newly installed, 0 to remove and 9 not upgraded.
Need to get 12.2 MB of archives.
After this operation, 58.3 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu xenial/main amd64 libgpm2 amd64 1.20.4-6.1 [16.5 kB]
Get:2 http://archive.ubuntu.com/ubuntu xenial/main amd64 libmagic1 amd64 1:5.25-2ubuntu1 [216 kB]
Get:3 http://archive.ubuntu.com/ubuntu xenial/main amd64 file amd64 1:5.25-2ubuntu1 [21.2 kB]
Get:4 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libexpat1 amd64 2.1.0-7ubuntu0.16.04.3 [71.2 kB]
Get:5 http://archive.ubuntu.com/ubuntu xenial/main amd64 libmpdec2 amd64 2.4.2-1 [82.6 kB]
Get:6 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libssl1.0.0 amd64 1.0.2g-1ubuntu4.11 [1082 kB]
Get:7 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libpython3.5-minimal amd64 3.5.2-2ubuntu0~16.04.4 [523 kB]
Get:8 http://archive.ubuntu.com/ubuntu xenial/main amd64 mime-support all 3.59ubuntu1 [31.0 kB]
Get:9 http://archive.ubuntu.com/ubuntu xenial/main amd64 libsqlite3-0 amd64 3.11.0-1ubuntu1 [396 kB]
Get:10 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libpython3.5-stdlib amd64 3.5.2-2ubuntu0~16.04.4 [2132 kB]
Get:11 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 vim-common amd64 2:7.4.1689-3ubuntu1.2 [103 kB]
Get:12 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libpython3.5 amd64 3.5.2-2ubuntu0~16.04.4 [1360 kB]
Get:13 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 vim-runtime all 2:7.4.1689-3ubuntu1.2 [5164 kB]
Get:14 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 vim amd64 2:7.4.1689-3ubuntu1.2 [1036 kB]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 12.2 MB in 1min 14s (164 kB/s)
Selecting previously unselected package libgpm2:amd64.
(Reading database ... 4768 files and directories currently installed.)
....
Setting up libgpm2:amd64 (1.20.4-6.1) ...
Setting up libmagic1:amd64 (1:5.25-2ubuntu1) ...
Setting up file (1:5.25-2ubuntu1) ...
Setting up libexpat1:amd64 (2.1.0-7ubuntu0.16.04.3) ...
Setting up libmpdec2:amd64 (2.4.2-1) ...
Setting up libssl1.0.0:amd64 (1.0.2g-1ubuntu4.11) ...
debconf: unable to initialize frontend: Dialog
debconf: (TERM is not set, so the dialog frontend is not usable.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.22.1 /usr/local/share/perl/5.22.1 /usr/lib/x86_64-linux-gnu/perl5/5.22 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl/5.22 /usr/share/perl/5.22 /usr/local/lib/site_perl /usr/lib/x86_64-linux-gnu/perl-base .) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7.)
debconf: falling back to frontend: Teletype
Setting up libpython3.5-minimal:amd64 (3.5.2-2ubuntu0~16.04.4) ...
Setting up mime-support (3.59ubuntu1) ...
Setting up libsqlite3-0:amd64 (3.11.0-1ubuntu1) ...
Setting up libpython3.5-stdlib:amd64 (3.5.2-2ubuntu0~16.04.4) ...
Setting up vim-common (2:7.4.1689-3ubuntu1.2) ...
Setting up libpython3.5:amd64 (3.5.2-2ubuntu0~16.04.4) ...
Setting up vim-runtime (2:7.4.1689-3ubuntu1.2) ...
Setting up vim (2:7.4.1689-3ubuntu1.2) ...
update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/vim (vim) in auto mode
update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/vimdiff (vimdiff) in auto mode
update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/rvim (rvim) in auto mode
update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/rview (rview) in auto mode
update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/vi (vi) in auto mode
update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/view (view) in auto mode
update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/ex (ex) in auto mode
update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/editor (editor) in auto mode
Processing triggers for libc-bin (2.23-0ubuntu10) ...
Removing intermediate container 700553be93dd
 ---> fa53d6cb9845
Step 4/4 : CMD vim
 ---> Running in 7a951e918fc8
Removing intermediate container 7a951e918fc8
 ---> bf0855dbdfca
Successfully built bf0855dbdfca
Successfully tagged sakthi/vimeditor:latest
[root@localhost ~]# docker run -it -d sakthi/vimeditor
c5997016fd2d4fc9a5a0a06e50ab7b18239284984c05773fdf068e3e1059121e
[root@localhost ~]# docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
c5997016fd2d        sakthi/vimeditor    "/bin/sh -c vim"         25 seconds ago      Up 24 seconds                              mystifying_proskuriakova
[root@localhost ~]# docker container inspect -f {{.NetworkSettings.IPAddress}} c599
172.17.0.4
[root@localhost ~]# docker exec -it c599 /bin/bash
root@c5997016fd2d:/# which vim
/usr/bin/vim
root@c5997016fd2d:/# vim /tmp/test.txt
----------------------------------------------------------------------------------------------------------
MySQL/WordPress

[root@localhost data]# docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql
61d86bac25a3ee8f3f1937fbd4373d7f5cd919f609ab9ddbf01c47a53f07c5de

[root@localhost data]# docker run --name some-wordpress --link some-mysql:mysql -p 8080:80 -d wordpress
Unable to find image 'wordpress:latest' locally
latest: Pulling from library/wordpress
2a72cbf407d6: Already exists
273cd543cb15: Pull complete
ec5ac8875de7: Pull complete
9106e19b56c1: Pull complete
ee2f70ac7c7d: Pull complete
7257ad6985e8: Pull complete
18f5c2055da2: Pull complete
85293a6fdd80: Pull complete
9e797eeb0c14: Pull complete
09b55b88e646: Pull complete
2cd18314711e: Pull complete
88b610931a5f: Pull complete
b90052b881e9: Pull complete
36317e1f49af: Pull complete
6dbef1d5801a: Pull complete
f98e14d31e08: Pull complete
dbc1b2b39588: Pull complete
280991283b71: Pull complete
5c4360fbc4f6: Pull complete
0623bccc9390: Pull complete
Digest: sha256:b6189dc683704a5011f64d71166f3e712d64816d96750ba4636bcbf137c00903
Status: Downloaded newer image for wordpress:latest
e49c1a6a60e6e40e6a88a9a0e3b4646b45a93750af1aea6a94873f244bd89921
----------------------------------------------------------------------------------------------------------

Sample custom images

[root@localhost ubuntu-ansible]# cat Dockerfile
FROM ubuntu:16.04

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
#RUN echo 'root:root' | chpasswd
RUN echo 'jenkins:jenkins' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
RUN mkdir -p /root/.ssh
COPY authorized_keys /root/.ssh/authorized_keys          

EXPOSE 22
EXPOSE 80
CMD ["/usr/sbin/sshd", "-D"]
[root@localhost ubuntu-ansible]# ls -ltr
total 8
-rw-r--r--. 1 root root 627 Apr  2 09:02 Dockerfile
-rw-r--r--. 1 root root 408 Apr  2 09:03 authorized_keys
[root@localhost ubuntu-ansible]# docker build -t sakthivel/dockerbase .
Sending build context to Docker daemon  54.27kB
Step 1/13 : FROM ubuntu:16.04
 ---> f975c5035748
Step 2/13 : RUN apt-get update && apt-get install -y openssh-server
 ---> Running in 4fce40f10e54
Get:1 http://archive.ubuntu.com/ubuntu xenial InRelease [247 kB]
Get:2 http://security.ubuntu.com/ubuntu xenial-security InRelease [102 kB]
Get:3 http://security.ubuntu.com/ubuntu xenial-security/universe Sources [77.2 kB]
....
Fetched 25.1 MB in 2min 25s (173 kB/s)
Reading package lists...
Reading package lists...
Building dependency tree...
Reading state information...
The following additional packages will be installed:
  ca-certificates dh-python file krb5-locales libbsd0 libedit2 libexpat1
  ...........
  openssh-client openssh-server openssh-sftp-server openssl python3
  python3-chardet python3-minimal python3-pkg-resources python3-requests
  python3-six python3-urllib3 python3.5 python3.5-minimal ssh-import-id tcpd
  wget xauth
0 upgraded, 47 newly installed, 0 to remove and 9 not upgraded.
Need to get 10.5 MB of archives.
After this operation, 55.1 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libssl1.0.0 amd64 1.0.2g-1ubuntu4.11 [1082 kB]
Get:2 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libpython3.5-minimal amd64 3.5.2-2ubuntu0~16.04.4 [523 kB]
.................
Get:47 http://archive.ubuntu.com/ubuntu xenial/main amd64 ssh-import-id all 5.5-0ubuntu1 [10.2 kB]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 10.5 MB in 54s (193 kB/s)
Selecting previously unselected package libssl1.0.0:amd64.
(Reading database ... 4768 files and directories currently installed.)
Preparing to unpack .../libssl1.0.0_1.0.2g-1ubuntu4.11_amd64.deb ...
Unpacking libssl1.0.0:amd64 (1.0.2g-1ubuntu4.11) ...
...
Setting up mime-support (3.59ubuntu1) ...
Setting up libmpdec2:amd64 (2.4.2-1) ...
...............
Setting up openssh-server (1:7.2p2-4ubuntu2.4) ...
debconf: unable to initialize frontend: Dialog
debconf: (TERM is not set, so the dialog frontend is not usable.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.22.1 /usr/local/share/perl/5.22.1 /usr/lib/x86_64-linux-gnu/perl5/5.22 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl/5.22 /usr/share/perl/5.22 /usr/local/lib/site_perl /usr/lib/x86_64-linux-gnu/perl-base .) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7.)
debconf: falling back to frontend: Teletype
Creating SSH2 RSA key; this may take some time ...
2048 SHA256:QSElQlvmW3go0AwyRDbdd2fcPsp8Zx9S4rCZ+EjieOM root@4fce40f10e54 (RSA)
Creating SSH2 DSA key; this may take some time ...
1024 SHA256:RC8F5mRYM9tLnSaOwl/bClLiwUtrwiv35RG9wbEc0gk root@4fce40f10e54 (DSA)
Creating SSH2 ECDSA key; this may take some time ...
256 SHA256:Nqtq+4IEbN7nNREP/GDtTH/nCKO/zWvdUnQ7NaYsqJ4 root@4fce40f10e54 (ECDSA)
Creating SSH2 ED25519 key; this may take some time ...
256 SHA256:ALwpY5f2ZnX/gv29ccDDrw7VmahaGqA4z46Sd0vjDIM root@4fce40f10e54 (ED25519)
invoke-rc.d: could not determine current runlevel
invoke-rc.d: policy-rc.d denied execution of start.
Setting up tcpd (7.6.q-25) ...
Setting up dh-python (2.20151103ubuntu1.1) ...
Setting up python3 (3.5.1-3) ...
running python rtupdate hooks for python3.5...
running python post-rtupdate hooks for python3.5...
Setting up python3-pkg-resources (20.7.0-1) ...
Setting up python3-chardet (2.3.0-2) ...
Setting up python3-six (1.10.0-3) ...
Setting up python3-urllib3 (1.13.1-2ubuntu0.16.04.1) ...
Setting up python3-requests (2.9.1-3) ...
Setting up ssh-import-id (5.5-0ubuntu1) ...
Processing triggers for libc-bin (2.23-0ubuntu10) ...
Processing triggers for ca-certificates (20170717~16.04.1) ...
Updating certificates in /etc/ssl/certs...
148 added, 0 removed; done.
Running hooks in /etc/ca-certificates/update.d...
done.
Processing triggers for systemd (229-4ubuntu21.1) ...
Removing intermediate container 4fce40f10e54
 ---> 67e634d5d43c
Step 3/13 : RUN mkdir /var/run/sshd
 ---> Running in 22fc05074c57
Removing intermediate container 22fc05074c57
 ---> 118c5b4636d1
Step 4/13 : RUN echo 'root:root' | chpasswd
 ---> Running in 1b43750e03fa
Removing intermediate container 1b43750e03fa
 ---> bd74e33d907d
Step 5/13 : RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
 ---> Running in 7df711202b41
Removing intermediate container 7df711202b41
 ---> 337e31814450
Step 6/13 : RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
 ---> Running in 1bc9693a987c
Removing intermediate container 1bc9693a987c
 ---> 5a5d9c3e384c
Step 7/13 : ENV NOTVISIBLE "in users profile"
 ---> Running in d61672c654dc
Removing intermediate container d61672c654dc
 ---> dc473d523651
Step 8/13 : RUN echo "export VISIBLE=now" >> /etc/profile
 ---> Running in 6acdc56dc8dc
Removing intermediate container 6acdc56dc8dc
 ---> 4f784ec229fa
Step 9/13 : RUN mkdir -p /root/.ssh
 ---> Running in f57c31ae3294
Removing intermediate container f57c31ae3294
 ---> ebd515de5089
Step 10/13 : COPY authorized_keys /root/.ssh/authorized_keys
 ---> fe4ea922720e
Step 11/13 : EXPOSE 22
 ---> Running in 2db8efab9fc5
Removing intermediate container 2db8efab9fc5
 ---> ffba61e9c576
Step 12/13 : EXPOSE 80
 ---> Running in 24b97d65af71
Removing intermediate container 24b97d65af71
 ---> 7b018173174d
Step 13/13 : CMD ["/usr/sbin/sshd", "-D"]
 ---> Running in d154533baa2e
Removing intermediate container d154533baa2e
 ---> e4d4b7944650
Successfully built e4d4b7944650
Successfully tagged sakthivel/dockerbase:latest
        

[root@localhost .ssh]# docker run -d -p 2200:22 -p 9080:80  sakthivel/dockerbase
7483e6b79f7391f603bc8972d7f78419ad5fe4c43569ee9362b0b81f9161ffa0
[root@localhost .ssh]# docker container inspect -f {{.NetworkSettings.IPAddress}} 7483
172.17.0.5
[root@localhost .ssh]# docker container ls
CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS              PORTS                                        NAMES
7483e6b79f73        sakthivel/dockerbase   "/usr/sbin/sshd -D"      2 minutes ago       Up 2 minutes        0.0.0.0:2200->22/tcp, 0.0.0.0:9080->80/tcp   competent_brown
c5997016fd2d        sakthi/vimeditor       "/bin/sh -c vim"         17 hours ago        Up 17 hours                                                      mystifying_proskuriakova
e49c1a6a60e6        wordpress              "docker-entrypoint.s…"   17 hours ago        Up 17 hours         0.0.0.0:8080->80/tcp                         some-wordpress
61d86bac25a3        mysql                  "docker-entrypoint.s…"   17 hours ago        Up 17 hours         3306/tcp                                     some-mysql
[root@localhost .ssh]#  docker exec -it 670c /bin/bash
Error: No such container: 670c
[root@localhost .ssh]#  docker exec -it 7483 /bin/bash
root@7483e6b79f73:/# df -h /
Filesystem      Size  Used Avail Use% Mounted on
overlay          17G   13G  4.6G  73% /
[root@localhost .ssh]# telnet `hostname` 2200
Trying ::1...
Connected to localhost.localdomain.
Escape character is '^]'.
SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.4
^C^C^C^C
Connection closed by foreign host.
[root@localhost ~]# ssh 203.0.113.129 -p 2200
The authenticity of host '[203.0.113.129]:2200 ([203.0.113.129]:2200)' can't be established.
ECDSA key fingerprint is SHA256:Nqtq+4IEbN7nNREP/GDtTH/nCKO/zWvdUnQ7NaYsqJ4.
ECDSA key fingerprint is MD5:26:46:e8:dd:30:f9:b6:31:67:a0:10:b0:7b:0e:2b:f9.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '[203.0.113.129]:2200' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 16.04.4 LTS (GNU/Linux 3.10.0-693.el7.x86_64 x86_64)
root@7483e6b79f73:~#

[trainer@localhost ~]$ telnet `hostname` 9080
Trying ::1...
Connected to localhost.localdomain.
Escape character is '^]'.
Connection closed by foreign host.
[trainer@localhost ~]$






