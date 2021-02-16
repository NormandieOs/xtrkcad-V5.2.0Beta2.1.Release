# spec file for package xtrkcad version 5.2.0Beta2.1
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2020 Gilles laffite,France <gilles.laffite76@gmail.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via <gilles.laffite76@gmail.com>
#
%define name xtrkcad
%define version 5.2.0Beta2.1
Name: %{name}
Version: %{version}
Release: 0
License: GPL-2.0-or-later
Summary: XTrackCAD is a CAD program for designing model railroad layouts
Summary(fr): XTrackCAD est un programme CAO/CAD de modélisme ferroviaire
Url:  http://www.xtrkcad.org
Group:  Productivity/Graphics/Other
Source0: xtrkcad-source-%{version}.tar.bz2
Patch0: fix_desktop_file.patch
BuildRequires: cmake >= 2.8
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: gettext-runtime
BuildRequires: gettext-devel
BuildRequires: glib2-devel
BuildRequires: glibc-devel
BuildRequires: gtk2-devel
BuildRequires: cairo-devel
BuildRequires: libgtkhtml-4_0-0
BuildRequires: libzip-devel
BuildRequires: zlib-devel
BuildRequires: zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Recommends: %{name}-lang
%lang_package

%description
XTrackCAD is a CAD program for designing model railroad layouts. You can easily create layout of any scale or size. Libraries for many brands of track and turnouts are included.Adding new components is easy with the built-in editor

%description -l fr
XTrackCAD est un programme CAO/CAD de modélisme ferroviaire

%prep
ln -s xtrkcad-source-%{version} xtrkcad-%{version}

%setup -q -D

%patch0 -p1 -b .fix_desktop_file
 
%build
%cmake \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_C_FLAGS="$RPM_OPT_FLAGS -Wl,--allow-multiple-definition " \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DXTRKCAD_USE_GETTEXT=ON \
    -DXTRKCAD_USE_GTK=ON
    
%cmake_build
 
%install

%cmake_install
        
%find_lang %{name} %{?no_lang_C}

%files
%defattr(-,root,root)
%doc app/COPYING
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%files lang -f %{name}.lang
%changelog
   
