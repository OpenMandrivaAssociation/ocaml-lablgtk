%define base_name	lablgtk
%define name		ocaml-%{base_name}
%define version		1.2.7
%define release		18

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


%changelog
* Mon Jan 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.7-17mdv2010.1
+ Revision: 496365
- rebuild

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.7-16mdv2010.0
+ Revision: 389926
- rebuild

* Wed Dec 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.7-15mdv2009.1
+ Revision: 318268
- site-lib hierarchy doesn't exists anymore

* Mon Dec 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.7-14mdv2009.1
+ Revision: 317606
- move non-devel files into main package

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.2.7-13mdv2009.0
+ Revision: 268320
- rebuild early 2009.0 package (before pixel changes)
- fix description

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.2.7-12mdv2009.0
+ Revision: 136633
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.7-12mdv2008.0
+ Revision: 77687
- ocaml policy compliance

* Tue Jul 03 2007 Pixel <pixel@mandriva.com> 1.2.7-11mdv2008.0
+ Revision: 47403
- rebuild for new ocaml 3.10.0


* Thu Jan 25 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.7-10mdv2007.0
+ Revision: 113149
- rebuild for new ocaml
- Import ocaml-lablgtk

* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.7-9mdv2007.0
- Rebuild

* Wed Apr 26 2006 Pixel <pixel@mandriva.com> 1.2.7-8mdk
- rebuild for new ocaml

* Thu Jan 26 2006 Pixel <pixel@mandriva.com> 1.2.7-7mdk
- only the stublibs are non-devel stuff (ie not requiring ocaml)

* Mon Jan 23 2006 Pixel <pixel@mandriva.com> 1.2.7-6mdk
- rebuild for new ocaml

* Fri Jan 13 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.7-5mdk
- spec cleanup
- splti devel file in subpackage

* Mon Nov 07 2005 Pixel <pixel@mandriva.com> 1.2.7-4mdk
- rebuild for new ocaml

* Thu Nov 03 2005 Pixel <pixel@mandriva.com> 1.2.7-3mdk
- rebuild for ocaml 3.08.3 (otherwise some builds fail) (thanks to Anssi Hannula)

* Sun Feb 06 2005 Pixel <pixel@mandrakesoft.com> 1.2.7-2mdk
- rebuild for ocaml 3.08.2 (otherwise one get error "... inconsistent assumptions over implementation Thread")

* Tue Nov 23 2004 Pixel <pixel@mandrakesoft.com> 1.2.7-1mdk
- new release

* Tue Nov 23 2004 Pixel <pixel@mandrakesoft.com> 1.2.6-3mdk
- rebuild

* Mon Oct 11 2004 Pascal Terjan <pterjan@mandrake.org> 1.2.6-2mdk
- drop patch

