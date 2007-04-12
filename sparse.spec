Name:		sparse
Version:	0.1
Release:	%mkrel 1
Summary:	A semantic parser of source files
License:	GPL
Group:		Development/C
URL:		http://kernel.org/pub/linux/kernel/people/josh/sparse/
Source0:	http://kernel.org/pub/linux/kernel/people/josh/sparse/dist/%name-%version.tar.bz2
Buildroot:	%_tmppath/%name-%version-root

%description
Sparse is a semantic parser of source files.

%prep
%setup -q

%build
%make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{,/usr}/bin

%makeinstall PREFIX=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc FAQ LICENSE README
/bin/*

