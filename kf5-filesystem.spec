# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kf5-filesystem

# >> macros
# << macros

Summary:    Filesystem and RPM macros for KDE Frameworks 5
Version:    4.99.0
Release:    1
Group:      System/Base
License:    BSD
BuildArch:  noarch
URL:        http://www.kde.org
Source0:    macros.kf5
Source100:  kf5-filesystem.yaml

%description
Filesystem and RPM macros for KDE Frameworks 5.

%package -n kf5-rpm-macros
Summary:    RPM macros for KDE Frameworks 5
Group:      Development/System
Requires:   %{name} = %{version}-%{release}
Requires:   qt5-qmake

%description -n kf5-rpm-macros
RPM macros for building KDE Frameworks 5 packages.

%prep
# No setup

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre

# >> install post
# See macros.kf5 where the directories are specified
mkdir -p %{buildroot}%{_libdir}/qt5/plugins/kf5
mkdir -p %{buildroot}%{_includedir}/KF5
mkdir -p %{buildroot}%{_libexecdir}/kf5

mkdir -p %{buildroot}%{_sysconfdir}/rpm/
install -pm644 %{_sourcedir}/macros.kf5 %{buildroot}%{_sysconfdir}/rpm/
# << install post

%files
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/kf5
%{_includedir}/KF5
%{_libexecdir}/kf5
# >> files
# << files

%files -n kf5-rpm-macros
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/rpm/macros.kf5
# >> files kf5-rpm-macros
# << files kf5-rpm-macros
