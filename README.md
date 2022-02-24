Chrony
=========

Install and configure Chrony.

Role Variables
--------------

| Variable    | Type   | Default      |
| ----------- | ------ | ------------ |
| chrony_pool | String | pool.ntp.org |

Example Playbook
----------------

```
- hosts: servers
  roles:
  - chrony
```

License
-------

MIT

Author Information
------------------

kcir
