#!/usr/bin/env python

from __future__ import division

from DoMonit.domonit.containers import Containers
from DoMonit.domonit.ids import Ids
from DoMonit.domonit.inspect import Inspect
from DoMonit.domonit.process import Process
from DoMonit.domonit.stats import Stats

c = Containers()
i = Ids()
print(f"i == {i}")
print("Number of containers is : %s " % (sum(1 for i in i.ids())))

if __name__ == "__main__":

    for c_id in i.ids():
        ins = Inspect(c_id)
        sta = Stats(c_id)
        proc = Process(c_id, ps_args="aux")

        # Container name
        print("\n#Container name")
        print(ins.name())

        # Container id
        print("\n#Container id")
        print(ins.id())

        # Memory usage
        mem_u = sta.memory_stats_usage()

        # Memory limit
        mem_l = sta.memory_stats_limit()

        # Memory usage %
        print("\n#Memory usage %")
        print(int(mem_u) * 100 / int(mem_l))

        # The number of times that a process of the cgroup triggered a "major fault"
        print("\n#The number of times that a process of the cgroup triggered a major fault")
        print(sta.memory_stats_stats_pgmajfault())

        # Same output as ps aux in *nix
        print("\n#Same output as ps aux in *nix")
        print(proc.ps())
