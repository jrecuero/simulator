#! /usr/bin/env python

"""engine.py class required for the engine.

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
import collections

#
# import engine python modules
#
import loggerator


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
class Engine(object):
    """Engine is the simulator engine.
    """

    #--------------------------------------------------------------------------
    def __init__(self):
        """ Engine initialization method.
        
        >>> eng = Engine()
        >>> eng.simTime
        0
        >>> eng.runQ
        defaultdict(<type 'list'>, {})
        >>> eng.waitQ
        defaultdict(<type 'list'>, {})
        >>> eng.runEv
        """
        self.simTime = 0
        self.runQ    = collections.defaultdict(list)
        self.waitQ   = collections.defaultdict(list)
        self.runEv   = None
        self.logger  = loggerator.getLoggerator('ENGINE')

    #--------------------------------------------------------------------------
    def addEvent(self, ev, fixTime=False):
        """ Add a new event to the engine.
        
        :type ev: event.Event
        :param ev: Event to be added to the engine
        """
        ev.time = ev.time if fixTime else ev.time + self.simTime
        self.runQ[ev.time].append(ev)

    #--------------------------------------------------------------------------
    def nextEvent(self):
        """Look for the first entry in the list of pending event to be executed."""
        if len(self.runQ) == 0:
            return False
        keys = self.runQ.keys()
        keys.sort()
        self.runEv = self.runQ[keys[0]]
        del self.runQ[keys[0]]
        return True

    #--------------------------------------------------------------------------
    def runEvent(self):
        """Run every event in the list of events ready to run.
        """
        if self.runEv:
            self.simTime = self.runEv[0].time
            map(self.runEv.run, self.runEv)

    #--------------------------------------------------------------------------
    def runEngine(self):
        """ Run the full engine.
        """
        while self.nextEvent():
            for ev in self.runEv:
                self.simTime = ev.time
                self.logger.info('Engine : run : %s : simtime:%s' % (ev.name, self.simTime))
                ev.run()


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