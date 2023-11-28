#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v2
# autospec commit: e661f3a
#
Name     : pypi-jupyter_server
Version  : 2.11.1
Release  : 72
URL      : https://files.pythonhosted.org/packages/8a/b9/3525a817adc21923be729ef4715adf5209c35e8a87057b336ffd30908a88/jupyter_server-2.11.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/8a/b9/3525a817adc21923be729ef4715adf5209c35e8a87057b336ffd30908a88/jupyter_server-2.11.1.tar.gz
Summary  : The backend—i.e. core services, APIs, and REST endpoints—to Jupyter web applications.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-jupyter_server-bin = %{version}-%{release}
Requires: pypi-jupyter_server-license = %{version}-%{release}
Requires: pypi-jupyter_server-python = %{version}-%{release}
Requires: pypi-jupyter_server-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Jupyter Server
[![Build Status](https://github.com/jupyter-server/jupyter_server/actions/workflows/python-tests.yml/badge.svg?query=branch%3Amain++)](https://github.com/jupyter-server/jupyter_server/actions/workflows/python-tests.yml/badge.svg?query=branch%3Amain++)
[![Documentation Status](https://readthedocs.org/projects/jupyter-server/badge/?version=latest)](http://jupyter-server.readthedocs.io/en/latest/?badge=latest)

%package bin
Summary: bin components for the pypi-jupyter_server package.
Group: Binaries
Requires: pypi-jupyter_server-license = %{version}-%{release}

%description bin
bin components for the pypi-jupyter_server package.


%package license
Summary: license components for the pypi-jupyter_server package.
Group: Default

%description license
license components for the pypi-jupyter_server package.


%package python
Summary: python components for the pypi-jupyter_server package.
Group: Default
Requires: pypi-jupyter_server-python3 = %{version}-%{release}

%description python
python components for the pypi-jupyter_server package.


%package python3
Summary: python3 components for the pypi-jupyter_server package.
Group: Default
Requires: python3-core
Provides: pypi(jupyter_server)
Requires: pypi(anyio)
Requires: pypi(argon2_cffi)
Requires: pypi(jinja2)
Requires: pypi(jupyter_client)
Requires: pypi(jupyter_core)
Requires: pypi(jupyter_events)
Requires: pypi(jupyter_server_terminals)
Requires: pypi(nbconvert)
Requires: pypi(nbformat)
Requires: pypi(overrides)
Requires: pypi(packaging)
Requires: pypi(prometheus_client)
Requires: pypi(pyzmq)
Requires: pypi(send2trash)
Requires: pypi(terminado)
Requires: pypi(tornado)
Requires: pypi(traitlets)
Requires: pypi(websocket_client)

%description python3
python3 components for the pypi-jupyter_server package.


%prep
%setup -q -n jupyter_server-2.11.1
cd %{_builddir}/jupyter_server-2.11.1
pushd ..
cp -a jupyter_server-2.11.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701162069
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . anyio
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . anyio
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupyter_server
cp %{_builddir}/jupyter_server-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jupyter_server/a2539650cfdf8871b9737115b20d5f8e48e8ab7b || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
pypi-dep-fix.py %{buildroot} anyio
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-server

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jupyter_server/a2539650cfdf8871b9737115b20d5f8e48e8ab7b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
