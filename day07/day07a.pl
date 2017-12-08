# AoC 2017 - day 7 pt 1 - perl implementation
# Solution by rhe 2017-12-07
# Note: input data is expected to be in file "day<daynum>.in"

use v5.8.4;
use strict;
use warnings;
use English;

my $teststr = <<EOL;
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
EOL

my $testcases = [
 [$teststr, "tknk"],
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
  #print join("+", @$lines)."\n";
  my %keys;
  my %values;
  foreach my $line (@$lines) {
    my ($k, $v) = split(/ -> /, $line);
    #print "k=$k; v=$v\n";
    $k =~ m/^(\w+) \(\d+\)$/;
    my $key = $1;
    $keys{$key} += 1;
    #print "key=$key\n";
    if (defined $v) {
      my @vals = split /, /, $v;
      foreach my $val (@vals) {
        $values{$val} +=1;
      }
    }
  }
  foreach my $v (keys %values) {
    delete $keys{$v};
  }
  foreach my $k (keys %keys) {
    print "left key=$k\n";
  }
  my @ks = keys(%keys);
  return $ks[0];
}

## MAIN

# test cases
foreach my $a (@$testcases) {
  my $result = solve($a->[0]);
  print "test input=".$a->[0].", solution='$result', expected='".$a->[1]."'\n";
  die "ABORT: test failed!" if $result ne $a->[1];
}

# individual input
my $input = read_file(get_infile_name());
#-print "input=$input\n";
print "data solution=".solve($input)."\n";
