Summary:	Constant DataBase
Summary(pl.UTF-8):	Stała baza danych
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

%description -l pl.UTF-8
cdb jest szybkim, wiarygodnym, małym pakietem do tworzenia i czytania
stałych baz danych. Struktura bazy została zoptymalizowana do
szybkiego odczytu:
- Udane odwołania normalnie potrzebują tylko dwóch odwołań do dysku.
- Nieudane odwołania potrzebują tylko jednego odwołania do dysku.
- Małe wymagania co do miejsca do dysku i pamięci; baza danych używa
  2048 bajtów na nagłówek i 24 bajtów na rekord plus miejsce na klucze
  i dane.
- Maksymalny rozmiar bazy to 4GB; rozmiar pojedynczego rekordu nie ma
  innych ograniczeń.
- Przenośny format pliku.
- Szybkie zastępowanie baz nowo utworzonymi.

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
