%global tl_name ftc-notebook
%global tl_revision 50043

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Typeset FIRST Tech Challenge (FTC) notebooks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ftc-notebook
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ftc-notebook.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ftc-notebook.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package will greatly simplify filling entries for your FIRST
Tech Challenge (FTC) engineering or outreach notebook. We developed this
package to support most frequently used constructs encountered in an FTC
notebook: meetings, tasks, decisions with pros and cons, tables, figures
with explanations, team stories and bios, and more. We developed this
package during the 2018-2019 season and are using it for our engineering
notebook. Team Robocracy is sharing this style in the spirit of
coopertition.

