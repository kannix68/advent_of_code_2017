# AoC 2017 - day 6 pt 1 - perl implementation
# Solution by rhe 2017-12-06
# Note: input data is expected to be in file "day<daynum>.in"

use v5.8.4;
use strict;
use warnings;
use English;

my $testcases = [
 ["0 2 7 0", 4],
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
sub recombine($){
  my $cells = shift();
  my $stp = 0;
  my $combi = join(',', @$cells);
  my $ptr = find_maxval_idx($cells);
  my $blocks = $cells->[$ptr];
  #-print "step=$stp, ptr=$ptr, blocks=$blocks; combi=$combi\n";
  $cells->[$ptr] = 0;
  while ($blocks > 0) {
    $stp++;
    $ptr = ($ptr+1) % scalar(@$cells);
    $cells->[$ptr] += 1;
    $blocks--;
    $combi = join(',', @$cells);
    #-print "step=$stp, ptr=$ptr, blocks=$blocks; combi=$combi\n";
  }
  return $cells;
}

sub solve($) {
  my $instr = shift();
  my $cells = [split(/\s+/s, $instr)];
  my $combi;
  my %seen = ();
  my $step = 0;
  $combi = join(',', @$cells);
  do {
    $seen{$combi} = $step;
    $step++;
    #print "step=$step, combi=$combi\n";
    $cells = recombine($cells);
    $combi = join(',', @$cells);
  } while( not exists($seen{$combi}) );
  my $delta = $step - $seen{$combi};
  print "step=$step, final combi=$combi, first at ".$seen{$combi}.", delta=$delta\n";
  return $delta;
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
