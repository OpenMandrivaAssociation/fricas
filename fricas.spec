Name: fricas
Version: 1.1.8
Release: 3
Summary: Computer Algebra System
License: Modified BSD License
Group: Sciences/Mathematics
Url: http://fricas.sourceforge.net
Source0: http://downloads.sourceforge.net/project/fricas/fricas/%{version}/%{name}-%{version}-full.tar.bz2
Source1: %name-16.png
Source2: %name-32.png
Source3: %name-48.png
Source4: %name.desktop
Requires: sbcl
Conflicts: axiom
BuildRequires: pkgconfig(xpm)
BuildRequires: clisp
BuildRequires: sbcl

%description
FriCAS is an advanced computer algebra system. Its capabilities range 
from calculus (integration and differentiation) to abstract algebra. 
It can plot functions and has integrated help system.
 
FriCAS a fork of Axiom project -- its starting point was wh-sandbox 
branch of the Axiom project.

%prep 
%setup -q -n %name-%version

%build

%configure --with-lisp=clisp
%make

%install
%define _strip_method no

%makeinstall_std
# icons
install -D -m644 %SOURCE1 %{buildroot}%{_miconsdir}/%name.png
install -D -m644 %SOURCE2 %{buildroot}%{_iconsdir}/%name.png
install -D -m644 %SOURCE3 %{buildroot}%{_liconsdir}/%name.png

# menu items
install -D -m644 %SOURCE4 %{buildroot}%{_datadir}/applications/%name.desktop

%files
%{_bindir}/*
%{_datadir}/applications/%name.desktop
%{_iconsdir}/*/
%{_libdir}/%name/*
%doc README FAQ CHA* Cha*


%changelog
* Thu Jun 21 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.7-1
+ Revision: 806605
- version update 1.1.7

* Mon Feb 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.6-1
+ Revision: 778072
- version update 1.1.6
- imported package fricas

