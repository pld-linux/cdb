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
constant databases. The database structure is tuned for fast reading:
- Successful lookups take normally just two disk accesses.
- Unsuccessful lookups take only one disk access.
- Small disk space and memory size requirements; a database uses 2048
  bytes for the header and 24 bytes per record plus the space for keys
  and data.
- Maximum database size is 4GB; individual record size is not
  otherwise limited.
- Portable file format.
- Fast database replacement.

%description -l pl
cdb jest szybkim, wiarygodnym, ma³ym pakietem do tworzenia i czytania
sta³ych baz danych. Struktura bazy zosta³a zoptymalizowana do
szybkiego odczytu:
- Udane odwo³ania normalnie potrzebuj± tylko dwóch odwo³añ do dysku.
- Nieudane odwo³ania potrzebuj± tylko jednego odwo³ania do dysku.
- Ma³e wymagania co do miejsca do dysku i pamiêci; baza danych u¿ywa
  2048 bajtów na nag³ówek i 24 bajtów na rekord plus miejsce na klucze
  i dane.
- Maksymalny rozmiar bazy to 4GB; rozmiar pojedynczego rekordu nie ma
  innych ograniczeñ.
- Przeno¶ny format pliku.
- Szybkie zastêpowanie baz nowo utworzonymi.

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
