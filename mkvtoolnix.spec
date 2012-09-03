# TODO:
# - make -gui subpackages (wxWidgets and Qt4 deps)
# - boost autodetection fails ($BOOSTLIBDIR empty), so all boost libs must be passed --with-boost-xxx=xxxx
#
# Conditional build
%bcond_with	verbose	# verbose build (V=1)
%bcond_without	qt	# disable GUI build (Qt4 deps)
%bcond_without	wx	# disable GUI build (wxWigets deps)
#
Summary:	Matroska video utilities
Summary(pl.UTF-8):	Narzędzia do filmów w formacie Matroska
Name:		mkvtoolnix
Version:	5.8.0
Release:	1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://www.bunkus.org/videotools/mkvtoolnix/sources/%{name}-%{version}.tar.bz2
# Source0-md5:	8caa3d37d2442a525bad35dbb1babc56
Patch0:		%{name}-init_locales.patch
URL:		http://www.bunkus.org/videotools/mkvtoolnix/
%{?with_qt:BuildRequires:	QtGui-devel}
BuildRequires:	boost-devel >= 1.36
BuildRequires:	bzip2-devel
BuildRequires:	expat-devel
BuildRequires:	flac-devel
BuildRequires:	gettext-devel
BuildRequires:	libebml-devel >= 1.2.0
BuildRequires:	libmagic-devel
BuildRequires:	libmatroska-devel >= 1.1.0
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	lzo-devel
BuildRequires:	pcre-cxx-devel
%if %{with qt}
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= 4.3.3-3
%endif
# required by rake
BuildRequires:	ruby-modules
%{?with_wx:BuildRequires:	wxGTK2-unicode-devel >= 2.6.0}
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
%configure \
	--docdir=%{_datadir}/%{name} \
	--enable-gui \
	--%{?with_wx:en}%{!?with_wx:dis}able-wxwidgets \
	--%{?with_qt:en}%{!?with_qt:dis}able-qt \
	--with-boost-filesystem=boost_filesystem \
	--with-boost-regex=boost_regex \
	--with-boost-system=boost_system \
	%{?with_qt:--with-moc=/usr/bin/moc-qt4} \
	%{?with_qt:--with-uic=/usr/bin/uic-qt4} \
	%{?with_wx:--with-wx-config=/usr/bin/wx-gtk2-unicode-config} \
	--without-curl

rake %{?with_verbose:V=1}

%install
rm -rf $RPM_BUILD_ROOT

rake install \
	INSTALL="install -cp" \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/guide
%{_datadir}/%{name}/guide/en
%lang(es) %{_datadir}/%{name}/guide/es
%lang(eu) %{_datadir}/%{name}/guide/eu
%lang(zh_CN) %{_datadir}/%{name}/guide/zh_CN
%{_datadir}/mime/packages/mkvtoolnix.xml
%{_desktopdir}/mkvinfo.desktop
%{_desktopdir}/mkvmergeGUI.desktop
%{_iconsdir}/hicolor/*/apps/mkvextract.png
%{_iconsdir}/hicolor/*/apps/mkvinfo.png
%{_iconsdir}/hicolor/*/apps/mkvmerge.png
%{_iconsdir}/hicolor/*/apps/mkvmergeGUI.png
%{_iconsdir}/hicolor/*/apps/mkvpropedit.png
%{_mandir}/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(uk) %{_mandir}/uk/man1/*
%lang(zh_CN) %{_mandir}/zh_CN/man1/*
