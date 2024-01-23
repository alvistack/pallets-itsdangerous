# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-itsdangerous
Epoch: 100
Version: 2.2.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Safely pass data to untrusted environments and back
License: BSD-3-Clause
URL: https://github.com/pallets/itsdangerous/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Various helpers to pass data to untrusted environments and to get it
back safe and sound. Data is cryptographically signed to ensure that a
token has not been tampered with.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-itsdangerous
Summary: Safely pass data to untrusted environments and back
Requires: python3
Provides: python3-itsdangerous = %{epoch}:%{version}-%{release}
Provides: python3dist(itsdangerous) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-itsdangerous = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(itsdangerous) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-itsdangerous = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(itsdangerous) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-itsdangerous
Various helpers to pass data to untrusted environments and to get it
back safe and sound. Data is cryptographically signed to ensure that a
token has not been tampered with.

%files -n python%{python3_version_nodots}-itsdangerous
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-itsdangerous
Summary: Safely pass data to untrusted environments and back
Requires: python3
Provides: python3-itsdangerous = %{epoch}:%{version}-%{release}
Provides: python3dist(itsdangerous) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-itsdangerous = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(itsdangerous) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-itsdangerous = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(itsdangerous) = %{epoch}:%{version}-%{release}

%description -n python3-itsdangerous
Various helpers to pass data to untrusted environments and to get it
back safe and sound. Data is cryptographically signed to ensure that a
token has not been tampered with.

%files -n python3-itsdangerous
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-itsdangerous
Summary: Safely pass data to untrusted environments and back
Requires: python3
Provides: python3-itsdangerous = %{epoch}:%{version}-%{release}
Provides: python3dist(itsdangerous) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-itsdangerous = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(itsdangerous) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-itsdangerous = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(itsdangerous) = %{epoch}:%{version}-%{release}

%description -n python3-itsdangerous
Various helpers to pass data to untrusted environments and to get it
back safe and sound. Data is cryptographically signed to ensure that a
token has not been tampered with.

%files -n python3-itsdangerous
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%changelog
