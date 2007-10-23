#
# Conditional build:
%bcond_with	allarchs	# enable all targets
# define addtargets x,y,z	# build with additional targets x,y,z (e.g. x86_64-linux)
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
Version:	2.18.50.0.2
Release:	1
Epoch:		3
License:	GPL v3+
Group:		Development/Tools
Source0:	ftp://ftp.kernel.org/pub/linux/devel/binutils/%{name}-%{version}.tar.bz2
# Source0-md5:	ba4647b164a4700ca62e6eeb76cae4fc
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	a717d9707ec77d82acb6ec9078c472d6
Patch0:		%{name}-gasp.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-libtool-relink.patch
Patch3:		%{name}-pt_pax_flags.patch
Patch4:		%{name}-mips-relocs.patch
Patch5:		%{name}-flex.patch
Patch6:		%{name}-discarded.patch
Patch7:		%{name}-absolute-gnu_debuglink-path.patch
Patch8:		%{name}-libtool-m.patch
URL:		http://sources.redhat.com/binutils/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8.2
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	perl-tools-pod
%ifarch sparc sparc32
BuildRequires:	sparc32
%endif
BuildRequires:	texinfo >= 4.2
Requires(post,postun):	/sbin/ldconfig
Requires:	%{name} = %{epoch}:%{version}-%{release}
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

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{?with_pax:%patch3 -p1}
%patch4 -p0
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
# non-standard regeneration (needed because of gasp patch)
# AM_BINUTILS_WARNINGS in bfd/warning.m4, ZW_GNU_GETTEXT_SISTER_DIR in config/gettext-sister.m4
cd gas
aclocal -I ../bfd -I ../config -I ..
automake --cygnus Makefile
automake --cygnus doc/Makefile
autoconf
cd ..

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
CFLAGS="%{rpmcflags} -fno-strict-aliasing"; export CFLAGS
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
	%{!?with_allarchs:`[ -n "${TARGETS}" ] && echo "--enable-targets=${TARGETS}"`} \
%ifarch sparc
	--enable-64-bit-bfd \
%else
	%{?with_allarchs:--enable-64-bit-bfd} \
%endif
	%{?with_allarchs:--enable-targets=alpha-linux,arm-linux,cris-linux,hppa-linux,i386-linux,ia64-linux,x86_64-linux,m68k-linux,mips-linux,mips64-linux,mips64el-linux,mipsel-linux,ppc-linux,s390-linux,s390x-linux,sh-linux,sparc-linux,sparc64-linux,i386-linuxaout}

%{__make} -j1 configure-bfd
%{__make} -j1 headers -C bfd
%{__make} -j1 all info \
	tooldir=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	tooldir=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	libdir=$RPM_BUILD_ROOT%{_libdir}

rm -f $RPM_BUILD_ROOT%{_infodir}/standards.info*

# remove these man pages unless we cross-build for win*/netware platforms.
# however, this should be done in Makefiles.
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/{dlltool,nlmconv,windres}.1

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

install include/libiberty.h $RPM_BUILD_ROOT%{_includedir}
install libiberty/pic/libiberty.a $RPM_BUILD_ROOT%{_libdir}

# remove evil -L pointing inside builder's home
perl -pi -e 's@-L[^ ]*/pic @@g' $RPM_BUILD_ROOT%{_libdir}/libbfd.la

%find_lang bfd
%find_lang binutils
%find_lang gas
%find_lang gprof
%find_lang ld
%find_lang opcodes
cat bfd.lang opcodes.lang > %{name}-libs.lang
cat gas.lang gprof.lang ld.lang >> %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/[!g]*
%attr(755,root,root) %{_bindir}/g[!a]*
%{_prefix}/lib/ldscripts
%{_infodir}/as.info*
%{_infodir}/binutils.info*
%{_infodir}/configure.info*
%{_infodir}/gprof.info*
%{_infodir}/ld.info*
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
%{_includedir}/*.h
%{_infodir}/bfd.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libbfd.a
%{_libdir}/libopcodes.a

%files gasp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gasp
%{_infodir}/gasp.info*
