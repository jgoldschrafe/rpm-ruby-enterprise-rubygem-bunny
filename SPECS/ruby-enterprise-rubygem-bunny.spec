%define _prefix /opt/ruby-enterprise
%define _gem %{_prefix}/bin/gem
%define _ruby %{_prefix}/bin/ruby

# Generated from bunny-0.6.0.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{_ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{_ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname bunny
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A synchronous Ruby AMQP client that enables interaction with AMQP-compliant brokers/servers
Name: ruby-enterprise-rubygem-%{gemname}
Version: 0.6.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/celldee/bunny/tree/master
Source0: http://gemcutter.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby-enterprise-rubygems
BuildRequires: ruby-enterprise-rubygems
BuildArch: noarch
Provides: ruby-enterprise-rubygem(%{gemname}) = %{version}

%description
Another synchronous Ruby AMQP client


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README.rdoc
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Oct  3 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 0.6.0-1.hhg
- Rebuild for Ruby Enterprise Edition

* Sun Dec 19 2010 Sergio Rubio <rubiojr@frameos.org> - 0.6.0-1
- Initial package
