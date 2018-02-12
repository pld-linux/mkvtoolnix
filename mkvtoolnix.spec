# TODO:
# - make -gui subpackages (Qt4 deps)
# - boost autodetection fails ($BOOSTLIBDIR empty), so all boost libs must be passed --with-boost-xxx=xxxx
#
# Conditional build
%bcond_with	verbose	# verbose build (V=1)
%bcond_without	qt	# disable GUI build (Qt4 deps)
#
Summary:	Matroska video utilities
Summary(pl.UTF-8):	Narzędzia do filmów w formacie Matroska
Name:		mkvtoolnix
Version:	20.0.0
Release:	1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://www.bunkus.org/videotools/mkvtoolnix/sources/%{name}-%{version}.tar.xz
# Source0-md5:	87a7ea4b6ace3cf954f86108a7d41a0f
Patch0:		%{name}-init_locales.patch
URL:		http://www.bunkus.org/videotools/mkvtoolnix/
%if %{with qt}
BuildRequires:	Qt5Concurrent-devel >= 5.3.0
BuildRequires:	Qt5Gui-devel >= 5.3.0
BuildRequires:	Qt5Multimedia-devel >= 5.3.0
BuildRequires:	cmark-devel
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= 5.3.0
BuildRequires:	qt5-linguist >= 5.3.0
%endif
BuildRequires:	autoconf
BuildRequires:	boost-devel >= 1.49.0
BuildRequires:	bzip2-devel
BuildRequires:	docbook-style-xsl
BuildRequires:	flac-devel
BuildRequires:	gettext-tools
BuildRequires:	libebml-devel >= 1.3.5
BuildRequires:	libmagic-devel
BuildRequires:	libmatroska-devel >= 1.4.8
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	lzo-devel
BuildRequires:	po4a
BuildRequires:	pugixml-devel
BuildRequires:	ruby-modules
BuildRequires:	ruby-rake
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matroska video utilities.

%description -l pl.UTF-8
Narzędzia do filmów w formacie Matroska.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure \
	%{?with_qt:LCONVERT=/usr/bin/lconvert-qt5} \
	--docdir=%{_datadir}/%{name} \
	--%{?with_qt:en}%{!?with_qt:dis}able-qt \
	--with-boost-filesystem=boost_filesystem \
	--with-boost-regex=boost_regex \
	--with-boost-system=boost_system \
	%{?with_qt:--with-moc=/usr/bin/moc-qt5} \
	%{?with_qt:--with-uic=/usr/bin/uic-qt5} \
	--with-docbook-xsl-root=/usr/share/sgml/docbook/xsl-stylesheets

LC_ALL="C.UTF-8" rake %{?_smp_mflags} %{?with_verbose:V=1}

%install
rm -rf $RPM_BUILD_ROOT

LC_ALL="C.UTF-8" rake install \
	INSTALL="install -cp" \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/sr_RS{,@latin}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README.md NEWS.md
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/mkvtoolnix
%dir %{_datadir}/mkvtoolnix/sounds
%{_datadir}/mkvtoolnix/sounds/finished-1.ogg
%{_datadir}/mkvtoolnix/sounds/finished-2.ogg
%{_datadir}/mkvtoolnix/sounds/finished-3.ogg
%{_datadir}/mime/packages/mkvtoolnix.xml
%{_desktopdir}/org.bunkus.mkvinfo.desktop
%{_desktopdir}/org.bunkus.mkvtoolnix-gui.desktop
%{_iconsdir}/hicolor/*/apps/mkvextract.png
%{_iconsdir}/hicolor/*/apps/mkvinfo.png
%{_iconsdir}/hicolor/*/apps/mkvmerge.png
%{_iconsdir}/hicolor/*/apps/mkvtoolnix-gui.png
%{_iconsdir}/hicolor/*/apps/mkvpropedit.png
%{_mandir}/man1/*
%lang(ca) %{_mandir}/ca/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(ko) %{_mandir}/ko/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(uk) %{_mandir}/uk/man1/*
%lang(zh_CN) %{_mandir}/zh_CN/man1/*
