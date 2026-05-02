<p align="center">
  <img src=".github/media/sheyald.png"></a>
</p>

<table align="center" style="border-collapse: collapse; border: none;">
  <tr align="center">
    <td style="padding: 0 15px;">
      <a href="https://es.wikipedia.org/wiki/LinuxCommands" title="Wikipedia"><img src=".github/media/icons/wikipedia.png" width="28"></a>
    </td>
    <td style="padding: 0 15px;">
      <a href="http://linuxcommands.wikidot.com/" title="Wikidot"><img src=".github/media/icons/wikidot.png" width="28"></a>
    </td>
    <td style="padding: 0 15px;">
      <a href="https://nisamov.github.io/LinuxCommands/" title="GitHub Pages"><img src=".github/media/icons/github.png" width="28"></a>
    </td>
    <td style="padding: 0 15px;">
      <a href="https://github.com/nisamov/LinuxCommands/blob/main/docs/commands.json" title="JSON Database"><img src=".github/media/icons/json.png" width="28" alt="JSON"></a>
    </td>
    <td style="padding: 0 15px;">
      <a href="https://nisamov.github.io/LinuxCommands/contributors" title="Contribuciones"><img src=".github/media/icons/contributions.png" width="28" alt="Contribuciones"></a>
    </td>
    <!--
    <td style="padding: 0 15px;">
      <a href="https://hikarune.online" title="Proyectos Recomendados"><img src=".github/media/icons/hikarune.ico" width="28" alt="Otros Proyectos"></a>
    </td>
    -->
  </tr>
  <tr align="center">
    <td><small><b><a href="https://nisamov.github.io/LinuxCommands/contributors" title="Contribuciones">Wikipedia</a></b></small></td>
    <td><small><b><a href="http://linuxcommands.wikidot.com/" title="Wikidot">Wikidot</a></b></small></td>
    <td><small><b><a href="https://nisamov.github.io/LinuxCommands/" title="GitHub Pages">Git Pages</a></b></small></td>
    <td><small><b><a href="https://github.com/nisamov/LinuxCommands/blob/main/docs/commands.json" title="JSON Database">JSON DB</a></b></small></td>
    <td><small><b><a href="https://nisamov.github.io/LinuxCommands/contributors" title="Contribuciones">Aports</a></b></small></td>
    <!--
    <td><small><b><a href="https://hikarune.online" title="Proyectos Recomendados">New Proj</a></b></small></td>
    -->
    <!--Proyectos nuevo [publicidad]-->
  </tr>
</table>

---

# LinuxCommands
[![Last commit](https://img.shields.io/github/last-commit/Nisamov/LinuxCommands?style=flat-square&color=000000&labelColor=ffffff&label=ultima-actualizacion)](https://github.com/Nisamov/LinuxCommands/commits)[![License](https://img.shields.io/github/license/Nisamov/LinuxCommands?style=flat-square&color=000000&labelColor=ffffff&label=licencia)](LICENSE)[![Visits](https://img.shields.io/endpoint?url=https://hits.dwyl.com/Nisamov/LinuxCommands.json&style=flat-square&color=000000&labelColor=ffffff&label=visitas)](https://github.com/Nisamov/LinuxCommands)

### Estructura y referencia para documentar comandos y servicios en Linux

LinuxCommands nació como una recopilación de apuntes personales para organizar y entender mejor distintos comandos, scripts y servicios en Linux.

[Más información sobre los orígenes del repositorio](.github/INFO.md).

---
<details open>
<summary><strong>• OBJETIVOS DEL PORYECTO</strong></summary>
<h1>Objetivos del proyecto</h1>

- Proporcionar un formato claro y reutilizable para documentar comandos y servicios de Linux.
- Facilitar una documentación legible para humanos y mantenible a largo plazo.
- Reducir duplicación, ambigüedad y variaciones innecesarias entre repositorios.
- Servir como referencia práctica para administradores de sistemas, desarrolladores y equipos técnicos.
</details>

---
<details open>
<summary><strong>• ESTRUCTURA DEL PROYECTO</strong></summary>
<h1>Estructura del proyecto</h1>

La organización del repositorio está pensada para facilitar la navegación y el crecimiento progresivo del contenido:

<!-- AUTO-GENERATED-INDEX:START -->
- [host_services](/host_services)
- [host_shared_storage](/host_shared_storage)
- [host_web_services](/host_web_services)
- [local_filesystem](/local_filesystem)
- [local_group](/local_group)
- [local_linux_fundamentals](/local_linux_fundamentals)
- [local_miscellaneous](/local_miscellaneous)
- [local_network](/local_network)
- [local_permissions](/local_permissions)
- [local_process](/local_process)
- [local_scripts](/local_scripts)
- [local_security](/local_security)
- [local_services](/local_services)
- [local_software](/local_software)
- [local_storage](/local_storage)
- [local_system_data](/local_system_data)
- [local_users](/local_users)
<!-- AUTO-GENERATED-INDEX:END -->

<details>
  <summary id="estrucutra_completa">Estructura completa del repositorio</summary>
  <pre><code>

<!-- AUTO-GENERATED-TREE:START -->
<pre><code>
LinuxCommands
├── .github
│   ├── ISSUE_TEMPLATE
│   │   ├── hallazgo-crítico.md
│   │   └── solicitud-de-implementación.md
│   ├── media
│   │   ├── icons
│   │   │   ├── contributions.png
│   │   │   ├── github.png
│   │   │   ├── hikarune.ico
│   │   │   ├── json.png
│   │   │   ├── wikidot.png
│   │   │   └── wikipedia.png
│   │   ├── OldFormat.png
│   │   ├── released_DE.png
│   │   ├── released_ENG.png
│   │   ├── released_ESP.png
│   │   ├── released_FR.png
│   │   ├── released_JA.png
│   │   ├── released_KO.png
│   │   ├── released_PT.png
│   │   ├── released_RU.png
│   │   ├── released_ZH.png
│   │   └── sheyald.png
│   ├── origins
│   │   ├── Directorios.txt
│   │   ├── LinuxCommandsModel.md
│   │   └── LinuxCommandsOrigen.md
│   ├── scripts
│   │   ├── build_commands_db.py
│   │   ├── generate_readme_index.py
│   │   ├── translate_adoc.py
│   │   └── tree_generation.py
│   ├── templates
│   │   ├── asciidocument_command.adoc
│   │   ├── asciidocument_docs.adoc
│   │   ├── asciidocument_index.adoc
│   │   └── markdown.md
│   ├── .gitattributes
│   ├── .gitignore
│   ├── CODE_OF_CONDUCT.md
│   ├── CODEOWNERS
│   ├── CONTRIBUTING.md
│   ├── FUNDING.yml
│   ├── INFO.md
│   ├── PULL_REQUEST_TEMPLATE
│   ├── SECURITY.md
│   └── STRUCTURE.md
├── docs
│   ├── styles
│   │   └── style.css
│   ├── commands.json
│   ├── contributors.html
│   ├── index.html
│   ├── README.md
│   └── search.html
├── host_services
│   ├── irc_server
│   │   ├── inspircd
│   │   │   ├── configuration.adoc
│   │   │   └── installation.adoc
│   │   ├── kiwiIrc
│   │   │   ├── configuration.adoc
│   │   │   └── installation.adoc
│   │   ├── matrix
│   │   │   ├── configuration.adoc
│   │   │   └── installation.adoc
│   │   ├── mattermost
│   │   │   ├── configuration.adoc
│   │   │   └── installation.adoc
│   │   ├── ngircd
│   │   │   ├── configuration.adoc
│   │   │   └── installation.adoc
│   │   ├── theory
│   │   │   └── theory.adoc
│   │   ├── unrealircd
│   │   │   ├── configuration.adoc
│   │   │   └── installation.adoc
│   │   └── index.adoc
│   └── snmp
│       ├── commands
│       │   ├── snmpbulkwalk.adoc
│       │   ├── snmpget.adoc
│       │   └── snmpwalk.adoc
│       ├── manual
│       │   └── manual.adoc
│       ├── snmp_monitoring_stack
│       │   ├── alert_manager
│       │   │   └── manual.adoc
│       │   └── manual.adoc
│       └── theory
│           └── theory.adoc
├── host_shared_storage
│   ├── commands
│   │   ├── ftp.adoc
│   │   ├── get.adoc
│   │   ├── mget.adoc
│   │   ├── mput.adoc
│   │   ├── put.adoc
│   │   ├── sftp.adoc
│   │   └── vsftpd.adoc
│   ├── ldap_server
│   │   ├── commands
│   │   │   ├── ldapadd.adoc
│   │   │   ├── ldapmodify.adoc
│   │   │   ├── ldapsearch.adoc
│   │   │   ├── slapcat.adoc
│   │   │   └── slappasswd.adoc
│   │   ├── open_ladp
│   │   │   └── documentation.adoc
│   │   ├── samba_ldap
│   │   │   └── documentation.adoc
│   │   ├── documentation.adoc
│   │   └── theory.adoc
│   ├── nfs_server
│   │   ├── documentation.adoc
│   │   └── theory.adoc
│   ├── samba_server
│   │   ├── documentation.adoc
│   │   └── theory.adoc
│   ├── index.adoc
│   └── README.md
├── host_web_services
│   ├── apache2
│   │   └── documentation.adoc
│   ├── commands
│   │   └── httrack.adoc
│   ├── nginx
│   │   ├── GeoIP2
│   │   │   └── documentation.adoc
│   │   └── documentation.adoc
│   ├── wordpress
│   │   └── documentation.adoc
│   ├── index.adoc
│   └── README.md
├── local_filesystem
│   ├── commands
│   │   ├── awk.adoc
│   │   ├── basename.adoc
│   │   ├── bzip2.adoc
│   │   ├── cat.adoc
│   │   ├── cd.adoc
│   │   ├── chattr.adoc
│   │   ├── cksum.adoc
│   │   ├── column.adoc
│   │   ├── comm.adoc
│   │   ├── cp.adoc
│   │   ├── cut.adoc
│   │   ├── diff.adoc
│   │   ├── dirname.adoc
│   │   ├── echo.adoc
│   │   ├── export.adoc
│   │   ├── file.adoc
│   │   ├── find.adoc
│   │   ├── fmt.adoc
│   │   ├── fold.adoc
│   │   ├── gedit.adoc
│   │   ├── grep.adoc
│   │   ├── gzip.adoc
│   │   ├── head.adoc
│   │   ├── iconv.adoc
│   │   ├── join.adoc
│   │   ├── less.adoc
│   │   ├── ln.adoc
│   │   ├── locate.adoc
│   │   ├── ls.adoc
│   │   ├── lsattr.adoc
│   │   ├── md5sum.adoc
│   │   ├── mkdir.adoc
│   │   ├── mkfifo.adoc
│   │   ├── more.adoc
│   │   ├── mv.adoc
│   │   ├── nl.adoc
│   │   ├── operators.adoc
│   │   ├── paste.adoc
│   │   ├── readlink.adoc
│   │   ├── realpath.adoc
│   │   ├── rm.adoc
│   │   ├── rmdir.adoc
│   │   ├── scp.adoc
│   │   ├── sed.adoc
│   │   ├── shred.adoc
│   │   ├── sort.adoc
│   │   ├── split.adoc
│   │   ├── stat.adoc
│   │   ├── sync.adoc
│   │   ├── tail.adoc
│   │   ├── tar.adoc
│   │   ├── touch.adoc
│   │   ├── tr.adoc
│   │   ├── tree.adoc
│   │   ├── uniq.adoc
│   │   ├── unlink.adoc
│   │   ├── updatedb.adoc
│   │   ├── wc.adoc
│   │   ├── xargs.adoc
│   │   ├── xz.adoc
│   │   └── zless.adoc
│   ├── index.adoc
│   └── README.md
├── local_group
│   ├── commands
│   │   ├── gpasswd.adoc
│   │   ├── groupadd.adoc
│   │   ├── groupdel.adoc
│   │   ├── groupmod.adoc
│   │   ├── groups.adoc
│   │   └── newgrp.adoc
│   ├── theory
│   │   └── theory.adoc
│   ├── index.adoc
│   └── README.md
├── local_linux_fundamentals
│   ├── combination_keys
│   │   └── combination.adoc
│   ├── theory
│   │   ├── linus_torvalds.adoc
│   │   └── linux.adoc
│   ├── index.adoc
│   └── README.md
├── local_miscellaneous
│   ├── commands
│   │   ├── banner.adoc
│   │   ├── bc.adoc
│   │   ├── cmatrix.adoc
│   │   ├── cowsay.adoc
│   │   ├── factor.adoc
│   │   ├── figlet.adoc
│   │   ├── fortune.adoc
│   │   ├── hollywood.adoc
│   │   ├── jq.adoc
│   │   ├── look.adoc
│   │   ├── pv.adoc
│   │   ├── sl.adoc
│   │   ├── tmux.adoc
│   │   ├── toilet.adoc
│   │   └── units.adoc
│   ├── index.adoc
│   └── README.md
├── local_network
│   ├── commands
│   │   ├── arp.adoc
│   │   ├── curl.adoc
│   │   ├── dig.adoc
│   │   ├── ethtool.adoc
│   │   ├── host.adoc
│   │   ├── ifconfig.adoc
│   │   ├── ip.adoc
│   │   ├── mtr.adoc
│   │   ├── nc.adoc
│   │   ├── netstat.adoc
│   │   ├── nmap.adoc
│   │   ├── nmcli.adoc
│   │   ├── nslookup.adoc
│   │   ├── ping.adoc
│   │   ├── socat.adoc
│   │   ├── ss.adoc
│   │   ├── tcpdump.adoc
│   │   ├── traceroute.adoc
│   │   ├── wget.adoc
│   │   └── whois.adoc
│   ├── dhcp
│   │   ├── dhcp_failover
│   │   │   ├── manual.md
│   │   │   ├── serv1_01-network-manager-all.yaml
│   │   │   ├── serv1_dhcpd.conf
│   │   │   ├── serv2_01-network-manager-all.yaml
│   │   │   ├── serv2_dhcpd.conf
│   │   │   └── servers_isc-dhcp-server
│   │   └── dhcp_samba
│   │       ├── smb.conf
│   │       └── theory.md
│   ├── interfaces_net
│   │   └── interfaces.adoc
│   ├── ipfire
│   │   └── ipfire.adoc
│   ├── iptables
│   │   ├── arptables
│   │   │   └── arptables.adoc
│   │   ├── ebtables
│   │   │   └── ebtables.adoc
│   │   ├── ip6tables
│   │   │   └── ip6tables.adoc
│   │   └── iptables
│   │       └── iptables.adoc
│   ├── local_network
│   │   └── commands
│   │       ├── netplan.adoc
│   │       └── network.adoc
│   ├── nftables
│   │   └── nftables.adoc
│   ├── theory
│   │   └── theory.adoc
│   ├── index.adoc
│   └── README.md
├── local_permissions
│   ├── access_control_lists
│   │   ├── commands
│   │   │   ├── getfacl.adoc
│   │   │   └── setfacl.adoc
│   │   └── acls.adoc
│   ├── commands
│   │   ├── chmod.adoc
│   │   ├── chown.adoc
│   │   ├── sudo.adoc
│   │   ├── umask.adoc
│   │   └── visudo.adoc
│   ├── theory
│   │   └── theory.adoc
│   ├── index.adoc
│   └── README.md
├── local_process
│   ├── commands
│   │   ├── fuser.adoc
│   │   ├── htop.adoc
│   │   ├── kill.adoc
│   │   ├── lsof.adoc
│   │   ├── nice.adoc
│   │   ├── nohup.adoc
│   │   ├── pgrep.adoc
│   │   ├── pkill.adoc
│   │   ├── ps.adoc
│   │   ├── renice.adoc
│   │   ├── strace.adoc
│   │   ├── timeout.adoc
│   │   └── top.adoc
│   ├── cron
│   │   ├── commands.md
│   │   └── theory.md
│   ├── index.adoc
│   └── README.md
├── local_scripts
│   ├── bash
│   │   ├── example_scripts
│   │   │   ├── arguments.sh
│   │   │   ├── echo.sh
│   │   │   ├── file_check.sh
│   │   │   ├── for.sh
│   │   │   ├── functions.sh
│   │   │   ├── if_else.sh
│   │   │   ├── input.sh
│   │   │   ├── pipes.sh
│   │   │   ├── variables.sh
│   │   │   └── while.sh
│   │   ├── exercises
│   │   │   ├── echo.sh
│   │   │   ├── for.sh
│   │   │   ├── if_else.sh
│   │   │   ├── input.sh
│   │   │   ├── variables.sh
│   │   │   └── while.sh
│   │   ├── one_liners
│   │   │   ├── user_check.sh
│   │   │   └── user_etc_passwd.sh
│   │   └── theory.adoc
│   ├── eBPF
│   │   ├── example_scripts
│   │   │   └── trace_open.bt
│   │   └── theory.adoc
│   ├── Tcl
│   │   ├── example_scripts
│   │   │   ├── comments.tcl
│   │   │   ├── if_else.tcl
│   │   │   ├── input_output.tcl
│   │   │   ├── lists.tcl
│   │   │   ├── procedures.tcl
│   │   │   └── variables.tcl
│   │   └── theory.adoc
│   ├── index.adoc
│   └── README.md
├── local_security
│   ├── certificates
│   │   └── open_ssl.adoc
│   ├── commands
│   │   └── hashcat.adoc
│   ├── forensics
│   │   ├── exiftool
│   │   │   ├── commands
│   │   │   │   └── exiftool.adoc
│   │   │   └── theory.adoc
│   │   └── lime
│   │       ├── commands
│   │       │   └── lime.adoc
│   │       └── theory.adoc
│   ├── local_audit
│   │   └── lynis
│   │       └── lynis.adoc
│   ├── manual_analysis
│   │   └── audit.md
│   ├── network_security
│   │   ├── fail2ban
│   │   │   ├── example.md
│   │   │   └── theory.adoc
│   │   ├── firewall_ufw
│   │   │   ├── commands
│   │   │   │   └── ufw.adoc
│   │   │   └── theory.adoc
│   │   ├── kerberos
│   │   │   └── theory.adoc
│   │   ├── proxy
│   │   │   ├── proxy_squid
│   │   │   │   ├── example.md
│   │   │   │   └── theory.adoc
│   │   │   └── theory
│   │   │       └── theory.adoc
│   │   └── vpn
│   │       ├── openvpn
│   │       │   ├── example.md
│   │       │   └── theory.adoc
│   │       └── theory
│   │           └── theory.adoc
│   ├── opsec
│   │   └── opsec.adoc
│   ├── persec
│   │   └── persec.adoc
│   ├── secure_channels
│   │   ├── secure_channel_ftp
│   │   │   ├── example.md
│   │   │   └── theory.adoc
│   │   ├── secure_channel_ssh
│   │   │   ├── example.md
│   │   │   └── theory.adoc
│   │   └── theory.adoc
│   ├── theory
│   │   └── theory.adoc
│   ├── index.adoc
│   └── README.md
├── local_services
│   ├── commands
│   │   ├── chkconfig.adoc
│   │   ├── initctl.adoc
│   │   ├── journalctl.adoc
│   │   ├── rc-service.adoc
│   │   ├── rc-status.adoc
│   │   ├── service.adoc
│   │   ├── systemctl.adoc
│   │   ├── systemd-analyze.adoc
│   │   └── update-rc.d.adoc
│   ├── daemons
│   │   └── daemons.adoc
│   ├── theory
│   │   └── theory.adoc
│   ├── index.adoc
│   └── README.md
├── local_software
│   ├── commands
│   │   ├── apk.adoc
│   │   ├── apt.adoc
│   │   ├── dnf.adoc
│   │   ├── dpkg.adoc
│   │   ├── flatpak.adoc
│   │   ├── pacman.adoc
│   │   ├── rpm.adoc
│   │   ├── snap_snapctl.adoc
│   │   ├── yum.adoc
│   │   └── zypper.adoc
│   ├── theory
│   │   └── theory.adoc
│   ├── index.adoc
│   └── README.md
├── local_storage
│   ├── backup
│   │   ├── dd
│   │   │   ├── commands
│   │   │   │   └── dd.adoc
│   │   │   └── theory
│   │   │       └── theory.adoc
│   │   ├── rsync
│   │   │   ├── commands
│   │   │   │   └── rsync.adoc
│   │   │   └── theory
│   │   │       └── theory.adoc
│   │   └── theory.adoc
│   ├── commands
│   │   ├── blkid.adoc
│   │   ├── cfdisk.adoc
│   │   ├── df.adoc
│   │   ├── du.adoc
│   │   ├── fdisk.adoc
│   │   ├── fsck.adoc
│   │   ├── ipmitool.adoc
│   │   ├── losetup.adoc
│   │   ├── lsblk.adoc
│   │   ├── lspci.adoc
│   │   ├── lsusb.adoc
│   │   ├── lvcreate.adoc
│   │   ├── lvdisplay.adoc
│   │   ├── lvextend.adoc
│   │   ├── lvreduce.adoc
│   │   ├── lvremove.adoc
│   │   ├── lvrename.adoc
│   │   ├── lvresize.adoc
│   │   ├── lvs.adoc
│   │   ├── lvscan.adoc
│   │   ├── mkfs.adoc
│   │   ├── mkswap.adoc
│   │   ├── mount.adoc
│   │   ├── nvme-cli.adoc
│   │   ├── partx.adoc
│   │   ├── pvcreate.adoc
│   │   ├── pvdisplay.adoc
│   │   ├── pvmove.adoc
│   │   ├── pvremove.adoc
│   │   ├── pvs.adoc
│   │   ├── quota.adoc
│   │   ├── resize2fs.adoc
│   │   ├── smartctl.adoc
│   │   ├── swapoff.adoc
│   │   ├── swapon.adoc
│   │   ├── umount.adoc
│   │   ├── vgchange.adoc
│   │   ├── vgcreate.adoc
│   │   ├── vgdisplay.adoc
│   │   ├── vgextend.adoc
│   │   ├── vgreduce.adoc
│   │   ├── vgremove.adoc
│   │   ├── vgs.adoc
│   │   └── vgscan.adoc
│   ├── partitions
│   │   └── theory.adoc
│   ├── procedures
│   │   ├── partition_disk.adoc
│   │   ├── raid.adoc
│   │   └── virtual_disk.adoc
│   ├── raid
│   │   ├── mount.md
│   │   ├── process.sh
│   │   └── theory.adoc
│   ├── index.adoc
│   └── README.md
├── local_system_data
│   ├── environment
│   │   ├── env.adoc
│   │   ├── environment_variables.adoc
│   │   ├── printenv.adoc
│   │   ├── shopt.adoc
│   │   └── uname.adoc
│   ├── graphics
│   │   └── commands
│   │       ├── glxinfo.adoc
│   │       ├── xdpyinfo.adoc
│   │       ├── xrandr.adoc
│   │       └── xwininfo.adoc
│   ├── in_out
│   │   ├── commands
│   │   │   ├── cal.adoc
│   │   │   ├── date.adoc
│   │   │   ├── tee.adoc
│   │   │   ├── time.adoc
│   │   │   └── yes.adoc
│   │   ├── pipes.adoc
│   │   ├── redirections.adoc
│   │   └── stdin_stdout_stderr.adoc
│   ├── monitoring
│   │   └── commands
│   │       ├── dmesg.adoc
│   │       ├── dstat.adoc
│   │       ├── free.adoc
│   │       ├── iostat.adoc
│   │       ├── iotop.adoc
│   │       ├── logrotate.adoc
│   │       ├── sensors.adoc
│   │       ├── uptime.adoc
│   │       ├── vmstat.adoc
│   │       └── watch.adoc
│   ├── shell
│   │   ├── alias.adoc
│   │   ├── history.adoc
│   │   └── shells.adoc
│   ├── system_info
│   │   └── commands
│   │       ├── arch.adoc
│   │       ├── dmidecode.adoc
│   │       ├── hostname.adoc
│   │       ├── inxi.adoc
│   │       ├── ldd.adoc
│   │       ├── lscpu.adoc
│   │       ├── lsdev.adoc
│   │       ├── lshw.adoc
│   │       ├── lsmod.adoc
│   │       ├── lsscsi.adoc
│   │       ├── lstopo.adoc
│   │       └── screenfetch.adoc
│   ├── system_structure
│   │   └── dirs.adoc
│   ├── index.adoc
│   └── README.md
├── local_users
│   ├── commands
│   │   ├── adduser.adoc
│   │   ├── chage.adoc
│   │   ├── chfn.adoc
│   │   ├── chsh.adoc
│   │   ├── deluser.adoc
│   │   ├── id.adoc
│   │   ├── last.adoc
│   │   ├── passwd.adoc
│   │   ├── su.adoc
│   │   ├── useradd.adoc
│   │   ├── w.adoc
│   │   ├── wall.adoc
│   │   └── who.adoc
│   ├── system_users
│   │   └── users.adoc
│   ├── theory
│   │   ├── account_files.adoc
│   │   └── theory.adoc
│   ├── index.adoc
│   └── README.md
├── LICENSE
└── README.md
</code></pre>
<!-- AUTO-GENERATED-TREE:END -->

  </code></pre>
</details>

---
<details open>
<summary><strong>• FORMATO DE DOCUMENTACIÓN</strong></summary>
<h1>Formato de documentación</h1>

El repositorio sigue un estándar fijo de documentación para mantener el orden y permitir una correcta indexación a la hora de generar PDFs.
- [Ejemplo de premodelo en Markdown (.md)](.github/templates/markdown.md)
- [Ejemplo de premodelo en Documento Ascii tipo Index (.adoc)](.github/templates/asciidocument_index.adoc)
- [Ejemplo de premodelo en Documento Ascii tipo Comandos (.adoc)](.github/templates/asciidocument_command.adoc)
- [Ejemplo de premodelo en Documento Ascii tipo Documentos (.adoc)](.github/templates/asciidocument_docs.adoc)
- [Formato y significado en nombres de directorios](STRUCTURE.md)

Más información en [CONTRIBUTING](.github/CONTRIBUTING.md).
</details>

---
<details open>
<summary><strong>• TRADUCCIONES</strong></summary>
<h1>Traducciones en los documentos</h1>

El repositorio se adapta a diferentes lenguas mediante la automatización de la generación PDF.
<p align="center">
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/ESP">Español</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/ENG">English</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/DE">Deutsch</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/FR">Français</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/PT">Português</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/RU">Русский</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/ZH">中文</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/KO">한국어</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/JA">日本語</a>
</p>

> En caso de ver iconos semejantes a "▯" es probable que sea necesario [descargar fuentes CJK](https://github.com/notofonts/noto-cjk/releases/latest) en el equipo.
</details>

---
<div align="center">
  <p>Linux Commands - By Nisamov | MIT License - 2026</p>
  <p>Contacto: <a href="mailto:nisamov.contact@gmail.com">nisamov.contact@gmail.com</a></p>
</div>