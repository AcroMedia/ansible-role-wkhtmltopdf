# Ansible role: WKHTMLTOPDF

Install WKHTMLTOPDF (and its dependencies).

# Molecule Setup

- refer to setup instructions for basic test running: [molecule-setup](https://git.acromedia.com/mmccann/molecule-setup/blob/master/README.md)
- after setting up your virtual environment and installing dependencies ...
```bash
$ TEST_HOME=root MOLECULE_DISTRO=debian8 molecule test --destroy=never
```

- if you do not include ```TEST_HOME``` then tests will fail because your local root inside the docker container (which doesn't exist!) 

__Variations of MOLECULE_DISTRO__ 


__running the full test suite__

```bash
$ tox
```

## Requirements

* Ubuntu 14.04, 18.04, or Red Hat / CentOS 6

## Role Variables

None: See 'vars'

## Dependencies

None

## Example Playbook

    - hosts: servers
    - name: Install WKHTMLTOPDF
      role: acromedia.wkhtmltopdf
      tags:
        - wkhtmltopdf

## License

GPLv3

## Author Information

Acro Media Inc.
https://www.acromedia.com/
