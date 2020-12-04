# Ansible role: WKHTMLTOPDF

Install WKHTMLTOPDF (and its dependencies).

## Requirements

* Ubuntu 14.04, 18.04, or Red Hat / CentOS 6

## Role Variables

See defaults.yml

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
