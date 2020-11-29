# TODO: PR/26302 <https://sourceware.org/bugzilla/show_bug.cgi?id=26302> (breaks kernel-tools build)
#
# Conditional build:
%bcond_with	allarchs	# enable all targets
# define addtargets x,y,z	# build with additional targets x,y,z (e.g. x86_64-linux)
				# http://sourceware.org/ml/binutils/2008-03/msg00162.html
%bcond_with	pax		# without PaX flags (for upstream bugreports)
%bcond_without	gold		# don't build gold (no C++ dependencies)
%bcond_without	default_bfd	# default ld.bfd instead of gold
%bcond_without	gasp		# gasp
%bcond_with	tests		# check target

%ifnarch %{ix86} %{x8664} x32 aarch64 %{arm}
%undefine	with_gold
%endif
%ifarch %{arm}
%undefine	with_gasp
%endif

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
Version:	2.35.1
Release:	1
Epoch:		4
License:	GPL v3+
Group:		Development/Tools
Source0:	https://ftp.gnu.org/gnu/binutils/%{name}-%{version}.tar.lz
# Source0-md5:	701103b50966364eadff838f5a5df928
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	a717d9707ec77d82acb6ec9078c472d6
Patch0:		%{name}-gasp.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-libtool-relink.patch
Patch3:		%{name}-pt_pax_flags.patch

Patch6:		%{name}-absolute-gnu_debuglink-path.patch
Patch7:		%{name}-libtool-m.patch
Patch8:		%{name}-build-id.patch
Patch9:		%{name}-tooldir.patch
Patch10:	%{name}-sanity-check.patch
Patch11:	binutils-CVE-2019-1010204.patch
URL:		http://sources.redhat.com/binutils/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-tools
%{?with_gold:BuildRequires:	libstdc++-devel >= 6:4.0-1}
%{?with_tests:BuildRequires:	libstdc++-static >= 6:4.0}
BuildRequires:	lzip
BuildRequires:	perl-tools-pod
%ifarch sparc sparc32
BuildRequires:	sparc32
%endif
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo >= 4.2
BuildRequires:	zlib-devel
%{?with_tests:BuildRequires:	zlib-static}
Conflicts:	gcc-c++ < 5:3.3
Conflicts:	modutils < 2.4.17
Conflicts:	rpmbuild(macros) < 1.660
Obsoletes:	binutils-gold
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
- addr2line - convert addresses to file and line.

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
#Requires:	zlib-static

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

%prep
%setup -q
%{?with_gasp:%patch0 -p1}
%patch1 -p1
%patch2 -p1
%{?with_pax:%patch3 -p1}

%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

# file contains hacks for ac 2.69 only
%{__rm} config/override.m4

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
%ifarch %{x8664}
TARGETS="x86_64-pep"
%endif
%ifarch x32
TARGETS="x86_64-linux,x86_64-pep"
%endif
%{?addtargets:TARGETS="%{addtargets}"}

cp -f /usr/share/automake/config.* .
CFLAGS="%{rpmcflags}"; export CFLAGS
CXXFLAGS="%{rpmcxxflags}"; export CXXFLAGS
CC="%{__cc}"; export CC
CXX="%{__cxx}"; export CXX
%ifarch sparc
sparc32 \
%endif
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--disable-debug \
	--disable-werror \
%ifarch sparc
	--enable-64-bit-bfd \
%else
	%{?with_allarchs:--enable-64-bit-bfd} \
%endif
	--enable-build-warnings=,-Wno-missing-prototypes \
	--enable-install-libiberty \
	--enable-lto \
	--enable-plugins \
	--enable-shared \
	%{?with_allarchs:--enable-targets=alpha-linux,arm-linux,cris-linux,hppa-linux,i386-linux,ia64-linux,x86_64-linux,x86_64-linux-gnux32,m68k-linux,mips-linux,mips64-linux,mips64el-linux,mipsel-linux,ppc-linux,s390-linux,s390x-linux,sh-linux,sparc-linux,sparc64-linux,i386-linuxaout,x86_64-pep} \
	%{!?with_allarchs:`[ -n "${TARGETS}" ] && echo "--enable-targets=${TARGETS}"`} \
	--with-tooldir=%{_prefix} \
	--with-zlib \
%if %{with gold}
	--enable-gold%{!?with_default_bfd:=default} --enable-ld%{?with_default_bfd:=default} \
%endif

%{__make} -j1

%{?with_tests:%{__make} -j1 check}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/bfd-plugins

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# remove these man pages unless we cross-build for win*/netware platforms.
# however, this should be done in Makefiles.
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/{dlltool,windmc,windres}.1

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

# overwrite libiberty.a with PIC version
cp -pf libiberty/pic/libiberty.a $RPM_BUILD_ROOT%{_libdir}

# remove evil -L pointing inside builder's home
perl -pi -e 's@-L[^ ]*/pic @@g' $RPM_BUILD_ROOT%{_libdir}/libbfd.la

[ -x $RPM_BUILD_ROOT%{_bindir}/ld.bfd ] || ln $RPM_BUILD_ROOT%{_bindir}/ld{,.bfd}

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%find_lang bfd
%find_lang binutils
%find_lang gas
%find_lang gprof
touch ld.lang gold.lang
%find_lang ld
%if %{with gold}
%find_lang gold
%endif
%find_lang opcodes
cat bfd.lang opcodes.lang > %{name}-libs.lang
cat gas.lang gprof.lang ld.lang gold.lang >> %{name}.lang

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

%post	gasp -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	gasp -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%{?with_gold:%doc gold/{ChangeLog,README,TODO}}
%attr(755,root,root) %{_bindir}/addr2line
%attr(755,root,root) %{_bindir}/ar
%attr(755,root,root) %{_bindir}/as
%attr(755,root,root) %{_bindir}/c++filt
%attr(755,root,root) %{_bindir}/elfedit
%attr(755,root,root) %{_bindir}/gprof
%attr(755,root,root) %{_bindir}/ld
%attr(755,root,root) %{_bindir}/ld.bfd
%if %{with gold}
%attr(755,root,root) %{_bindir}/ld.gold
%attr(755,root,root) %{_bindir}/dwp
%endif
%attr(755,root,root) %{_bindir}/nm
%attr(755,root,root) %{_bindir}/objcopy
%attr(755,root,root) %{_bindir}/objdump
%attr(755,root,root) %{_bindir}/ranlib
%attr(755,root,root) %{_bindir}/readelf
%attr(755,root,root) %{_bindir}/size
%attr(755,root,root) %{_bindir}/strings
%attr(755,root,root) %{_bindir}/strip
%{_prefix}/lib/ldscripts
%{_infodir}/as.info*
%{_infodir}/binutils.info*
%{_infodir}/gprof.info*
%{_infodir}/ld.info*
%{_mandir}/man1/addr2line.1*
%{_mandir}/man1/ar.1*
%{_mandir}/man1/as.1*
%{_mandir}/man1/c++filt.1*
%{_mandir}/man1/elfedit.1*
%{_mandir}/man1/gprof.1*
%{_mandir}/man1/ld.1*
%{_mandir}/man1/nm.1*
%{_mandir}/man1/objcopy.1*
%{_mandir}/man1/objdump.1*
%{_mandir}/man1/ranlib.1*
%{_mandir}/man1/readelf.1*
%{_mandir}/man1/size.1*
%{_mandir}/man1/strings.1*
%{_mandir}/man1/strip.1*
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
%attr(755,root,root) %{_libdir}/libbfd-%{version}.so
%attr(755,root,root) %{_libdir}/libctf.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libctf.so.0
%attr(755,root,root) %{_libdir}/libctf-nobfd.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libctf-nobfd.so.0
%attr(755,root,root) %{_libdir}/libopcodes-%{version}.so
%dir %{_libdir}/bfd-plugins

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbfd.so
%attr(755,root,root) %{_libdir}/libctf.so
%attr(755,root,root) %{_libdir}/libctf-nobfd.so
%attr(755,root,root) %{_libdir}/libopcodes.so
%{_libdir}/libbfd.la
%{_libdir}/libctf.la
%{_libdir}/libctf-nobfd.la
%{_libdir}/libopcodes.la
%{_libdir}/libiberty.a
%{_includedir}/ansidecl.h
%{_includedir}/bfd.h
%{_includedir}/bfd_stdint.h
%{_includedir}/bfdlink.h
%{_includedir}/ctf-api.h
%{_includedir}/ctf.h
%{_includedir}/diagnostics.h
%{_includedir}/dis-asm.h
%{_includedir}/plugin-api.h
%{_includedir}/symcat.h
%{_includedir}/libiberty
%{_infodir}/bfd.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libbfd.a
%{_libdir}/libctf.a
%{_libdir}/libctf-nobfd.a
%{_libdir}/libopcodes.a

%if %{with gasp}
%files gasp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gasp
%{_infodir}/gasp.info*
%endif
