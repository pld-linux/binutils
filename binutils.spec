Summary:	GNU Binary Utility Development Utilities
Summary(pl):	Narzêdzia GNU dla programistów
Name:		binutils
Version:	2.9.1.0.24
Release:	1
Copyright:	GPL
Group:		Development/Tools
Group(pl):	Programowanie/Narzêdzia
Source:		ftp://ftp.varesearch.com/pub/support/hjl/binutils/%{name}-%{version}.tar.gz
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

%package static
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
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
%ifarch sparc sparc64
sparc32 ./configure %{_target} \
%else
./configure %{_target} \
	--prefix=/usr \
	--enable-shared \
	--disable-debug \
	%{_target_cpu}-pld-linux
%endif

make tooldir=/usr all info

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr

make install install-info \
	prefix=$RPM_BUILD_ROOT/usr \
	tooldir=$RPM_BUILD_ROOT/usr

gzip -9nf $RPM_BUILD_ROOT/usr/info/*.inf*

strip $RPM_BUILD_ROOT/usr/bin/*

install include/libiberty.h $RPM_BUILD_ROOT/usr/include

gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/* \
	README

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/as.info.gz /etc/info-dir
/sbin/install-info /usr/info/bfd.info.gz /etc/info-dir
/sbin/install-info /usr/info/binutils.info.gz /etc/info-dir 
/sbin/install-info /usr/info/ld.info.gz /etc/info-dir
/sbin/install-info /usr/info/gasp.info.gz /etc/info-dir 
/sbin/install-info /usr/info/gprof.info.gz /etc/info-dir 
/sbin/ldconfig

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete /usr/info/as.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/bfd.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/binutils.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/ld.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/gasp.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/gprof.info.gz /etc/info-dir
fi

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /usr/bin/*
%attr(755,root,root) /usr/lib/*.so

/usr/lib/ldscripts
/usr/include/*.h

/usr/info/*.gz

/usr/lib/libiberty.a
/usr/man/man1/*

%files static
%defattr(644,root,root)
/usr/lib/libbfd.a
/usr/lib/libopcodes.a

%changelog
* Thu Apr 22 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.9.1.0.23-2]
- recompiles on new rpm.

* Wed Apr  7 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.9.1.0.23-1]
- standarized {un}registering info pages (added binutils-info.patch).

* Thu Feb 18 1999 Micha³ Kuratczyk <kura@wroclaw.art.pl>
  [2.9.1.0.19-5d]
- gzipping instead bzipping
- added LDFLAGS=-s
- minor changes

* Mon Jan 18 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.9.1.0.19-4d]
- fixed %preun && %post,
- commpresed %doc,
- added Group(pl),
- added Prereq: /sbin/ldconfig,
- added URL,

  by Maciek W. Ró¿ycki <macro@ds2.pg.gda.pl>    

- fixed the binary BFD to correctly output sections,
- modified gas so it recognizes single-argument aad and aam,
- modified gas so iret generates a non-prefixed opcode
  regardless of the current argument size.
- added support for new Pentium II instructions (see "Addendum
  -- Intel Architecture Software Developer's Manual, Volume 2:
  Instruction Set Reference", order number 243689-001),
- fixed a problem with relative branch distance overflow checking,
- added a fix for 16-bit PC-relative relocations on i386.

* Sun Dec 20 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.9.1.0.19-2d]
- removed static subpackages,
- cosmetic changes,
- final build for Tornado.

* Wed Dec  8 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.9.1.0.17-2] 
- added using sparc32 for run ./configure script on sparc
  architecture (thanks DaveM).

* Fri Oct  9 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.9.1.0.15-2]
- /usr/lib/libiberty.a moved to main.

* Sat Oct 03 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.9.1.0.15-1d]
- fixed pl translation,
- updated to 2.9.1.0.15.

* Sun Sep 13 1998 Wojtek ¦lusarczyk <wojtek@SHADOW.EU.ORG>
  [2.9.1.0.12-1d]
- updated to 2.9.1.0.12.
- install -d instead mkdir -p,
- restricted ELF binaries permissions.

* Tue Sep 07 1998 Wojtek ¦lusarczyk <wojtek@SHADOW.EU.ORG>
  [2.9.1.0.11-1d]
- updated to 2.9.1.0.11,
- build without $RPM_OPT_FLAGS - some problems with egcs & -O6 ...
- added a static package,
- build from non root's account.

* Sat Aug 22 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.9.1.0.10-3]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- removed /usr/lib/lib*.la files,
- added using $RPM_OPT_FLAGS during building package.

* Fri Jun 12 1998 Wojtek ¦lusarczyk <wojtek@SHADOW.EU.ORG>
  [2.9.1.0.6-2]
- build against GNU libc-2.1.

* Fri May 29 1998 Wojtek ¦lusarczyk <wojtek@SHADOW.EU.ORG>
- Replaced binutils to binutils-2.9.1.0.6,
- start at RH spec file.
