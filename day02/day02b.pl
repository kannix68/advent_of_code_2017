# AoC 2017 - day 2 pt 2 - perl implementation
# Solution by rhe 2017-12-02
# Note: input data is expected to be in file "day<daynum>.in"

use v5.8.4;
use strict;
use warnings;
use English;

use List::Util qw(min max);

my $testin = <<EOL;
5 9 2 8
9 4 7 3
3 8 6 5
EOL

my $testcases = [
 [$testin, 9],
];

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


# solution function
# index based lookup of character to compare, with modulo-overflow-handling
sub solve($) {
  my $instr = shift();
  my @lines = split(/\n/, $instr);
  my $chksum = 0;
  foreach my $line (@lines) {
    my @tokens = split /\s+/, $line;
    OUTER: foreach my $token (@tokens) {
      foreach my $tok2 (@tokens) {
        if (($token < $tok2) and ($tok2 % $token == 0)) {
          #-print "found $tok2 and $token\n"; 
          $chksum += $tok2/$token;
          last OUTER;
        }
      }
    }
  }
  return $chksum;
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
