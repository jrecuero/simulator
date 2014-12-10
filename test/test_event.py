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
        self.evCb = mock.Mock()
        self.ev   = event.Event('test event', 100.0, self.evCb, 0, 1, 2)

    #--------------------------------------------------------------------------
    def tearDown(self):
        self.ev = None

    #--------------------------------------------------------------------------
    def test_init(self):
        """ Test Event.servicer method with standard parameters
        """
        # Expectations
        self.assertEqual(self.ev.name, 'test event', 'test event name error')
        self.assertEqual(self.ev.time, 100.0, 'test event simulation time error')
        self.assertEqual(self.ev.cb, self.evCb, 'test event callback error')
        self.assertEqual(self.ev.cbArgs, (0, 1, 2), 'test event callback error')

    #--------------------------------------------------------------------------
    def test_run(self):
        """ Test Event.run method with standard behavior
        """
        # Test
        self.ev.run()

        # Expectations
        self.evCb.assert_called_once_with(0, 1, 2)


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
