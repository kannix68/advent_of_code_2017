# AoC 2017 - day 4 pt 2 - perl implementation
# Solution by rhe 2017-12-04
# Note: input data is expected to be in file "day<daynum>.in"

use v5.8.4;
use strict;
use warnings;
use English;

my $testcases = [
 ["abcde fghij", 1],
 ["abcde xyz ecdab", 0],
 ["a ab abc abd abf abj", 1],
 ["iiii oiii ooii oooi oooo", 1],
 ["oiii ioii iioi iiio", 0],
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
  my @tokens = split(/ +/, $instr);
  my %check = ();
  foreach my $token (@tokens) {
    $token = join('', sort(split(//, $token))); #build sorted non-unique set
    $check{$token} += 1;
    if ($check{$token} > 1) {
      return 0;
    }
  }
  return 1;
}

## MAIN

# test cases
foreach my $a (@$testcases) {
  my $result = solve($a->[0]);
  print "test input=".$a->[0].", solution=$result, expected=".$a->[1]."\n";
  die "ABORT: test failed!" if $result != $a->[1];
}

# individual input
my $lines = read_file_lines(get_infile_name());
my $ok = 0;
foreach my $line (@$lines) {
  #print "$line\n";
  $ok += solve($line);
}
#-print "input=$input\n";
#print "data solution=".solve($input)."\n";
print "passphrases ok=$ok\n";