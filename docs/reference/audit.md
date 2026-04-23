# Audit
Audit records and configuration change history. `configchanges` requires FMC **7.4.0**.

::: fireREST.fmc.audit.auditrecord.AuditRecord
    options:
      show_root_heading: true
      heading_level: 2
      show_source: false
      show_bases: true
      inherited_members: true
      filters:
        - "!^_"

::: fireREST.fmc.audit.configchanges.ConfigChanges
    options:
      show_root_heading: true
      heading_level: 2
      show_source: false
      show_bases: true
      inherited_members: true
      filters:
        - "!^_"
