Summary:     GNU Binary Utility Development Utilities
Summary(de): GNU Binary Utility Development Utilities
Summary(fr): Utilitaires de développement binaire de GNU
Summary(pl): Narzêdzia GNU dla programistów
Summary(tr): GNU geliþtirme araçlarý
Name:        binutils
Version:     2.9.1.0.17
Release:     1
Copyright:   GPL
Group:       Development/Tools
Source       ftp://ftp.kernel.org/pub/linux/devel/gcc/%{name}-%{version}.tar.bz2
Patch0:      binutils-2.9.1-sparcsectionreloc.patch
Buildroot:   /tmp/%{name}-%{version}-root

%description
Binutils is a collection of utilities necessary for compiling programs. It
includes the assembler and linker, as well as a number of other
miscellaneous programs for dealing with executable formats.

%description -l pl
Pakiet binutils zawiera zestaw narzêdzi umo¿liwiaj±cych kompilacjê
programów. Zawiera on assembler, konsolidator (linker), a tak¿e inne narzêdzia
do manipulowania na binarnych plikach programów i bibliotek.

%package static
Summary:     GNU Binutils static libraries
Summary(pl): Biblioteki statyczne do GNU Binutils
Group:       Libraries

%description static
Static libraries for GNU Binutils.

%description -l pl static
Biblioteki statyczne do GNU Binutils.

%prep
%setup -q
(cd bfd;
%patch -p0 -b .secreloc
)

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr --enable-shared
make tooldir=/usr all info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr
make	install install-info \
	prefix=$RPM_BUILD_ROOT/usr \
	tooldir=$RPM_BUILD_ROOT/usr

strip $RPM_BUILD_ROOT/usr/{bin/*,lib/lib*.so.*.*}
gzip -q9f $RPM_BUILD_ROOT/usr/info/*.info*

install include/libiberty.h $RPM_BUILD_ROOT/usr/include

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/install-info --info-dir=/usr/info /usr/info/as.info.gz
/sbin/install-info --info-dir=/usr/info /usr/info/bfd.info.gz
/sbin/install-info --info-dir=/usr/info /usr/info/binutils.info.gz
/sbin/install-info --info-dir=/usr/info /usr/info/gasp.info.gz
/sbin/install-info --info-dir=/usr/info /usr/info/gprof.info.gz
/sbin/install-info --info-dir=/usr/info /usr/info/ld.info.gz
/sbin/install-info --info-dir=/usr/info /usr/info/standards.info.gz

%preun
/sbin/install-info --delete --info-dir=/usr/info /usr/info/as.info.gz
/sbin/install-info --delete --info-dir=/usr/info /usr/info/bfd.info.gz
/sbin/install-info --delete --info-dir=/usr/info /usr/info/binutils.info.gz
/sbin/install-info --delete --info-dir=/usr/info /usr/info/gasp.info.gz
/sbin/install-info --delete --info-dir=/usr/info /usr/info/gprof.info.gz
/sbin/install-info --delete --info-dir=/usr/info /usr/info/ld.info.gz
/sbin/install-info --delete --info-dir=/usr/info /usr/info/standards.info.gz

%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*
/usr/include/*
%attr(755, root, root) /usr/lib/lib*.so.*.*
/usr/lib/lib*.so
/usr/lib/ldscripts
/usr/info/*info*
/usr/lib/libiberty.a

%files static
%defattr(644, root, root)
/usr/lib/libbfd.a
/usr/lib/libopcodes.a

%changelog
* Mon Dec  9 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.9.1.0.17-1]
- added gzipping man pages,
- added using LDFLAGS="-s" to ./configure enviroment,
- changed base Source url to ftp:ftp.kernel.org/pub/linux/devel/gcc/.

* Fri Oct  9 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.9.1.0.14-2]
- /usr/lib/libiberty.a moved to main.

* Sat Aug 22 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.9.1.0.10-3]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- removed /usr/lib/lib*.la files,
- added using $RPM_OPT_FLAGS during building package,
- added striping shared libraries,
- added %attr and %defattr macros in %files (allow build package from
  non-root account).

* Thu Jul  2 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.9.1.0.7.

* Wed Jun 03 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.9.1.0.6.

* Tue Jun 02 1998 Erik Troan <ewt@redhat.com>
- added patch from rth to get right offsets for sections in relocateable
  objects on sparc32

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue May 05 1998 Cristian Gafton <gafton@redhat.com>
- version 2.9.1.0.4 is out; even more, it is public !

* Tue May 05 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.9.1.0.3.

* Mon Apr 20 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.9.0.3

* Tue Apr 14 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 2.9.0.2

* Sun Apr 05 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.8.1.0.29 (HJ warned me that this thing is a moving target...
  :-)
- "fixed" the damn make install command so that all tools get installed

* Thu Apr 02 1998 Cristian Gafton <gafton@redhat.com>
- upgraded again to 2.8.1.0.28 (at least on alpha now egcs will compile)
- added info packages handling

* Tue Mar 10 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 2.8.1.0.23

* Mon Mar 02 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.8.1.0.15 (required to compile the newer glibc)
- all patches are obsoleted now

* Wed Oct 22 1997 Erik Troan <ewt@redhat.com>
- added 2.8.1.0.1 patch from hj
- added patch for alpha palcode form rth
