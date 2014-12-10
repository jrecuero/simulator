#! /usr/bin/env python

"""queue.py class generates events.

:author:    Jose Carlos Recuero
:version:   0.1
:since:     12/09/2014

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
import random

#
# import engine python modules
#
import loggerator
import event


###############################################################################
##
##   ___ ___  _ __  ___| |_ __ _ _ __ | |_ ___
##  / __/ _ \| '_ \/ __| __/ _` | '_ \| __/ __|
## | (_| (_) | | | \__ \ || (_| | | | | |_\__ \
##  \___\___/|_| |_|___/\__\__,_|_| |_|\__|___/
##
###############################################################################
#

###############################################################################
##            _                     _   _
##  ___ _   _| |__  _ __ ___  _   _| |_(_)_ __   ___  ___
## / __| | | | '_ \| '__/ _ \| | | | __| | '_ \ / _ \/ __|
## \__ \ |_| | |_) | | | (_) | |_| | |_| | | | |  __/\__ \
## |___/\__,_|_.__/|_|  \___/ \__,_|\__|_|_| |_|\___||___/
##
###############################################################################
#


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
class Generator(object):
    """ Generates random events.
    """

    #--------------------------------------------------------------------------
    def __init__(self,
                 engine,
                 name,
                 cb=None,
                 cbArgs=None,
                 timeStart=1.0,
                 timeEnd=100.0,
                 limit=None):
        """ Generator initialization method.
        """
        self.engine    = engine
        self.counter   = 0
        self.name      = name
        self.timeStart = timeStart
        self.timeEnd   = timeEnd
        self.limit     = limit
        self.cb        = cb
        self.cbArgs    = cbArgs if cbArgs else ()
        self.logger    = loggerator.getLoggerator('GENERATOR')

    #--------------------------------------------------------------------------
    def _getName(self):
        """ Get name for a new generator event.
        """
        return '%s[%d]' % (self.name, self.counter)

    #--------------------------------------------------------------------------
    def _getTime(self):
        """ Get timeout for a new generator event.
        """
        return random.randint(self.timeStart, self.timeEnd)

    #--------------------------------------------------------------------------
    def _checkLimit(self):
        """ Check if event limit has been reached.
        """
        return self.limit and self.counter < self.limit

    #--------------------------------------------------------------------------
    def _createEvent(self):
        ev = event.Event(self._getName(), self._getTime(), self.next)
        self.logger.info('Generator : event : %s in %s' % (ev.name, ev.time))
        self.engine.addEvent(ev)
        self.counter += 1

    #--------------------------------------------------------------------------
    def _call(self):
        if self.cb:
            self.cb(*self.cbArgs)

    #--------------------------------------------------------------------------
    def start(self):
        if not self.counter:
            self._createEvent()

    #--------------------------------------------------------------------------
    def next(self):
        """ Generate a new event.
        """
        if self._checkLimit():
            self._createEvent()
            self._call()
        else:
            self.logger.warning('%s has reached the maximum number of events' % (self.name, ))


###############################################################################
##                  _
##  _ __ ___   __ _(_)_ __
## | '_ ` _ \ / _` | | '_ \
## | | | | | | (_| | | | | |
## |_| |_| |_|\__,_|_|_| |_|
##
###############################################################################
#
if __name__ == '__main__':
    import doctest
    doctest.testmod()
