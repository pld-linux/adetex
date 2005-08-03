Summary:	LaTeX macros for converting Jade TeX output into DVI/PS/PDF
Summary(pl):	Makra LaTeXa do konwersji wyj¶cia Jade TeXa do DVI/PS/PDF
Name:		jadetex
Version:	2.15
Release:	1
License:	Copyright (C) 1995,1996,1997,1998 Sebastian Rahtz <s.rahtz@elsevier.co.uk>
Group:		Applications/Publishing/SGML
Source0:	ftp://ftp.duke.edu/tex-archive/macros/%{name}.tar.bz2
# Source0-md5:	2e2d266e03062b9157d177b4f73a3a2f
Patch0:		%{name}-i18n.patch
Requires:	sgml-common
Requires:	tetex >= 0.9
Requires:	tetex-latex >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jadetex contains the additional LaTeX macros necessary for taking Jade
TeX output files and processing them as LaTeX files.

%description -l pl
Jadetex zawiera dodatkowe makra LaTeXa, niezbêdne do obróbki plików
wyj¶ciowych Jade TeX tak samo jak plików LaTeXa.

%prep
%setup -q -n jadetex
%patch0 -p1

%build
#make -f Makefile.jadetex install DESTDIR=$RPM_BUILD_ROOT

# temporary fix for some latex errors
# they are not important and can be ignored
tex jadetex.ins
echo | tex -ini "&hugelatex" -progname=jadetex jadetex.ini || :
echo | pdftex -ini "&pdflatex" -progname=pdfjadetex pdfjadetex.ini || :

#tex jadetex.ins
#tex -ini "&hugelatex" -progname=jadetex jadetex.ini
#pdftex -ini "&pdflatex" -progname=pdfjadetex pdfjadetex.ini

%install
rm -rf $RPM_BUILD_ROOT

##export TT=`kpsewhich -expand-var '$TEXMFMAIN'`
# make install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/texmf/web2c
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/jadetex
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1

mv pdfjadetex.fmt jadetex.fmt $RPM_BUILD_ROOT%{_datadir}/texmf/web2c
mv jadetex.1 pdfjadetex.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp dsssl.def jadetex.ltx $RPM_BUILD_ROOT%{_datadir}/texmf/tex/jadetex

#ln -s virtex $RPM_BUILD_ROOT%{_bindir}/jadetex
#ln -s pdfvirtex $RPM_BUILD_ROOT%{_bindir}/pdfjadetex
ln -s tex $RPM_BUILD_ROOT%{_bindir}/jadetex
ln -s pdftex $RPM_BUILD_ROOT%{_bindir}/pdfjadetex

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x %{_bindir}/texhash ] || /usr/bin/env - %{_bindir}/texhash 1>&2

%postun
[ ! -x %{_bindir}/texhash ] || /usr/bin/env - %{_bindir}/texhash 1>&2

%files
%defattr(644,root,root,755)
#%doc ChangeLog
%{_datadir}/texmf/web2c/*
%{_datadir}/texmf/tex/jadetex
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
