# AoC 2017 - day 5 pt 1 - perl implementation
# Solution by rhe 2017-12-06
# Note: input data is expected to be in file "day<daynum>.in"

use v5.8.4;
use strict;
use warnings;
use English;

my $teststr = <<EOL;
0
3
0
1
-3
EOL

my $testcases = [
 [$teststr, 5],
];

## LIBRARY functions

# get input data file name
sub get_infile_name() {
  my $infile = $0;
  $infile =~ s/^.*?(day\d+).*$/$1/;
  $infile .= ".in";
  #-print "infile=$infile\n";
  return $infile;
}

# read first line of file
sub read_file_line($) {
  my $infile = shift();
  open(my $fh, $infile) or die "Could not open $infile: $!";
  my $line = <$fh>;
  chomp($line);
  close($fh);
  return $line;
}

# read all lines of file into array-of-strings
sub read_file_lines($) {
  my $infile = shift();
  my @lines = ();
  open(my $fh, $infile) or die "Could not open $infile: $!";
  while(my $line = <$fh>) {
    chomp($line);
    push @lines, $line;
  }
  close($fh);
  return \@lines;
}

# read all lines of file into array-of-strings
sub read_file($) {
  my $infile = shift();
  my $lines = "";
  open(my $fh, $infile) or die "Could not open $infile: $!";
  while(my $line = <$fh>) {
    $lines .= $line;
  }
  close($fh);
  return $lines;
}

## SOLUTION domain

# solution function

sub solve($) {
  my $instr = shift();
  my @cells = split(/\s+/s, $instr);
  #-print join(',', @cells) . "\n";
  my $ptr = 0;
  my $steps = 0;
  while (($ptr >= 0) and ($ptr < scalar(@cells))) {
    $steps++;
    my $ptr2 = $cells[$ptr];
    $cells[$ptr] += 1;
    $ptr = $ptr + $ptr2;
    #-print "new step=#$steps, jumped $ptr2: at $ptr, " . join(',', @cells) . "\n";
  }
  return $steps;
}

## MAIN

# test cases
foreach my $a (@$testcases) {
  my $result = solve($a->[0]);
  print "test input=".$a->[0].", solution=$result, expected=".$a->[1]."\n";
  die "ABORT: test failed!" if $result != $a->[1];
}

# individual input
my $input = read_file(get_infile_name());
#-print "input=$input\n";
print "data solution=".solve($input)."\n";
