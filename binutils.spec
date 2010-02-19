#
# Conditional build:
%bcond_with	allarchs	# enable all targets
# define addtargets x,y,z	# build with additional targets x,y,z (e.g. x86_64-linux)
				# http://sourceware.org/ml/binutils/2008-03/msg00162.html
%bcond_without	gold		# don't build gold (no C++ dependencies)
%bcond_without	pax		# without PaX flags (for upstream bugreports)
#
Summary:	GNU Binary Utility Development Utilities
Summary(de.UTF-8):	GNU Binary Utility Development Utilities
Summary(es.UTF-8):	Utilitarios para desarrollo de binarios de la GNU
Summary(fr.UTF-8):	Utilitaires de développement binaire de GNU
Summary(pl.UTF-8):	Narzędzia GNU dla programistów
Summary(pt_BR.UTF-8):	Utilitários para desenvolvimento de binários da GNU
Summary(ru.UTF-8):	Набор инструментов GNU для построения исполняемых программ
Summary(tr.UTF-8):	GNU geliştirme araçları
Summary(uk.UTF-8):	Набір інструментів GNU для побудови виконуваних програм
Name:		binutils
Version:	2.20.51.0.6
Release:	1
Epoch:		3
License:	GPL v3+
Group:		Development/Tools
Source0:	ftp://ftp.kernel.org/pub/linux/devel/binutils/%{name}-%{version}.tar.bz2
# Source0-md5:	8a5b135a6dcdd891a32a7c67bb401fe8
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	a717d9707ec77d82acb6ec9078c472d6
Patch0:		%{name}-gasp.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-libtool-relink.patch
Patch3:		%{name}-pt_pax_flags.patch
Patch5:		%{name}-discarded.patch
Patch6:		%{name}-absolute-gnu_debuglink-path.patch
Patch7:		%{name}-libtool-m.patch
Patch8:		%{name}-build-id.patch
Patch9:		%{name}-tooldir.patch
URL:		http://sources.redhat.com/binutils/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
%{?with_gold:BuildRequires:	libstdc++-devel >= 6:4.0-1}
BuildRequires:	perl-tools-pod
%ifarch sparc sparc32
BuildRequires:	sparc32
%endif
BuildRequires:	texinfo >= 4.2
Conflicts:	gcc-c++ < 5:3.3
Conflicts:	modutils < 2.4.17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Binutils is a collection of binary utilities, including:
- ar - create, modify and extract from archives,
- nm - lists symbols from object files,
- objcopy - copy and translate object files,
- objdump - display information from object files,
- ranlib - generate an index for the contents of an archive,
- size - list the section sizes of an object or archive file,
- strings - list printable strings from files,
- strip - discard symbols,
- addr2line - convert addresses to file and line,
- nlmconv - convert object code into an NLM.

%description -l es.UTF-8
Binutils es una colección de utilitarios necesarios para compilar
programas. Incluye assembler y linker, así como varios otros programas
para trabajar con formatos que se puedan ejecutar.

%description -l pl.UTF-8
Pakiet binutils zawiera zestaw narzędzi umożliwiających kompilację
programów. Znajdują się tutaj między innymi assembler, konsolidator
(linker), a także inne narzędzia do manipulowania binarnymi plikami
programów i bibliotek.

%description -l pt_BR.UTF-8
binutils é uma coletânea de utilitários necessários para compilar
programas. Inclui assembler e linker, assim como vários outros
programas para trabalhar com formatos executáveis.

%description -l ru.UTF-8
binutils - это набор инструментов, необходимых для компилляции
программ. Включает ассемблер, компоновщик и набор других программ для
работы с исполняемыми файлами разнообразных форматов.

%description -l uk.UTF-8
binutils - це набір інструментів, необхідних для компіляції програм.
Містить асемблер, компоновщик та інші програми, необхідні для роботи з
виконуваними файлами різних форматів.

%package libs
Summary:	GNU binutils shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone GNU binutils
Group:		Libraries
Conflicts:	binutils < 3:2.17.50.0.8-3

%description libs
GNU binutils shared libraries (libbfd, libopcodes).

%description libs -l pl.UTF-8
Biblioteki współdzielone GNU binutils (libbfd, libopcodes).

%package devel
Summary:	Development files for GNU binutils libraries
Summary(pl.UTF-8):	Pliki programistyczne bibliotek GNU binutils
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
Development files for GNU binutils libraries (libbfd, libopcodes) and
static libiberty library.

%description devel -l pl.UTF-8
Pliki programistyczne bibliotek GNU binutils (libbfd, libopcodes) oraz
statyczna biblioteka libiberty.

%package static
Summary:	GNU binutils static libraries
Summary(pl.UTF-8):	Biblioteki statyczne do GNU binutils
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static GNU binutils libraries (libbfd, libopcodes).

%description static -l pl.UTF-8
Biblioteki statyczne GNU binutils (libbfd, libopcodes).

%package gasp
Summary:	GASP - old preprocessor for assembly programs
Summary(pl.UTF-8):	GASP - stary preprocesor dla programów w asemblerze
Group:		Development/Tools
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gasp
GASP - old preprocessor for assembly programs. It's officially
obsoleted, but it's still needed to build some packages.

%description gasp -l pl.UTF-8
GASP - stary preprocesor dla programów w asemblerze. Jest oficjalnie
uznany za przestarzały, ale jest nadal potrzebny do zbudowania
niektórych pakietów.

%package gold
Summary:	GOLD - new version of ELF linker originally developed at Google
Summary(pl.UTF-8):	GOLD - nowa wersja linkera ELF powstała w Google
Group:		Development/Tools
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gold
gold is an ELF linker. It is intended to have complete support for ELF
and to run as fast as possible on modern systems. For normal use it is
a drop-in replacement for the older GNU linker. gold was originally
developed at Google, and was contributed to the Free Software
Foundation in March 2008.

gold supports most of the features of the GNU linker for ELF targets.
Notable omissions - features of the GNU linker not currently supported
in gold - are:
 - MEMORY regions in linker scripts
 - MRI compatible linker scripts
 - cross-reference reports (--cref)
 - various other minor options.

%description gold -l pl.UTF-8
gold to linker dla plików ELF. Powstał z myślą o pełnej obsłudze
formatu ELF i jak najszybszym działaniu na współczesnych systemach.
Przy zwykłym użyciu jest zamiennikiem starszego linkera GNU. gold
początkowo był rozwijany przez Google i został przekazany Free
Software Foundation w marcu 2008.

gold obsługuje większość funkcji linkera GNU dla plików ELF. Istotne
braki - możliwości linkera GNU aktualnie nie obsługiwane przez gold -
to:
- regiony typu MEMORY w skryptach linkera
- skrypty linkera kompatybilne z MRI
- raporty odsyłaczy (--cref)
- kilka innych, mniej istotnych opcji.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{?with_pax:%patch3 -p1}
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

# file contains hacks for ac 2.59 only
rm config/override.m4

%build
%{__aclocal}
%{__autoconf}

# non-standard regeneration (needed because of gasp patch)
# AM_BINUTILS_WARNINGS in bfd/warning.m4, ZW_GNU_GETTEXT_SISTER_DIR in config/gettext-sister.m4
for dir in gas bfd; do
	cd $dir || exit 1
	%{__aclocal} -I .. -I ../config -I ../bfd
	%{__automake} Makefile
	%{__automake} doc/Makefile
	%{__autoconf}
	cd ..
done

# More targets
TARGETS=
%ifarch ia64
TARGETS=i686-linux
%endif
# uhm?
%ifarch %{ix86}
TARGETS=x86_64-linux
%endif
%ifarch sparc
TARGETS=sparc64-linux
%endif
%{?addtargets:TARGETS="%{addtargets}"}

cp -f /usr/share/automake/config.* .
CFLAGS="%{rpmcflags}"; export CFLAGS
CC="%{__cc}"; export CC
%ifarch sparc
sparc32 \
%endif
./configure %{_target_platform} \
	--disable-debug \
	--disable-werror \
	--enable-build-warnings=,-Wno-missing-prototypes \
	--enable-shared \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--with-tooldir=%{_prefix} \
	%{!?with_allarchs:`[ -n "${TARGETS}" ] && echo "--enable-targets=${TARGETS}"`} \
%ifarch sparc
	--enable-64-bit-bfd \
%else
	%{?with_allarchs:--enable-64-bit-bfd} \
%endif
	%{?with_allarchs:--enable-targets=alpha-linux,arm-linux,cris-linux,hppa-linux,i386-linux,ia64-linux,x86_64-linux,m68k-linux,mips-linux,mips64-linux,mips64el-linux,mipsel-linux,ppc-linux,s390-linux,s390x-linux,sh-linux,sparc-linux,sparc64-linux,i386-linuxaout} \
%if %{with gold}
	--enable-gold=both/bfd
%else
	--disable-gold
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_infodir}/standards.info*

# remove these man pages unless we cross-build for win*/netware platforms.
# however, this should be done in Makefiles.
rm $RPM_BUILD_ROOT%{_mandir}/man1/{dlltool,nlmconv,windres}.1

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

install include/libiberty.h $RPM_BUILD_ROOT%{_includedir}
install libiberty/pic/libiberty.a $RPM_BUILD_ROOT%{_libdir}

# remove evil -L pointing inside builder's home
perl -pi -e 's@-L[^ ]*/pic @@g' $RPM_BUILD_ROOT%{_libdir}/libbfd.la

[ -x $RPM_BUILD_ROOT%{_bindir}/ld.bfd ] || ln $RPM_BUILD_ROOT%{_bindir}/ld{,.bfd}

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%find_lang bfd
%find_lang binutils
%find_lang gas
%find_lang gprof
touch ld.lang
%find_lang ld
%if %{with gold}
%find_lang gold
%endif
%find_lang opcodes
cat bfd.lang opcodes.lang > %{name}-libs.lang
cat gas.lang gprof.lang ld.lang >> %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/addr2line
%attr(755,root,root) %{_bindir}/ar
%attr(755,root,root) %{_bindir}/as
%attr(755,root,root) %{_bindir}/c++filt
%attr(755,root,root) %{_bindir}/elfedit
%attr(755,root,root) %{_bindir}/gprof
%attr(755,root,root) %{_bindir}/ld
%attr(755,root,root) %{_bindir}/ld.bfd
%attr(755,root,root) %{_bindir}/nm
%attr(755,root,root) %{_bindir}/objcopy
%attr(755,root,root) %{_bindir}/objdump
%attr(755,root,root) %{_bindir}/ranlib
%attr(755,root,root) %{_bindir}/readelf
%attr(755,root,root) %{_bindir}/size
%attr(755,root,root) %{_bindir}/strings
%attr(755,root,root) %{_bindir}/strip
%{_infodir}/as.info*
%{_infodir}/binutils.info*
%{_infodir}/configure.info*
%{_infodir}/gprof.info*
%{_infodir}/ld.info*
%{_prefix}/lib/ldscripts
%{_mandir}/man1/*
%lang(cs) %{_mandir}/cs/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%files libs -f %{name}-libs.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbfd-*.so
%attr(755,root,root) %{_libdir}/libopcodes-*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbfd.so
%attr(755,root,root) %{_libdir}/libopcodes.so
%{_libdir}/libbfd.la
%{_libdir}/libopcodes.la
%{_libdir}/libiberty.a
%{_includedir}/ansidecl.h
%{_includedir}/bfd.h
%{_includedir}/bfdlink.h
%{_includedir}/dis-asm.h
%{_includedir}/libiberty.h
%{_includedir}/symcat.h
%{_infodir}/bfd.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libbfd.a
%{_libdir}/libopcodes.a

%files gasp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gasp
%{_infodir}/gasp.info*

%if %{with gold}
%files gold -f gold.lang
%defattr(644,root,root,755)
%doc gold/{ChangeLog,README,TODO}
%attr(755,root,root) %{_bindir}/ld.gold
%endif
