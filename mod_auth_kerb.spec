
Summary: Kerberos authentication module for HTTP
Name: mod_auth_kerb
Version: 5.4
Release: 6%{?dist}
License: BSD and MIT
Group: System Environment/Daemons
URL: http://modauthkerb.sourceforge.net/
Source0: http://downloads.sourceforge.net/modauthkerb/%{name}-%{version}.tar.gz
Source1: auth_kerb.conf
Patch1: mod_auth_kerb-5.4-rcopshack.patch
Patch2: mod_auth_kerb-5.4-fixes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: httpd-devel, krb5-devel
Requires: httpd-mmn = %(cat %{_includedir}/httpd/.mmn || echo missing)

%description
mod_auth_kerb is module for the Apache HTTP Server designed to
provide Kerberos authentication over HTTP.  The module supports the
Negotiate authentication method, which performs full Kerberos
authentication based on ticket exchanges.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1 -b .rcopshack
%patch2 -p1 -b .fixes

%build
%configure --without-krb4 --with-krb5=/usr/kerberos \
        --with-apache=%{_prefix}
make %{?_smp_mflags} 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/httpd/modules \
         $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
install -m 755 src/.libs/mod_auth_kerb.so \
        $RPM_BUILD_ROOT%{_libdir}/httpd/modules/mod_auth_kerb.so
install -p -m 644 %{SOURCE1} \
        $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/auth_kerb.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README LICENSE
%config(noreplace) %{_sysconfdir}/httpd/conf.d/auth_kerb.conf
%{_libdir}/httpd/modules/*.so

%changelog
* Mon Mar 29 2010 Joe Orton <jorton@redhat.com> - 5.4-6
- package LICENSE file

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 5.4-5.1
- Rebuilt for RHEL 6

* Fri Aug 07 2009 Parag <paragn@fedoraproject.org> 5.4-5
- Spec cleanup as suggested in review bug #226150

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 11 2008 Joe Orton <jorton@redhat.com> 5.4-2
- update to 5.4

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.3-7
- Autorebuild for GCC 4.3

* Tue Sep 25 2007 Joe Orton <jorton@redhat.com> 5.3-6
- fix configure invocation (#301181)

* Sun Sep  2 2007 Joe Orton <jorton@redhat.com> 5.3-5
- rebuild for fixed 32-bit APR

* Thu Aug 30 2007 Joe Orton <jorton@redhat.com> 5.3-4
- clarify License tag

* Wed Nov 29 2006 Joe Orton <jorton@redhat.com> 5.3-3
- fix r->user caching (Enrico Scholz, #214207)
- update to 5.3 (CVE-2006-5989, #215443)

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 5.1-3
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 Joe Orton <jorton@redhat.com> 5.1-2
- update to 5.1

* Thu Aug  3 2006 Joe Orton <jorton@redhat.com> 5.0-10
- fix segfault at startup (#201145)

* Thu Jul 20 2006 Joe Orton <jorton@redhat.com> 5.0-9
- add Russ Allbery's fix for disabling replay cache with krb15

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 5.0-8.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 5.0-8.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 5.0-8.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Dec  5 2005 Joe Orton <jorton@redhat.com> 5.0-8
- rebuild for httpd 2.2

* Wed Sep 21 2005 Joe Orton <jorton@redhat.com> 5.0-7
- fix build without /usr/sbin in $PATH (Roozbeh Pournader, #168212)

* Tue May 10 2005 Joe Orton <jorton@redhat.com> 5.0-6
- update to 5.0rc6
- don't force CC=gcc4

* Fri Mar  4 2005 Joe Orton <jorton@redhat.com> 5.0-3
- fix build with GCC 4
- only add "auth_kerb_module" symbol to dynamic symbol table

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Apr  8 2004 Joe Orton <jorton@redhat.com> 5.0-0.rc4.5
- remove static globals
- add SSLRequireSSL

* Mon Mar 29 2004 Joe Orton <jorton@redhat.com> 5.0-0.rc4.3
- support mutual authentication (Nalin Dahyabhai)
- once authentication returns COMPLETE, cache name for the duration
  of the connection

* Thu Mar 25 2004 Joe Orton <jorton@redhat.com> 5.0-0.rc4.2
- add example config file

* Wed Mar 24 2004 Joe Orton <jorton@redhat.com> 5.0-0.rc4.1
- update to mod_auth_kerb.c from HEAD to get workaround for
  "Request is a replay" errors

* Tue Mar 23 2004 Joe Orton <jorton@redhat.com> 
- Initial build.
