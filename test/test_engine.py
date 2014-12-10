#! /usr/bin/env python

"""test_event.py class for testing the engine event.

:author:    Jose Carlos Recuero
:version:   0.1
:since:     12/07/2014

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
import mock

#
# import engine python modules
#
import engine
import event

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
        self.eng = engine.Engine()
        self.events = {}
        for i in xrange(5):
            ev = event.Event('%s' % i, i+1, mock.Mock(), i+1)
            self.events[i+1] = ev
            self.eng.addEvent(ev)

    #--------------------------------------------------------------------------
    def tearDown(self):
        pass

    #--------------------------------------------------------------------------
    def test_init(self):
        pass

    #--------------------------------------------------------------------------
    def test_run(self):
        # Test
        self.eng.runEngine()

        # Expectations
        for i, ev in self.events.iteritems():
            ev.cb.assert_called_once_with(i)



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
