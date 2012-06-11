Summary:        Advanced UrbanTerror launcher program
Name:           urtconnector
Version:        0.8.1
Release:        1
License:        GPLv3
Group:          Games/Other
Url:            http://code.google.com/p/%{name}/
Source0:        http://urtconnector.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:         change_qstat_binary_name.diff

BuildRequires:  qt4-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
Requires:       qstat

%description
Primary developed by Vladislav Navrocky (=XaoC=vlad.ru), =XaoC= and Loaded Arms Russian clans members.
This program uses Qt4, written in C++ and can be run on windows, unix or mac.

%prep 
%setup -qn %{name}-%{version}
%patch0 -p1

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build

%find_lang %name

%files -f %{name}.lang
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/*
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/%{name}.png

