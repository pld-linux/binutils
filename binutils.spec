#
# conditional build:
# _with_allarchs	- enable
#
Summary:	GNU Binary Utility Development Utilities
Summary(de):	GNU Binary Utility Development Utilities
Summary(es):	Utilitarios para desarrollo de binarios de la GNU
Summary(fr):	Utilitaires de dИveloppement binaire de GNU
Summary(pl):	NarzЙdzia GNU dla programistСw
Summary(pt_BR):	UtilitАrios para desenvolvimento de binАrios da GNU
Summary(ru):	Набор инструментов GNU для построения исполняемых программ
Summary(tr):	GNU geliЧtirme araГlarЩ
Summary(uk):	Наб╕р ╕нструмент╕в GNU для побудови виконуваних програм
Name:		binutils
Version:	2.13.90.0.16
Release:	1
Epoch:		2
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.kernel.org/pub/linux/devel/binutils/%{name}-%{version}.tar.bz2
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-info.patch
Patch1:		%{name}-sparc-nonpic.patch
Patch2:		%{name}-ia64-brl.patch
Patch3:		%{name}-rodata-cst.patch
Patch4:		%{name}-eh-frame-ro.patch
Patch5:		%{name}-ppc-apuinfo.patch
Patch6:		%{name}-stt_tls.patch
Patch7:		%{name}-ia64-bootstrap.patch
Patch8:		%{name}-tls-strip.patch
Patch9:		%{name}-ia64-tls.patch
Patch10:	%{name}-alpha-plt.patch
Patch11:	%{name}-ia64-tls2.patch
Patch12:	%{name}-array-sects-compat.patch
URL:		http://sources.redhat.com/binutils/
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	perl-devel
%ifarch sparc sparc32
BuildRequires:	sparc32
%endif
Requires(post,postun):	/sbin/ldconfig
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

%description -l pl
Pakiet binutils zawiera zestaw narzЙdzi umo©liwiaj╠cych kompilacjЙ
programСw. Znajduj╠ siЙ tutaj miЙdzy innymi assembler, konsolidator
(linker), a tak©e inne narzЙdzia do manipulowania binarnymi plikami
programСw i bibliotek.

%description -l es
binutils es una colectАnea de utilitarios necesarios para compilar
programas. Incluye assembler y linker, asМ como varios otros programas
para trabajar con formatos que se puedan ejecutar.

%description -l pt_BR
binutils И uma coletБnea de utilitАrios necessАrios para compilar
programas. Inclui assembler e linker, assim como vАrios outros
programas para trabalhar com formatos executАveis.

%description -l ru
binutils - это набор инструментов, необходимых для компилляции
программ. Включает ассемблер, компоновщик и набор других программ для
работы с исполняемыми файлами разнообразных форматов.

%description -l uk
binutils - це наб╕р ╕нструмент╕в, необх╕дних для комп╕ляц╕╖ програм.
М╕стить асемблер, компоновщик та ╕нш╕ програми, необх╕дн╕ для роботи з
виконуваними файлами р╕зних формат╕в.

%package static
Summary:	GNU Binutils static libraries
Summary(pl):	Biblioteki statyczne do GNU Binutils
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description static
Static libraries for GNU Binutils.

%description static -l pl
Biblioteki statyczne GNU Binutils.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%ifarch %{ix86}
%patch12 -p1
%endif

%build
cp -f /usr/share/automake/config.* .
CFLAGS="%{rpmcflags}"; export CFLAGS
CC="%{__cc}"; export CC
%ifarch sparc
sparc32 \
%endif
./configure %{_target_platform} \
	--enable-shared \
	--disable-debug \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
%ifarch sparc
	--enable-targets=sparc64-linux \
%endif
	%{?_with_allarchs:--enable-64-bit-bfd} \
	%{?_with_allarchs:--enable-targets=alpha-linux,arm-linux,cris-linux,hppa-linux,i386-linux,ia64-linux,m68k-linux,mips-linux,mips64-linux,mips64el-linux,mipsel-linux,ppc-linux,s390-linux,s390x-linux,sh-linux,sparc-linux,sparc64-linux,i386-linuxaout}

%{__make} tooldir=%{_prefix} all info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

%{__make} install install-info \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	tooldir=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	libdir=$RPM_BUILD_ROOT%{_libdir}

# these are already in gcc-g++
rm -f $RPM_BUILD_ROOT%{_bindir}/c++filt $RPM_BUILD_ROOT%{_mandir}/man1/c++filt*

rm -f $RPM_BUILD_ROOT%{_infodir}/standards.info*

# remove these man pages unless we cross-build for win*/netware platforms.
# however, this should be done in Makefiles.
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/{dlltool,nlmconv,windres}.1

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

install include/libiberty.h $RPM_BUILD_ROOT%{_includedir}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/libiberty.a
%{_libdir}/lib*.la

%{_libdir}/ldscripts
%{_includedir}/*.h

%{_infodir}/*info*
%{_mandir}/man1/*
%lang(cs) %{_mandir}/cs/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib[^i]*.a
