Summary:	GNU Binary Utility Development Utilities
Summary(de):	GNU Binary Utility Development Utilities
Summary(fr):	Utilitaires de développement binaire de GNU
Summary(pl):	Narzêdzia GNU dla programistów
Summary(tr):	GNU geliþtirme araçlarý
Name:		binutils
Version:	2.10.1.0.7
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	ftp://ftp.varesearch.com/pub/support/hjl/binutils/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
URL:		http://sourceware.cygnus.com/binutils/
Prereq:		/sbin/ldconfig
BuildRequires:	flex
BuildRequires:	bison
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
- c++filt - a filter for demangling encoded C++ symbols,
- addr2line - convert addresses to file and line,
- nlmconv - convert object code into an NLM.

%description -l pl
Pakiet binutils zawiera zestaw narzêdzi umo¿liwiaj±cych kompilacjê
programów. Znajduj± siê tutaj miêdzy innymi assembler, konsolidator
(linker), a tak¿e inne narzêdzia do manipulowania binarnymi plikami
programów i bibliotek.

%package static
Summary:	GNU Binutils static libraries
Summary(pl):	Biblioteki statyczne do GNU Binutils
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
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
CFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-g -O0}"
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

rm -f $RPM_BUILD_ROOT%{_bindir}/c++filt 

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

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
