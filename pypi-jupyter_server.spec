#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jupyter_server
Version  : 1.18.1
Release  : 48
URL      : https://files.pythonhosted.org/packages/5b/6e/01af30a3e12d2f8eda1405ca8710442f1e7d05d30f8abbfca3b1f0375ce0/jupyter_server-1.18.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/5b/6e/01af30a3e12d2f8eda1405ca8710442f1e7d05d30f8abbfca3b1f0375ce0/jupyter_server-1.18.1.tar.gz
Summary  : The backend—i.e. core services, APIs, and REST endpoints—to Jupyter web applications.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-jupyter_server-bin = %{version}-%{release}
Requires: pypi-jupyter_server-license = %{version}-%{release}
Requires: pypi-jupyter_server-python = %{version}-%{release}
Requires: pypi-jupyter_server-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(anyio)
BuildRequires : pypi(argon2_cffi)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(jupyter_client)
BuildRequires : pypi(jupyter_core)
BuildRequires : pypi(jupyter_packaging)
BuildRequires : pypi(nbconvert)
BuildRequires : pypi(nbformat)
BuildRequires : pypi(packaging)
BuildRequires : pypi(pre_commit)
BuildRequires : pypi(prometheus_client)
BuildRequires : pypi(pyzmq)
BuildRequires : pypi(send2trash)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(terminado)
BuildRequires : pypi(tornado)
BuildRequires : pypi(traitlets)
BuildRequires : pypi(websocket_client)
BuildRequires : pypi(wheel)

%description
# Jupyter Server
[![Build Status](https://github.com/jupyter/jupyter_server/workflows/CI/badge.svg?query=branch%3A1.x++)](https://github.com/jupyter-server/jupyter_server/actions?query=branch%3A1.x++)
[![Documentation Status](https://readthedocs.org/projects/jupyter-server/badge/?version=stable)](http://jupyter-server.readthedocs.io/en/latest/?badge=stable)

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
Requires: pypi(nbconvert)
Requires: pypi(nbformat)
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
%setup -q -n jupyter_server-1.18.1
cd %{_builddir}/jupyter_server-1.18.1
pushd ..
cp -a jupyter_server-1.18.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657116601
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupyter_server
cp %{_builddir}/jupyter_server-1.18.1/COPYING.md %{buildroot}/usr/share/package-licenses/pypi-jupyter_server/8fd549f28c3423c251b3b70e91bdad2fbfe6ef30
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-server

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jupyter_server/8fd549f28c3423c251b3b70e91bdad2fbfe6ef30

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
