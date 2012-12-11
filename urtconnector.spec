Summary:        Advanced UrbanTerror launcher program
Name:           urtconnector
Version:        0.9.0
Release:        1
License:        GPLv3
Group:          Games/Other
Url:            http://code.google.com/p/%{name}/
Source0:        http://urtconnector.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRequires:  qt4-devel
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(phonon)
BuildRequires:  cmake
Requires:       qstat

%description
Primary developed by Vladislav Navrocky (=XaoC=vlad.ru),
=XaoC= and Loaded Arms Russian clans members.
This program uses Qt4, written in C++ and can
be run on windows, unix or mac.

%prep 
%setup -qn %{name}

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build

%files
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/*
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/%{name}.png

