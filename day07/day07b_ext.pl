# code !stolen!
# see: [-- 2017 Day 7 Solutions -- : adventofcode](https://www.reddit.com/r/adventofcode/comments/7i44pg/2017_day_7_solutions/)
# https://www.reddit.com/r/adventofcode/comments/7i44pg/2017_day_7_solutions/dqwg41b/


my (@ready, %parent);
while (<>) {
  /^(?<program>\w+) \((?<weight>\d+)\)( -> (?<dependency>.*))?/ or die;
  my $node = {
        name => $+{program},
        own_weight => $+{weight},
        total_weight => $+{weight},
      };
  if ($+{dependency}) {
    my @child = split /, /, $+{dependency};
    $node->{unknown_dependencies} = @child;
    $parent{$_} = $node foreach @child;
  }
  else {
    push @ready, $node;
  }
}

my $wonky;
while (my $child = shift @ready) {
  my $parent = delete $parent{$child->{name}};
  $parent->{total_weight} += $child->{total_weight};
  push @{$parent->{child_weighing}{$child->{total_weight}}}, $child;
  if (--$parent->{unknown_dependencies} == 0) {
    push @ready, $parent;
    $wonky = $parent
        if keys %{$parent->{child_weighing}} > 1
            && (!$wonky || $parent->{total_weight} < $wonky->{total_weight});
  }
}

my ($bad_node, $right_total_weight);
while (my ($weight, $child) = each %{$wonky->{child_weighing}}) {
  if (@$child == 1) {
    $bad_node = $child->[0];
  }
  else {
    $right_total_weight = $weight;
  }
}
#say "$bad_node->{name} should have weight ",
print "$bad_node->{name} should have weight ",
    $bad_node->{own_weight} - $bad_node->{total_weight} + $right_total_weight . "\n";
