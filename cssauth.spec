Summary:	CSS authentication/decryption tools
Summary(pl):	Narzêdzia do autentykacji i dekodowania CSS
Name:		cssauth
Version:	0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.uslawbooks.com/computerscience/%{name}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for authenticating and decrypting CSS-protected DVD. Makes
playing DVD using MPEG-2 software decoders (like VideoLAN client)
possible.

%description -l pl
Narzêdzia do autentykacji i dekodowania p³yt DVD zakodowanych CSS.
Sprawiaj±, ¿e odtwarzanie DVD przy pomocy programowych dekoderów
MPEG-2 (jak klient VideoLAN) jest mo¿liwe.

%prep
%setup -qn css-auth

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install css-cat dvdinfo tstdvd $RPM_BUILD_ROOT%{_bindir}
install reset $RPM_BUILD_ROOT%{_bindir}/dvdreset

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/*
