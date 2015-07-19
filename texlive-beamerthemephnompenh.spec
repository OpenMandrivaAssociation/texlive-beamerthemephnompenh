# revision 31392
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-beamerthemephnompenh
Version:	20131013
Release:	9
Summary:	TeXLive beamerthemephnompenh package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemephnompenh.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemephnompenh.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive beamerthemephnompenh package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/beamerthemephnompenh/beamerthemePhnomPenh.sty
%doc %{_texmfdistdir}/doc/latex/beamerthemephnompenh/README
%doc %{_texmfdistdir}/doc/latex/beamerthemephnompenh/beamerthemePhnomPenh.pdf
%doc %{_texmfdistdir}/doc/latex/beamerthemephnompenh/beamerthemePhnomPenh.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
