#########################################################################
# -*- coding: utf-8 -*-
#
# SwapSniffer
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

import time
from SwapCallback import SwapCallback

class SwapSniffer(SwapCallback):
    """
    Print each received and sent SWAP packet in raw form to stdout
    """

    def swapPacketReceived(self, packet):
        msgtime = time.strftime("%Y-%m-%d %H:%M:%S")
        print "{} <-- ({:02X}{:02X}){}".format(msgtime, packet.rssi, packet.lqi, packet.toString())

    def swapPacketSent(self, packet):
        msgtime = time.strftime("%Y-%m-%d %H:%M:%S")
        print "{} --> ({:02X}{:02X}){}".format(msgtime, packet.rssi, packet.lqi, packet.toString())
