%define base_name	lablgtk
%define name		ocaml-%{base_name}
%define version		1.2.7
%define release		%mkrel 17

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
OCaml interface to Gtk+ tool kit.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
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
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_libdir}/ocaml/stublibs
make install \
	BINDIR=%{buildroot}%{_bindir} \
	INSTALLDIR=%{buildroot}%{_libdir}/ocaml/lablgtk \
	DLLDIR=%{buildroot}%{_libdir}/ocaml/stublibs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING CHANGES README
%dir %{_libdir}/ocaml/lablgtk
%{_libdir}/ocaml/lablgtk/*.cmi
%{_libdir}/ocaml/lablgtk/*.cma
%{_libdir}/ocaml/stublibs/*.so

%files devel
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/ocaml/lablgtk/*.a
%{_libdir}/ocaml/lablgtk/*.cmo
%{_libdir}/ocaml/lablgtk/*.cmx
%{_libdir}/ocaml/lablgtk/*.cmxa
%{_libdir}/ocaml/lablgtk/*.mli
%{_libdir}/ocaml/lablgtk/*.ml
%{_libdir}/ocaml/lablgtk/*.o
%{_libdir}/ocaml/lablgtk/*.h
%{_libdir}/ocaml/lablgtk/varcc
%{_libdir}/ocaml/lablgtk/lablgtktop
%{_libdir}/ocaml/lablgtk/lablgtktop_t
