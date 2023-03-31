Name:		texlive-ftc-notebook
Version:	50043
Release:	2
Summary:	Typeset FIRST Tech Challenge (FTC) notebooks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ftc-notebook
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ftc-notebook.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ftc-notebook.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package will greatly simplify filling entries for
your FIRST Tech Challenge (FTC) engineering or outreach
notebook. We developed this package to support most frequently
used constructs encountered in an FTC notebook: meetings,
tasks, decisions with pros and cons, tables, figures with
explanations, team stories and bios, and more. We developed
this package during the 2018-2019 season and are using it for
our engineering notebook. Team Robocracy is sharing this style
in the spirit of coopertition.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ftc-notebook
%doc %{_texmfdistdir}/doc/latex/ftc-notebook

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
