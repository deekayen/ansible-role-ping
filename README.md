Ping and Traceroute
===================

[![CI](https://github.com/deekayen/ansible-role-ping/workflows/CI/badge.svg)](https://github.com/deekayen/ansible-role-ping/actions?query=workflow%3ACI) [![Project Status: Inactive – The project has reached a stable, usable state but is no longer being actively developed; support/maintenance will be provided as time allows.](https://www.repostatus.org/badges/latest/inactive.svg)](https://www.repostatus.org/#inactive) ![BSD 3-Clause license](https://img.shields.io/badge/license-BSD%203--Clause-blue) ![Linux platform](https://img.shields.io/badge/platform-linux-lightgrey)

Install the firewalld service, then override the default-deny firewall configurations to allow ping (echo-request) or other diagnostic traceroute traffic.

Requirements
------------

firewalld

Default Variables
-----------------

The options for types of allowed ICMP are dictated by the firewalld service.

```Shell
# firewall-cmd --get-icmptypes
destination-unreachable echo-reply echo-request parameter-problem redirect router-advertisement router-solicitation source-quench time-exceeded timestamp-reply timestamp-request
```

The `ping_zone` is where the firewalld rules will update to modify ICMP access.

### Role Defaults

```YAML
ping_enable: yes
ping_source: 0.0.0.0/0
ping_types:
- echo-request
ping_zone: public
```

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: all:!platform_windows
      roles:
        - deekayen.ping
