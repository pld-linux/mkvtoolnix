# TODO:
# - make -gui subpackages (wxWidgets and Qt4 deps)
#
# Conditional build
%bcond_with	verbose	# verbose build (V=1)
%bcond_without	qt	# disable GUI build (Qt4 deps)
%bcond_without	wx	# disable GUI build (wxWigets deps)
#
Summary:	Matroska video utilities
Summary(pl.UTF-8):	Narzędzia do filmów w formacie Matroska
Name:		mkvtoolnix
Version:	2.9.9
Release:	1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://www.bunkus.org/videotools/mkvtoolnix/sources/%{name}-%{version}.tar.bz2
# Source0-md5:	4bad0301e94cc24ec8f847c84502ab4d
Patch0:		%{name}-configure.patch
Patch1:		%{name}-init_locales.patch
URL:		http://www.bunkus.org/videotools/mkvtoolnix/
%{?with_qt:BuildRequires:	QtGui-devel}
BuildRequires:	boost-devel >= 1.32
BuildRequires:	bzip2-devel
BuildRequires:	expat-devel
BuildRequires:	flac-devel
BuildRequires:	gettext-devel
BuildRequires:	libebml-devel >= 0.7.7
BuildRequires:	libmagic-devel
BuildRequires:	libmatroska-devel >= 0.8.1
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	lzo-devel
BuildRequires:	pcre-cxx-devel
%if %{with qt}
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= 4.3.3-3
%endif
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
%patch1 -p1

%build
%configure \
	--enable-gui \
	--%{?with_wx:en}%{!?with_wx:dis}able-wxwidgets \
	--%{?with_qt:en}%{!?with_qt:dis}able-qt \
	%{?with_qt:--with-moc=/usr/bin/moc-qt4} \
	%{?with_qt:--with-uic=/usr/bin/uic-qt4} \
	%{?with_wx:--with-wx-config=/usr/bin/wx-gtk2-unicode-config}

%{__make} \
	%{?with_verbose:V=1}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/doc/images

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# help files
install doc/*.h* $RPM_BUILD_ROOT%{_datadir}/%{name}/doc
install doc/images/* $RPM_BUILD_ROOT%{_datadir}/%{name}/doc/images

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
