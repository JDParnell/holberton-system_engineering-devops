# This program kills the process killmenow
exec { 'pkill' :
  command => '/usr/bin/pkill killmenow',
}