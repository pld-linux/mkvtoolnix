# TODO:
# - compile mkvinfo's GUI and mmg (--enable-gui)

Summary:	Matroska video utilities
Summary(pl):	Narzêdzia do filmów w formacie Matroska
Name:		mkvtoolnix
Version:	1.4.0
Release:	0.1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://www.bunkus.org/videotools/mkvtoolnix/sources/%{name}-%{version}.tar.bz2
# Source0-md5:	593c9f51ff99c90a017117bad2edd3e4
URL:		http://www.bunkus.org/videotools/mkvtoolnix/
BuildRequires:	bzip2-devel
BuildRequires:	expat-devel
BuildRequires:	flac-devel
BuildRequires:	libebml-devel >= 0.7.3
BuildRequires:	libmatroska-devel >= 0.7.5
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matroska video utilities.

%description -l pl
Narzêdzia do filmów w formacie Matroska.

%prep
%setup -q

%build
%configure \
	--disable-gui \
	--enable-bz2

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
