%define base_name	lablgtk
%define name		ocaml-%{base_name}
%define version		1.2.7
%define release		%mkrel 11

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	OCaml interface to the GIMP Tool Kit
Source:		http://wwwfun.kurims.kyoto-u.ac.jp/soft/olabl/dist/lablgtk-%{version}.tar.bz2
URL:		http://wwwfun.kurims.kyoto-u.ac.jp/soft/olabl/lablgtk.html
License:	LGPL
Group:		Development/Other
BuildRequires:	camlp4
BuildRequires:	gtk-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
OCaml interface to the GIMP Tool Kit.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}
Requires:	gtk-devel

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n %{base_name}-%{version}

%build
make configure
make
make opt

%install
rm -rf %{buildroot}
destdir=`ocamlc -where`
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}$destdir/stublibs
make install \
	BINDIR=%{buildroot}%{_bindir} \
	INSTALLDIR=%{buildroot}$destdir/lablgtk \
	DLLDIR=%{buildroot}$destdir/stublibs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/ocaml/stublibs/*

%files devel
%defattr(-,root,root)
%doc CHANGES README
%{_bindir}/*
%{_libdir}/ocaml/lablgtk


