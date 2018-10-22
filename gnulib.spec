%define		snap	20181013
%define		commit	6c3b072e6a48d45455b37420caf14b804cbba23c
Summary:	GNU Portability Library
Summary(pl.UTF-8):	Biblioteka przenośności GNU
Name:		gnulib
Version:	0
Release:	0.%{snap}.3
License:	GPL v2.0+/3.0+ (generally), LGPL v2.1+/3.0+ (some modules)
Group:		Development
Source0:	http://git.savannah.gnu.org/cgit/gnulib.git/snapshot/%{name}-%{commit}.tar.gz
# Source0-md5:	3b15e5f01d613b6c40ef5a8dab622a39
Source1:	%{name}-tool.1
Source2:	%{name}-check-module.1
Patch0:		%{name}-paths.patch
URL:		http://www.gnu.org/software/gnulib/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GNU portability library is a macro system and C declarations and
definitions for commonly-used API elements and abstracted system
behaviors. It can be used to improve portability and other
functionality in your programs.

%description -l pl.UTF-8
Biblioteka przenośności GNU to system makr i deklaracji oraz definicji
C dla często używanych elementów API. Biblioteka ta może być
wykorzystana w celu ulepszenia przeności oraz funkcjonalności
programów.

%prep
%setup -q -n %{name}-%{commit}
%patch0 -p1
sed -ie 's@\(^\| \)gnulib_dir=.*@\1gnulib_dir=%{_datadir}/gnulib@' gnulib-tool

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/gnulib,%{_mandir}/man1}
cp -a check-module gnulib-tool $RPM_BUILD_ROOT%{_bindir}
cp -a build-aux config doc lib m4 modules tests $RPM_BUILD_ROOT%{_datadir}/gnulib
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1/check-module.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog COPYING DEPENDENCIES NEWS
%attr(755,root,root) %{_bindir}/check-module
%attr(755,root,root) %{_bindir}/gnulib-tool
%{_datadir}/gnulib
%exclude %{_datadir}/gnulib/lib/uniname/gen-uninames.lisp
%{_mandir}/man1/check-module.1*
%{_mandir}/man1/gnulib-tool.1*
