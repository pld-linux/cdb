Summary:	Constant DataBase
Summary(pl):	Sta³a baza danych
Name:		cdb
Version:	0.75
Release:	1
License:	Public Domain
Group:		Applications/Databases
Source0:	http://cr.yp.to/cdb/%{name}-%{version}.tar.gz
# Source0-md5:	81fed54d0bde51b147dd6c20cdb92d51
Patch0:		%{name}-glibc.patch
URL:		http://cr.yp.to/cdb.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cdb is a fast, reliable, lightweight package for creating and reading
constant databases.

%description -l pl
cdb jest szybkim, wiarygodnym, ma³ym pakietem do tworzenia i czytania
sta³ych baz danych.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
echo "%{__cc} %{rpmcflags} %{rpmldflags}" >conf-ld
echo %{__cc} %{rpmcflags} >conf-cc
echo %{_prefix} > conf-home
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install cdbget cdbmake cdbdump cdbstats cdbtest \
	cdbmake-12 cdbmake-sv rts rts.tests testzero $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO SYSDEPS
%attr(755,root,root) %{_bindir}/*
