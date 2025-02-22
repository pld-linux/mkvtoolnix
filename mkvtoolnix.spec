#
# Conditional build
%bcond_with	verbose	# verbose build (V=1)
%bcond_without	qt	# disable GUI build (Qt6 deps)
#
Summary:	Matroska video utilities
Summary(pl.UTF-8):	Narzędzia do filmów w formacie Matroska
Name:		mkvtoolnix
Version:	88.0
Release:	2
License:	GPL v2
Group:		Applications/Multimedia
Source0:	https://www.bunkus.org/videotools/mkvtoolnix/sources/%{name}-%{version}.tar.xz
# Source0-md5:	b7c06326998d18553681c9565a9f2931
Patch0:		%{name}-init_locales.patch
URL:		https://www.bunkus.org/videotools/mkvtoolnix/
%if %{with qt}
BuildRequires:	Qt6Concurrent-devel >= 6.2.0
BuildRequires:	Qt6DBus-devel >= 6.2.0
BuildRequires:	Qt6Gui-devel >= 6.2.0
BuildRequires:	Qt6Multimedia-devel >= 6.2.0
BuildRequires:	Qt6Svg-devel >= 6.2.0
BuildRequires:	Qt6Widgets-devel >= 6.2.0
BuildRequires:	cmark-devel
BuildRequires:	qt6-build >= 6.2.0
BuildRequires:	qt6-linguist >= 6.2.0
%endif
BuildRequires:	autoconf >= 2.69
BuildRequires:	boost-devel >= 1.66.0
BuildRequires:	bzip2-devel
BuildRequires:	docbook-style-xsl
BuildRequires:	flac-devel
BuildRequires:	gettext-tools
BuildRequires:	gmp-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libebml-devel >= 1.4.4
BuildRequires:	libfmt-devel >= 8.0.0
BuildRequires:	libmagic-devel
BuildRequires:	libmatroska-devel >= 1.7.1
BuildRequires:	libogg-devel
BuildRequires:	libstdc++-devel >= 6:10
BuildRequires:	libvorbis-devel
BuildRequires:	libxslt-progs
BuildRequires:	lzo-devel
BuildRequires:	nlohmann-json-devel
BuildRequires:	pandoc
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	po4a
BuildRequires:	pugixml-devel
BuildRequires:	ruby-modules
BuildRequires:	ruby-rake
BuildRequires:	utf8cpp-devel
BuildRequires:	zlib-devel
Requires:	libebml >= 1.4.4
Requires:	libfmt >= 8.0.0
Requires:	libmatroska >= 1.7.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matroska video utilities.

%description -l pl.UTF-8
Narzędzia do filmów w formacie Matroska.

%package gui
Summary:	Qt GUI for mkvmerge including a chapter and a header editor
Summary(pl.UTF-8):	Graficzny interfejs Qt do mkvmerge, zawierający edytor rozdziałów i nagłówków
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description gui
Qt GUI for mkvmerge including a chapter and a header editor.

%description gui -l pl.UTF-8
Graficzny interfejs Qt do mkvmerge, zawierający edytor rozdziałów i
nagłówków.

%prep
%setup -q
%patch -P 0 -p1

%build
%{__autoconf}
# TODO: drop -DBOOST_CSTDFLOAT_NO_LIBQUADMATH_SUPPORT=1 after boost update to gcc 14 ready
CPPFLAGS="%{rpmcppflags} -DBOOST_CSTDFLOAT_NO_LIBQUADMATH_SUPPORT=1 -I/usr/include/utf8cpp"
%configure \
%if %{with qt}
	LCONVERT=/usr/bin/lconvert-qt6 \
	MOC=/usr/bin/moc-qt6 \
	RCC=/usr/bin/rcc-qt6 \
	UIC=/usr/bin/uic-qt6 \
	--with-qmake6=/usr/bin/qmake-qt6 \
%else
	--disable-gui \
%endif
	--docdir=%{_datadir}/%{name} \
	--with-docbook-xsl-root=/usr/share/sgml/docbook/xsl-stylesheets

LC_ALL="C.UTF-8" \
rake %{?_smp_mflags} %{?with_verbose:V=1}

%install
rm -rf $RPM_BUILD_ROOT

LC_ALL="C.UTF-8" \
rake install \
	INSTALL="install -cp" \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{sr_RS,sr}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{sr_RS@latin,sr@latin}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README.md NEWS.md
%attr(755,root,root) %{_bindir}/mkvmerge
%attr(755,root,root) %{_bindir}/mkvextract
%attr(755,root,root) %{_bindir}/mkvpropedit
%{_mandir}/man1/mkvmerge.1*
%{_mandir}/man1/mkvextract.1*
%{_mandir}/man1/mkvpropedit.1*
%lang(be) %{_mandir}/be/man1/mkvmerge.1*
%lang(be) %{_mandir}/be/man1/mkvextract.1*
%lang(be) %{_mandir}/be/man1/mkvpropedit.1*
%lang(bg) %{_mandir}/bg/man1/mkvmerge.1*
%lang(bg) %{_mandir}/bg/man1/mkvextract.1*
%lang(bg) %{_mandir}/bg/man1/mkvpropedit.1*
%lang(ca) %{_mandir}/ca/man1/mkvmerge.1*
%lang(ca) %{_mandir}/ca/man1/mkvextract.1*
%lang(ca) %{_mandir}/ca/man1/mkvpropedit.1*
%lang(de) %{_mandir}/de/man1/mkvmerge.1*
%lang(de) %{_mandir}/de/man1/mkvextract.1*
%lang(de) %{_mandir}/de/man1/mkvpropedit.1*
%lang(es) %{_mandir}/es/man1/mkvmerge.1*
%lang(es) %{_mandir}/es/man1/mkvextract.1*
%lang(es) %{_mandir}/es/man1/mkvpropedit.1*
%lang(fr) %{_mandir}/fr/man1/mkvmerge.1*
%lang(fr) %{_mandir}/fr/man1/mkvextract.1*
%lang(fr) %{_mandir}/fr/man1/mkvpropedit.1*
%lang(it) %{_mandir}/it/man1/mkvmerge.1*
%lang(it) %{_mandir}/it/man1/mkvextract.1*
%lang(it) %{_mandir}/it/man1/mkvpropedit.1*
%lang(ja) %{_mandir}/ja/man1/mkvmerge.1*
%lang(ja) %{_mandir}/ja/man1/mkvextract.1*
%lang(ja) %{_mandir}/ja/man1/mkvpropedit.1*
%lang(ko) %{_mandir}/ko/man1/mkvmerge.1*
%lang(ko) %{_mandir}/ko/man1/mkvextract.1*
%lang(ko) %{_mandir}/ko/man1/mkvpropedit.1*
%lang(nb) %{_mandir}/nb/man1/mkvextract.1*
%lang(nb) %{_mandir}/nb/man1/mkvmerge.1*
%lang(nb) %{_mandir}/nb/man1/mkvpropedit.1*
%lang(nl) %{_mandir}/nl/man1/mkvmerge.1*
%lang(nl) %{_mandir}/nl/man1/mkvextract.1*
%lang(nl) %{_mandir}/nl/man1/mkvpropedit.1*
%lang(pl) %{_mandir}/pl/man1/mkvmerge.1*
%lang(pl) %{_mandir}/pl/man1/mkvextract.1*
%lang(pl) %{_mandir}/pl/man1/mkvpropedit.1*
%lang(ru) %{_mandir}/ru/man1/mkvmerge.1*
%lang(ru) %{_mandir}/ru/man1/mkvextract.1*
%lang(ru) %{_mandir}/ru/man1/mkvpropedit.1*
%lang(uk) %{_mandir}/uk/man1/mkvmerge.1*
%lang(uk) %{_mandir}/uk/man1/mkvextract.1*
%lang(uk) %{_mandir}/uk/man1/mkvpropedit.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/mkvmerge.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/mkvextract.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/mkvpropedit.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/mkvmerge.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/mkvextract.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/mkvpropedit.1*

%if %{without qt}
%attr(755,root,root) %{_bindir}/mkvinfo
%{_mandir}/man1/mkvinfo.1*
%lang(bg) %{_mandir}/bg/man1/mkvinfo.1*
%lang(ca) %{_mandir}/ca/man1/mkvinfo.1*
%lang(de) %{_mandir}/de/man1/mkvinfo.1*
%lang(es) %{_mandir}/es/man1/mkvinfo.1*
%lang(fr) %{_mandir}/fr/man1/mkvinfo.1*
%lang(it) %{_mandir}/it/man1/mkvinfo.1*
%lang(ja) %{_mandir}/ja/man1/mkvinfo.1*
%lang(ko) %{_mandir}/ko/man1/mkvinfo.1*
%lang(nb) %{_mandir}/nb/man1/mkvinfo.1*
%lang(nl) %{_mandir}/nl/man1/mkvinfo.1*
%lang(pl) %{_mandir}/pl/man1/mkvinfo.1*
%lang(ru) %{_mandir}/ru/man1/mkvinfo.1*
%lang(uk) %{_mandir}/uk/man1/mkvinfo.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/mkvinfo.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/mkvinfo.1*
%endif

%if %{with qt}
%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mkvinfo
%attr(755,root,root) %{_bindir}/mkvtoolnix-gui
%{_datadir}/mkvtoolnix
%{_datadir}/metainfo/org.bunkus.mkvtoolnix-gui.appdata.xml
%{_datadir}/mime/packages/org.bunkus.mkvtoolnix-gui.xml
%{_desktopdir}/org.bunkus.mkvtoolnix-gui.desktop
%{_iconsdir}/hicolor/*/apps/mkvextract.png
%{_iconsdir}/hicolor/*/apps/mkvinfo.png
%{_iconsdir}/hicolor/*/apps/mkvmerge.png
%{_iconsdir}/hicolor/*/apps/mkvtoolnix-gui.png
%{_iconsdir}/hicolor/*/apps/mkvpropedit.png
%{_mandir}/man1/mkvinfo.1*
%{_mandir}/man1/mkvtoolnix-gui.1*
%lang(be) %{_mandir}/be/man1/mkvinfo.1*
%lang(be) %{_mandir}/be/man1/mkvtoolnix-gui.1*
%lang(bg) %{_mandir}/bg/man1/mkvinfo.1*
%lang(bg) %{_mandir}/bg/man1/mkvtoolnix-gui.1*
%lang(ca) %{_mandir}/ca/man1/mkvinfo.1*
%lang(ca) %{_mandir}/ca/man1/mkvtoolnix-gui.1*
%lang(de) %{_mandir}/de/man1/mkvinfo.1*
%lang(de) %{_mandir}/de/man1/mkvtoolnix-gui.1*
%lang(es) %{_mandir}/es/man1/mkvinfo.1*
%lang(es) %{_mandir}/es/man1/mkvtoolnix-gui.1*
%lang(fr) %{_mandir}/fr/man1/mkvinfo.1*
%lang(fr) %{_mandir}/fr/man1/mkvtoolnix-gui.1*
%lang(it) %{_mandir}/it/man1/mkvinfo.1*
%lang(it) %{_mandir}/it/man1/mkvtoolnix-gui.1*
%lang(ja) %{_mandir}/ja/man1/mkvinfo.1*
%lang(ja) %{_mandir}/ja/man1/mkvtoolnix-gui.1*
%lang(ko) %{_mandir}/ko/man1/mkvinfo.1*
%lang(ko) %{_mandir}/ko/man1/mkvtoolnix-gui.1*
%lang(nb) %{_mandir}/nb/man1/mkvinfo.1*
%lang(nb) %{_mandir}/nb/man1/mkvtoolnix-gui.1*
%lang(nl) %{_mandir}/nl/man1/mkvinfo.1*
%lang(nl) %{_mandir}/nl/man1/mkvtoolnix-gui.1*
%lang(pl) %{_mandir}/pl/man1/mkvinfo.1*
%lang(pl) %{_mandir}/pl/man1/mkvtoolnix-gui.1*
%lang(ru) %{_mandir}/ru/man1/mkvinfo.1*
%lang(ru) %{_mandir}/ru/man1/mkvtoolnix-gui.1*
%lang(uk) %{_mandir}/uk/man1/mkvinfo.1*
%lang(uk) %{_mandir}/uk/man1/mkvtoolnix-gui.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/mkvinfo.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/mkvtoolnix-gui.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/mkvinfo.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/mkvtoolnix-gui.1*
%endif
