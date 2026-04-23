# System
FMC system information, domain list, and server version.

::: fireREST.fmc.system.info.Info
    options:
      show_root_heading: true
      heading_level: 2
      show_source: false
      show_bases: true
      inherited_members: true
      filters:
        - "!^_"

::: fireREST.fmc.system.info.domain.Domain
    options:
      show_root_heading: true
      heading_level: 2
      show_source: false
      show_bases: true
      inherited_members: true
      filters:
        - "!^_"

::: fireREST.fmc.system.info.serverversion.ServerVersion
    options:
      show_root_heading: true
      heading_level: 2
      show_source: false
      show_bases: true
      inherited_members: true
      filters:
        - "!^_"
