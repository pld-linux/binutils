Summary:	GNU Binary Utility Development Utilities
Summary(de):	GNU Binary Utility Development Utilities
Summary(es):	Utilitarios para desarrollo de binarios de la GNU
Summary(fr):	Utilitaires de d�veloppement binaire de GNU
Summary(pl):	Narz�dzia GNU dla programist�w
Summary(pt_BR):	Utilit�rios para desenvolvimento de bin�rios da GNU
Summary(tr):	GNU geli�tirme ara�lar�
Name:		binutils
Version:	2.11.92.0.5
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Source0:	ftp://ftp.kernel.org/pub/linux/devel/binutils/%{name}-%{version}.tar.bz2
Source1:	%{name}-non-english-man-pages.tar.gz
Patch0:		%{name}-info.patch
URL:		http://sourceware.cygnus.com/binutils/
Prereq:		/sbin/ldconfig
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	perl-devel
%ifarch sparc sparc32
BuildRequires:	sparc32
%endif
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
Pakiet binutils zawiera zestaw narz�dzi umo�liwiaj�cych kompilacj�
program�w. Znajduj� si� tutaj mi�dzy innymi assembler, konsolidator
(linker), a tak�e inne narz�dzia do manipulowania binarnymi plikami
program�w i bibliotek.

%description -l es
binutils es una colect�nea de utilitarios necesarios para compilar
programas. Incluye assembler y linker, as� como varios otros programas
para trabajar con formatos que se puedan ejecutar.

%description -l pt_BR
binutils � uma colet�nea de utilit�rios necess�rios para compilar
programas. Inclui assembler e linker, assim como v�rios outros
programas para trabalhar com formatos execut�veis.

%package static
Summary:	GNU Binutils static libraries
Summary(pl):	Biblioteki statyczne do GNU Binutils
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name} = %{version}

%description static
Static libraries for GNU Binutils.

%description -l pl static
Biblioteki statyczne GNU Binutils.

%prep
%setup -q 
%patch0 -p1

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
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
	--enable-targets=sparc64-linux
%endif

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

tar xzvf %{SOURCE1} -C $RPM_BUILD_ROOT%{_mandir}/

install include/libiberty.h $RPM_BUILD_ROOT%{_includedir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so

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
%{_libdir}/lib*.a
