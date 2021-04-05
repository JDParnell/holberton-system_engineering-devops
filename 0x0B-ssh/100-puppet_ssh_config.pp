# puppet code for the task

file_line { 'PA':
  ensure => 'present',
  path   => '/.ssh/config',
  line   => 'PasswordAuthentication no',
}

file_line { 'IF':
  ensure => 'present',
  path   => '/.ssh/config',
  line   => 'IdentityFile ~/.ssh/holberton',
}