#!/usr/bin/env python

import os
import sys
sys.path.insert(0, os.pardir)
from testing_harness import TestHarness, PyAPITestHarness
import openmc


class FilterEnergyTestHarness(PyAPITestHarness):
    def _build_inputs(self):
        filt = openmc.Filter(type='energy',
                             bins=(0.0, 0.253e-6, 1.0e-3, 1.0, 20.0))
        tally = openmc.Tally(tally_id=1)
        tally.add_filter(filt)
        tally.add_score('total')
        self._input_set.tallies = openmc.TalliesFile()
        self._input_set.tallies.add_tally(tally)

        super(FilterEnergyTestHarness, self)._build_inputs()

    def _cleanup(self):
        super(FilterEnergyTestHarness, self)._cleanup()
        f = os.path.join(os.getcwd(), 'tallies.xml')
        if os.path.exists(f): os.remove(f)


if __name__ == '__main__':
    harness = FilterEnergyTestHarness('statepoint.10.*', True)
    harness.main()
