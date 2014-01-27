#########################################################################
# -*- coding: utf-8 -*-
#
# SwapCallback
#
# Copyright (c) 2014 Rainer Müller <raimue@codingfarm.de>
#
# This file is part of the panStamp project.
#
# panStamp  is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# panStamp is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with panLoader; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301
# USA
#
#########################################################################
__author__="Rainer Müller"
__date__ ="$Date$"
#########################################################################

class SwapCallback:
    """
    SWAP callback for use in SwapManager, reacting on packet and network events
    """

    def swapPacketReceived(self, packet):
        """
        Called for each SWAP packet received

        @param packet: SWAP packet object
        """
        pass

    def swapPacketSent(self, packet):
        """
        Called for each SWAP packet sent

        @param packet: SWAP packet object
        """
        pass

    def __init__(self):
        pass
