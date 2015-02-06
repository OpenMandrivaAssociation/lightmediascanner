%define		major	0
%define		libname %mklibname %name %{major}
%define		develname %mklibname %name -d

Summary: 	Lightweight media scanner
Name: 		lightmediascanner
Version: 	0.4.1.0
Release: 	2
Group: 		System/Libraries
License: 	LGPL
URL: 		http://lms.garage.maemo.org/
Source0: 	%{name}-%{version}.tar.xz


%description
Lightweight media scanner meant to be used in not-so-powerful
devices, like embedded systems or old machines. Provides an optimized
way to recursively scan directories, handling the parser in a child
process, avoiding breaks of the main process when parsers break.
One can opt to use the single process version, but be aware that
if something bad happens during parsing, your application will suffer. 

%package -n %{libname}
Summary:    %{name} library
Group:      System/Libraries

%description -n %{libname}
This package contains the dynamic libraries from %{name}.

%package -n %{develname}
Summary: 	Headers for developing programs that will use %{name}
Group:      Development/C
Requires:   %{libname} = %{version}
Provides:   %{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*  
%{_libdir}/%{name}/plugins/*.so 

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/%{name}.pc




%changelog
* Wed Jan 11 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.4.1.0-1
+ Revision: 760024
- remove all .la file
- imported package lightmediascanner


* Fri Dec 17 2010 mdawkins <mattydaw@gmail.com> 0.4.1.0-1-unity2011
- import for Unity
- new version 0.4.1.0
- mdv'fied lib

* Fri Aug 21 2009 Texstar <texstar@gmail.com> 0.3.0-1pclos2009
- create
