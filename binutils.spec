Summary:	GNU Binary Utility Development Utilities
Summary(pl):	Narzêdzia GNU dla programistów
Name:		binutils
Version:	2.9.1.0.25
Release:	2
Copyright:	GPL
Group:		Development/Tools
Group(pl):	Programowanie/Narzêdzia
URL:		ftp://ftp.varesearch.com/pub/support/hjl/binutils
Source:		%{name}-%{version}.tar.gz
Patch0:		binutils-info.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
binutils is a collection of utilities necessary for compiling programs. It
includes the assembler and linker, as well as a number of other
miscellaneous programs for dealing with executable formats.

%description -l pl
Pakiet binutils zawiera zestaw narzêdzi umo¿liwiaj±cych kompilacjê programów. 
Znajduj± siê tutaj miêdzy innymi assembler, konsolidator (linker), a tak¿e 
inne narzêdzia do manipulowania binarnymi plikami programów i bibliotek.

%package	static
Summary:	GNU Binutils static libraries
Summary(pl):	Biblioteki statyczne do GNU Binutils
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description static
Static libraries for GNU Binutils.

%description -l pl static
Biblioteki statyczne GNU Binutils.

%prep
%setup -q 
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
%ifarch sparc sparc64
sparc32 \
%endif
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--enable-shared \
	--disable-debug \
	--infodir=%{_infodir}

make tooldir=%{_prefix} all info

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}

make install install-info \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	tooldir=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir}

rm -f $RPM_BUILD_ROOT%{_bindir}/c++filt 

strip $RPM_BUILD_ROOT%{_bindir}/*
strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so

install include/libiberty.h $RPM_BUILD_ROOT%{_includedir}

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/*.inf*,%{_mandir}/man1/*} \
	README

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info %{_infodir}/as.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/bfd.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/binutils.info.gz /etc/info-dir 
/sbin/install-info %{_infodir}/ld.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/gasp.info.gz /etc/info-dir 
/sbin/install-info %{_infodir}/gprof.info.gz /etc/info-dir 
/sbin/ldconfig

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/as.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/bfd.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/binutils.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/ld.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/gasp.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/gprof.info.gz /etc/info-dir
fi

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so

%{_libdir}/ldscripts
%{_includedir}/*.h

%{_infodir}/*.gz
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)

%{_libdir}/lib*.a

%changelog
* Tue May 25 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.9.1.0.25-1]
- spec based on RH version,
- rewrited by PLD team,
- pl translation Wojtek ¦lusarczyk <wojtek@shadow.eu.org>.
