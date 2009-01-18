%define		snap	20090118
Summary:	GNU Portability Library
Summary(pl.UTF-8):	biblioteka przenośności GNU
Name:		gnulib
Version:	0
Release:	0.%{snap}.1
License:	GPL
Group:		Development
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	52857c69c2f671b1e9bdc6bd9acacf84
Source1:	%{name}-tool.1
Source2:	%{name}-check-module.1
URL:		http://www.gnu.org/software/gnulib/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%setup -q -n %{name}-%{snap}
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
%{_mandir}/man1/*.1*
