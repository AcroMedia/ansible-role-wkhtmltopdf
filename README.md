# Ansible role: WKHTMLTOPDF

![.github/workflows/molecule.yml](https://github.com/AcroMedia/ansible-role-wkhtmltopdf/workflows/.github/workflows/molecule.yml/badge.svg)

Install WKHTMLTOPDF (and its dependencies).

## Requirements

* Ubuntu 14.04, 18.04, or Red Hat / CentOS 6
* Your playbook must gather facts.

## Role Variables

See defaults.yml

## Dependencies

None

## Example Playbook

    - hosts: my_group
      gather_facts: true
      become: true
      roles:
        - name: Install WKHTMLTOPDF
          role: acromedia.wkhtmltopdf
          tags:
            - wkhtmltopdf

## License

GPLv3

## Author Information

Acro Media Inc.
https://www.acromedia.com/
