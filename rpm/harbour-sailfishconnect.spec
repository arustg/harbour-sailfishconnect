# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-sailfishconnect

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    SailfishOS client for KDE-Connect
Version:    0.4
Release:    0.1
Group:      Qt/Qt
License:    LICENSE
URL:        https://github.com/R1tschY/harbour-sailfishconnect
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-sailfishconnect.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(openssl) >= 1.0.1
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(contextkit-statefs)
BuildRequires:  pkgconfig(nemonotifications-qt5)
BuildRequires:  ninja
BuildRequires:  cmake
BuildRequires:  desktop-file-utils

%description
SailfishOS client for KDE-Connect


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre

# should be setup, but qtc5 ignores it
VENV=$RPM_BUILD_ROOT/venv

if [ ! -f ~/.local/bin/virtualenv ] ; then
  curl -q https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python2 get-pip.py --user virtualenv
  rm get-pip.py
fi

if [ ! -f "$VENV/bin/conan" ] ; then
  ~/.local/bin/virtualenv "$VENV"
  pip install conan
  conan remote add -f sailfishos https://api.bintray.com/conan/r1tschy/sailfishos
fi

source "$VENV/bin/activate"

# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# >> files
# << files
