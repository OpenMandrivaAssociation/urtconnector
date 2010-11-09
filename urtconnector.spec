Summary:        Advanced UrbanTerror launcher program
Name:           urtconnector
Version:        0.5.1
Release:        %mkrel 1
License:        GPLv3
Group:          Games/Other
Source0:        http://urtconnector.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:         change_qstat_binary_name.diff
Url:            http://code.google.com/p/%{name}/
BuildRequires:  qt4-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
Requires:       qstat
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Primary developed by Vladislav Navrocky (=XaoC=vlad.ru), =XaoC= and Loaded Arms Russian clans members.
This program uses Qt4, written in C++ and can be run on windows, unix or mac.


%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/*
#--------------------------------------------------------------------

%prep 
%setup -qn %{name}-%{version}
%patch0 -p1

%build
%cmake_qt4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%find_lang %name

%clean 
rm -rf %{buildroot} 
