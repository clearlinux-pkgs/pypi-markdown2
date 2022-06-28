#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-markdown2
Version  : 2.4.3
Release  : 6
URL      : https://files.pythonhosted.org/packages/2b/26/1dd47bdf8adb98e1807b2283a88d6d4379911a2e1a1da266739c038ef8e2/markdown2-2.4.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/2b/26/1dd47bdf8adb98e1807b2283a88d6d4379911a2e1a1da266739c038ef8e2/markdown2-2.4.3.tar.gz
Summary  : A fast and complete Python implementation of Markdown
Group    : Development/Tools
License  : MIT
Requires: pypi-markdown2-bin = %{version}-%{release}
Requires: pypi-markdown2-license = %{version}-%{release}
Requires: pypi-markdown2-python = %{version}-%{release}
Requires: pypi-markdown2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Markdown is a text-to-HTML filter; it translates an easy-to-read /
        easy-to-write structured text format into HTML.  Markdown's text
        format is most similar to that of plain text email, and supports
        features such as headers, *emphasis*, code blocks, blockquotes, and

%package bin
Summary: bin components for the pypi-markdown2 package.
Group: Binaries
Requires: pypi-markdown2-license = %{version}-%{release}

%description bin
bin components for the pypi-markdown2 package.


%package license
Summary: license components for the pypi-markdown2 package.
Group: Default

%description license
license components for the pypi-markdown2 package.


%package python
Summary: python components for the pypi-markdown2 package.
Group: Default
Requires: pypi-markdown2-python3 = %{version}-%{release}

%description python
python components for the pypi-markdown2 package.


%package python3
Summary: python3 components for the pypi-markdown2 package.
Group: Default
Requires: python3-core
Provides: pypi(markdown2)

%description python3
python3 components for the pypi-markdown2 package.


%prep
%setup -q -n markdown2-2.4.3
cd %{_builddir}/markdown2-2.4.3
pushd ..
cp -a markdown2-2.4.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656394620
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-markdown2
cp %{_builddir}/markdown2-2.4.3/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-markdown2/2e9aec16de154cd9fbdc11f4d1b3bbd25f104c1a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/markdown2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-markdown2/2e9aec16de154cd9fbdc11f4d1b3bbd25f104c1a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
