# Puppet script to edit config file.

file_line { 'Identity file':
  ensure => present,
  line   => 'IdentityFile ~/.ssh/holberton',
  path   => '/.ssh/config',
}

file_line { 'No password':
  ensure => present,
  line   => 'PasswordAuthentication no',
  path   => '/.ssh/config',
}