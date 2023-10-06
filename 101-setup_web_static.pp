# Sets up web servers for deployment of web_static

class web_static {

  package { 'nginx':
    ensure => 'latest',
  }

  file { '/data/web_static/releases/test':
    ensure  => 'directory',
    recurse => true,
    owner   => 'ubuntu',
    group   => 'ubuntu',
  }

  file { '/data/web_static/shared':
    ensure  => 'directory',
    recurse => true,
    owner   => 'ubuntu',
    group   => 'ubuntu',
  }

  file { '/data/web_static/releases/test/index.html':
    ensure  => 'file',
    content => 'joelofelectronics',
    owner   => 'ubuntu',
    group   => 'ubuntu',
  }

  file { '/data/web_static/current':
    ensure  => 'link',
    target  => '/data/web_static/releases/test/',
    owner   => 'ubuntu',
    group   => 'ubuntu',
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => 'file',
    content => template('web_static/default.erb'),
    notify  => Service['nginx'],
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure  => 'link',
    target  => '/etc/nginx/sites-available/default',
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => File['/etc/nginx/sites-enabled/default'],
  }
}

class { 'web_static': }

