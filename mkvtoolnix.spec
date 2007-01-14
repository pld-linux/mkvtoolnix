# TODO:
# - make subpackage -gui (wxWidgets deps)
#
# Conditional build
%bcond_without	gui	# disable GUI build (wxWigets deps)
#
Summary:	Matroska video utilities
Summary(pl):	Narzêdzia do filmów w formacie Matroska
Name:		mkvtoolnix
Version:	2.0.0
Release:	1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://www.bunkus.org/videotools/mkvtoolnix/sources/%{name}-%{version}.tar.bz2
# Source0-md5:	d8a1d1f014f2ee5e69da04a46305f9dd
Patch0:		%{name}-help.patch
URL:		http://www.bunkus.org/videotools/mkvtoolnix/
BuildRequires:	bzip2-devel
BuildRequires:	expat-devel
BuildRequires:	flac-devel
BuildRequires:	libebml-devel >= 0.7.7
BuildRequires:	libmatroska-devel >= 0.8.0
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	lzo-devel
BuildRequires:	pcre-cxx-devel
BuildRequires:	sed >= 4.0
%{?with_gui:BuildRequires:	wxGTK2-devel >= 2.6.0}
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matroska video utilities.

%description -l pl
Narzêdzia do filmów w formacie Matroska.

%prep
%setup -q
%patch0 -p1

%build
%if %{with gui}
%{__sed} -i 's,wx-config,wx-gtk2-ansi-config,g' configure
%endif
%{__sed} -i 's,$INSTDIR,%{_datadir}/%{name},' src/mmg/mmg.cpp

%configure \
	--enable-gui=%{?with_gui:yes}%{?!with_gui:no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/doc/images

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# help files
install doc/*.h* $RPM_BUILD_ROOT%{_datadir}/%{name}/doc
install doc/images/* $RPM_BUILD_ROOT%{_datadir}/%{name}/doc/images

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
