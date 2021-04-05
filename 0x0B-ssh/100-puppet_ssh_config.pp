B# Puppet script to edit config file.

file_line { 'indentity_file':
  ensure => present,
  line   => 'IdentityFile ~/.ssh/holberton',
  path   => '/etc/ssh/ssh_config',
}

file_line { 'pwd_aut':
  ensure => present,
  line   => 'PasswordAuthentication no',
  path   => '/etc/ssh/ssh_config',
}