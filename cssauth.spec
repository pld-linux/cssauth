Summary:	CSS authentication/decryption tools	
Name:		cssauth
Version:	0
Release:	1
License:	GPL
Group:		Utilities
Group(pl):	Narzêdzia
Source0:	%{name}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for authenticating and decrypting CSS-protected DVD. Makes
playing DVD using MPEG-2 software decoders (like VideoLAN client)
possible.

%prep
%setup -qn css-auth

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -s css-cat dvdinfo tstdvd $RPM_BUILD_ROOT%{_bindir}
install -s reset $RPM_BUILD_ROOT%{_bindir}/dvdreset

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/*
