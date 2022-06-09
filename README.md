# DBT-7 packaging

This repository contains scripts, relying on `docker-compose`, used to build
`dbt7` packages. Only the RPM format for RHEL 8 based distros is currently
supported.

## Package building

Execute the following `make` command to build the packages:
```console
$ make -C rpm
```

Generated packages are located into the `rpm/build/` directory.
