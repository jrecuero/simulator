#! /usr/bin/env python

"""test_simulator.py class for testing the simulator.

:author:    Jose Carlos Recuero
:version:   0.1
:since:     12/10/2014

"""

__docformat__ = 'restructuredtext en'

###############################################################################
##  _                            _
## (_)_ __ ___  _ __   ___  _ __| |_ ___
## | | '_ ` _ \| '_ \ / _ \| '__| __/ __|
## | | | | | | | |_) | (_) | |  | |_\__ \
## |_|_| |_| |_| .__/ \___/|_|   \__|___/
##             |_|
###############################################################################
#
# import std python modules
#
import unittest
#import mock

#
# import engine python modules
#
from engine                     import Engine
from device.tasker_generator    import TaskerGenerator
from device.queuer              import Queuer
from device.servicer            import Servicer


###############################################################################
##       _                     _       __ _       _ _   _
##   ___| | __ _ ___ ___    __| | ___ / _(_)_ __ (_) |_(_) ___  _ __  ___
##  / __| |/ _` / __/ __|  / _` |/ _ \ |_| | '_ \| | __| |/ _ \| '_ \/ __|
## | (__| | (_| \__ \__ \ | (_| |  __/  _| | | | | | |_| | (_) | | | \__ \
##  \___|_|\__,_|___/___/  \__,_|\___|_| |_|_| |_|_|\__|_|\___/|_| |_|___/
##
###############################################################################
#

#
#------------------------------------------------------------------------------
class Test(unittest.TestCase):

    #--------------------------------------------------------------------------
    def setUp(self):
        self.eng = Engine()
        self.que = Queuer()
        self.gen = TaskerGenerator(self.eng,
                                   'taskerGen',
                                   self.que,
                                   taskStart=50.0,
                                   taskEnd=200.0,
                                   limit=10)
        self.svc = Servicer(self.que, self.eng)

    #--------------------------------------------------------------------------
    def tearDown(self):
        pass

    #--------------------------------------------------------------------------
    def test_init(self):
        pass

    #--------------------------------------------------------------------------
    def test_run(self):
        # Test
        self.gen.start()
        self.svc.start()
        self.eng.runEngine()

        # Expectations
        pass


###############################################################################
##                  _
##  _ __ ___   __ _(_)_ __
## | '_ ` _ \ / _` | | '_ \
## | | | | | | (_| | | | | |
## |_| |_| |_|\__,_|_|_| |_|
##
###############################################################################
#
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
