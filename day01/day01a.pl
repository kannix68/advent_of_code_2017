# AoC 2017 - day 1 pt 1 - perl implementation
# rhe 2017-12-01

use v5.8.4;
use strict;
use warnings;
use English;

my $testcases = [
 ['1122', 3],
 ['1111', 4],
 ['1234', 0],
 ['91212129', 9],
];

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
  my @chars = split //, $instr;
  push @chars, $chars[0]; # last char handling
  @chars = reverse @chars; # look-behind
  my $lastchar = '';
  my $sum = 0;
  foreach my $char (@chars) { # iterate chars
    if ($char eq $lastchar) {
	  $sum += $char;
	}
	$lastchar = $char;
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
my $input = read_file_line("day01.in");
#-print "input=$input\n";
print "data solution=".solve($input)."\n";
