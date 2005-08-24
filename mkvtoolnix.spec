# TODO:
# - make subpackage -gui (wxWidgets deps)
#
Summary:	Matroska video utilities
Summary(pl):	Narz�dzia do film�w w formacie Matroska
Name:		mkvtoolnix
Version:	1.5.5
Release:	0.1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://www.bunkus.org/videotools/mkvtoolnix/sources/%{name}-%{version}.tar.bz2
# Source0-md5:	f86b4b8e3ae07a3d8d2fd69a1f2dd3d5
URL:		http://www.bunkus.org/videotools/mkvtoolnix/
BuildRequires:	bzip2-devel
BuildRequires:	expat-devel
BuildRequires:	flac-devel
BuildRequires:	libebml-devel >= 0.7.3
BuildRequires:	libmatroska-devel >= 0.7.5
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	sed >= 4.0
BuildRequires:	wxGTK2-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matroska video utilities.

%description -l pl
Narz�dzia do film�w w formacie Matroska.

%prep
%setup -q

%build
%{__sed} -i 's,wx-config,wx-gtk2-ansi-config,g' configure
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO doc/*.html doc/images/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
