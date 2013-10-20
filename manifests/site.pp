class { 'python':
  version    => 'system',
  dev        => true,
  virtualenv => true,
  gunicorn   => false,
  pip        => true,
}

python::virtualenv { '/srv/eight_queens':
  ensure       => present,
  version      => 'system',
  requirements => '/srv/eight_queens/requirements.txt',
  owner        => 'vagrant',
  group        => 'vagrant',
}
