class { 'python':
  version    => 'system',
  dev        => true,
  virtualenv => true,
  gunicorn   => false,
  pip        => true,
}
