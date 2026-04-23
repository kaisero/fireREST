# NetMap
Network map host and vulnerability management, including bulk delete by IP address.

::: fireREST.fmc.netmap.host.Host
    options:
      show_root_heading: true
      heading_level: 2
      show_source: false
      show_bases: true
      inherited_members: true
      filters:
        - "!^_"

::: fireREST.fmc.netmap.vulnerability.Vulnerability
    options:
      show_root_heading: true
      heading_level: 2
      show_source: false
      show_bases: true
      inherited_members: true
      filters:
        - "!^_"
