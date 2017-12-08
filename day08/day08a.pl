# AoC 2017 - day 8 pt 1 - perl implementation
# Solution by rhe 2017-12-08
# Note: input data is expected to be in file "day<daynum>.in"

use v5.8.4;
use strict;
use warnings;
use English;

use Data::Dumper;
use List::Util qw(max);

$Data::Dumper::Terse = 1;  # don't output names where feasible
$Data::Dumper::Indent = 0;  # turn off all pretty print

my $teststr = <<EOL;
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
EOL

my $testcases = [
 [$teststr, 1],
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
sub read_str_lines($) {
  my $instr = shift();
  my @lines = split /\n/, $instr;
  return \@lines;
}

# find index of maximum array value
sub find_maxval_idx($) {
  my $aref = shift(); 
  my $maxidx;
  my $maxval = undef;
  for(my $i=0; $i<scalar(@$aref); $i++){
    my $v = $aref->[$i];
    if (not defined($maxval) or $maxval < $v) {
      $maxidx = $i;
      $maxval = $v;
    }
  }
  return $maxidx;
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
  my $lines = read_str_lines($instr);
  my %regs;
  foreach my $line (@$lines) {
    print "line=$line\n";
    #c dec -10 if a >= 1
    $line =~ m/^(\w+) (inc|dec) ([\-0-9]+) if (\w+) ([<>=!]+) ([\-0-9]+)$/;
    my ($reg1, $cmd, $inc, $reg2, $op, $cmp) = ($1, $2, $3, $4, $5, $6);
    if (not exists($regs{$reg1})) {
      $regs{$reg1} = 0;
    }
    if (not exists($regs{$reg2})) {
      $regs{$reg2} = 0;
    }
    if (
      ($op eq '==' and $regs{$reg2} == $cmp)
      or ($op eq '!=' and $regs{$reg2} != $cmp)
      or ($op eq '<' and $regs{$reg2} < $cmp)
      or ($op eq '>' and $regs{$reg2} > $cmp)
      or ($op eq '<=' and $regs{$reg2} <= $cmp)
      or ($op eq '>=' and $regs{$reg2} >= $cmp)
    ){
      print "do! " . Dumper(\%regs) . "\n";
      my $add = $inc;
      if ($cmd eq 'dec') {
        $add *= -1;
      }
      print "$reg1 += $add\n";
      $regs{$reg1} += $add;
      print "regs=" . Dumper(\%regs) . "\n";
    }
  }
  print "final-regs=" . Dumper(\%regs) . "\n";
  return max(values(%regs));
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
