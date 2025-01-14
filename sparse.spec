Name:		sparse
Version:	0.4.4
Release:	1
Summary:	A semantic parser of source files
License:	Open Software License v1.1
Group:		Development/C
URL:		https://www.kernel.org/pub/software/devel/sparse/
Source0:	http://kernel.org/pub/software/devel/sparse/dist/%name-%version.tar.gz

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
mkdir -p $RPM_BUILD_ROOT{,/usr}/bin

%makeinstall_std PREFIX=%_prefix LIBDIR=%_libdir

%files
%doc FAQ LICENSE README
%_bindir/*
%_includedir/*
%_libdir/libsparse.a
%_libdir/pkgconfig/sparse.pc
%_mandir/man1/*


