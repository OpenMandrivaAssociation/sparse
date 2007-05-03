Name:		sparse
Version:	0.3
Release:	%mkrel 1
Summary:	A semantic parser of source files
License:	GPL
Group:		Development/C
URL:		http://www.kernel.org/pub/software/devel/sparse/
Source0:	http://kernel.org/pub/software/devel/sparse/dist/%name-%version.tar.bz2
Buildroot:	%_tmppath/%name-%version-root

%description
Sparse, the semantic parser, provides a compiler frontend capable of parsing
most of ANSI C as well as many GCC extensions, and a collection of sample
compiler backends, including a static analyzer also called "sparse".

Sparse provides a set of annotations designed to convey semantic information
about types, such as what address space pointers point to, or what locks a
function acquires or releases.

%prep
%setup -q

%build
%make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{,/usr}/bin

%makeinstall_std PREFIX=%_prefix LIBDIR=%_libdir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc FAQ LICENSE README
%_bindir/*
%_includedir/*
%_libdir/libsparse.a
%_libdir/pkgconfig/sparse.pc



