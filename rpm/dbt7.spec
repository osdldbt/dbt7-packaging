%global debug_package %{nil}
%{!?pkgrevision: %global pkgrevision 1}
%{!?pgversion: %global pgversion 14}
%global pkgname dbt7
%define installpath /usr/bin
%define _unpackaged_files_terminate_build 0

Name:          %{pkgname}
Version:       %{pkgversion}
Release:       %{pkgrevision}%{?dist}
Summary:       Fair Use TPC Benchmark(TM) DS kit
License:       The Artistic License
Source:        v%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Fair Use TPC Benchmark(TM) H kit

%prep
%setup -q -n dbt7-%{version}

%build
PKG_CONFIG_PATH="/usr/pgsql-%{pgversion}/lib/pkgconfig" PATH=$PATH:/usr/pgsql-%{pgversion}/bin cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}/%{installpath}/.. .
make

%install
%{__install} -d %{buildroot}/%{installpath}
make install
mkdir -p %{buildroot}/usr/share/dbt7

# DSGen patches
cp patches/dbt7-DSGen-software-code-3.2.0rc1.diff %{buildroot}/usr/share/dbt7/
cp patches/dbt7-DSGen-software-code-3.2.0rc1-postgresql-queries.diff %{buildroot}/usr/share/dbt7/

%files
%{installpath}/dbt7-generate-report
%{installpath}/dbt7-get-config
%{installpath}/dbt7-load-test
%{installpath}/dbt7-pgsql-create-db
%{installpath}/dbt7-pgsql-create-indexes
%{installpath}/dbt7-pgsql-create-tables
%{installpath}/dbt7-pgsql-data-maintenance
%{installpath}/dbt7-pgsql-dbstat
%{installpath}/dbt7-pgsql-drop-tables
%{installpath}/dbt7-pgsql-get-query-time
%{installpath}/dbt7-pgsql-load-data
%{installpath}/dbt7-pgsql-report
%{installpath}/dbt7-pgsql-run-stream
%{installpath}/dbt7-pgsql-start-db
%{installpath}/dbt7-pgsql-stop-db
%{installpath}/dbt7-pgsql-time-statistics
%{installpath}/dbt7-plot-results
%{installpath}/dbt7-post-process
%{installpath}/dbt7-power-test
%{installpath}/dbt7-run-workload
%{installpath}/dbt7-sysstats
%{installpath}/dbt7-throughput-test
/usr/share/dbt7/dbt7-DSGen-software-code-3.2.0rc1.diff
/usr/share/dbt7/dbt7-DSGen-software-code-3.2.0rc1-postgresql-queries.diff

%changelog
* Fri Oct 15 2021 Julien Tachoires <julmon@gmail.com> - master-1
- Initial packaging
