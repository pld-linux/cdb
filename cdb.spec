Summary:	Constant DataBase
Summary(pl):	Sta�a baza danych
Name:		cdb 
Version:	0.75 
Release:	1
License:	Public Domain 
Group:		Applications/Databases
Source0:	http://cr.yp.to/cdb/%{name}-%{version}.tar.gz
URL:		http://pobox.com/~djb/cdb.html 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cdb is a fast, reliable, lightweight package for creating and reading
constant databases.

%description -l pl
cdb jest szybkim, wiarygodnym, ma�ym pakietem do tworzenia i czytania
sta�ych baz danych.

%prep
%setup -q

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
gzip -9nf CHANGES README TODO SYSDEPS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc *.gz 