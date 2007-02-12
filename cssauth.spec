Summary:	CSS authentication/decryption tools
Summary(pl.UTF-8):	Narzędzia do autentykacji i dekodowania CSS
Name:		cssauth
Version:	0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.uslawbooks.com/computerscience/%{name}.tar.gz
# Source0-md5:	b815dfc23185d44ba327319030cd6237
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for authenticating and decrypting CSS-protected DVD. Makes
playing DVD using MPEG-2 software decoders (like VideoLAN client)
possible.

%description -l pl.UTF-8
Narzędzia do autentykacji i dekodowania płyt DVD zakodowanych CSS.
Sprawiają, że odtwarzanie DVD przy pomocy programowych dekoderów
MPEG-2 (jak klient VideoLAN) jest możliwe.

%prep
%setup -qn css-auth

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install css-cat dvdinfo tstdvd $RPM_BUILD_ROOT%{_bindir}
install reset $RPM_BUILD_ROOT%{_bindir}/dvdreset

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
