%define short_name imakeidx
%define texhash [ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	A package for producing multiple indexes
Name:		tetex-latex-%{short_name}
Version:	1.3e
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	https://mirrors.ctan.org/install/macros/latex/contrib/%{short_name}.tds.zip
# Source0-md5:	db630e135ffeefbb3004fb5f530fec3b
BuildRequires:	unzip
Requires(post,postun):	/usr/bin/texhash
Requires:	tetex-latex
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package enables the user to produce and typeset one or more
indexes simultaneously with a document. The package is known to work
in LaTeX documents processed with pdfLaTeX, XeLaTeX and LuaLaTeX. If
makeindex is used for processing the index entries, no particular
setting up is needed when TeX Live is used. Using xindy or other
programs it is necessary to enable shell escape; shell escape is also
needed if splitindex is used.

%prep
%setup -q -c -n %{short_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/%{short_name}

cp -p tex/latex/imakeidx/*.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
cp -p doc/latex/imakeidx/*.pdf $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc %{_datadir}/texmf/doc/latex/%{short_name}
%{_datadir}/texmf/tex/latex/%{short_name}
