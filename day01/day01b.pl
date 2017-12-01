# AoC 2017 - day 1 pt 2 - perl implementation
# Solution by rhe 2017-12-01
# Note: input data is expected to be in file "day<daynum>.in"

use v5.8.4;
use strict;
use warnings;
use English;

my $testcases = [
 ['1212', 6],
 ['1221', 0],
 ['123425', 4],
 ['123123', 12],
 ['12131415', 4],
];

# get input data file name
sub get_infile_name() {
  my $infile = $0;
  $infile =~ s/^.*?(day\d+).*$/$1/;
  $infile .= ".in";
  #-print "infile=$infile\n";
  return $infile;
}

# read first lien of file
sub read_file_line($) {
  my $infile = shift();
  open(my $fh, $infile) or die "Could not open $infile: $!";
  my $line = <$fh>;
  chomp($line);
  close($fh);
  return $line;
}

# itarate chars-array, change lookahead to lookbehind by reversing array,
#   consider last char handling
sub solve($) {
  my $instr = shift();
  my @chars = split(//, $instr);
  my $alen = scalar(@chars);
  my $sum = 0;
  my $jump = $alen/2; # part 1: =1
  for(my $i=0; $i<$alen; $i++) {
    my $char = $chars[$i];
    my $cmpchar = $chars[($i+$jump) % $alen];
    if ($char eq $cmpchar) {
      $sum += $char;
    }
  }
  return $sum;
}

## MAIN

# test cases
foreach my $a (@$testcases) {
  #-print "test: ".$a->[0].", ".$a->[1]."\n";
  my $result = solve($a->[0]);
  print "test input=".$a->[0].", solution=$result, expected=".$a->[1]."\n";
  die "ABORT: test failed!" if $result != $a->[1];
}

# individual input
my $input = read_file_line(get_infile_name());
#-print "input=$input\n";
print "data solution=".solve($input)."\n";
