#########################################################################
# -*- coding: utf-8 -*-
#
# SwapMonitor
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
from swap.protocol.SwapDefs import SwapFunction
from SwapCallback import SwapCallback

class SwapMonitor(SwapCallback):
    """
    Print each received and sent SWAP packet in raw form to stdout
    """

    def _get_message_type(self, packet):
        """
        Return string defining the type of message

        @param packet: SWAP packet

        @return string
        """
        if packet.function == SwapFunction.COMMAND:
            msgtype = "C"
        elif packet.function == SwapFunction.QUERY:
            msgtype = "Q"
        elif packet.function == SwapFunction.STATUS:
            msgtype = "S"
        else:
            msgtype = "?"

        return msgtype

    def swapPacketReceived(self, packet):
        msgtime = time.strftime("%Y-%m-%d %H:%M:%S")
        msgtype = self._get_message_type(packet)
        print "[{}] {:>3} <-{}-- {:<3} {}".format(msgtime, packet.srcAddress, msgtype, packet.destAddress, packet.toString())

    def swapPacketSent(self, packet):
        msgtime = time.strftime("%Y-%m-%d %H:%M:%S")
        msgtype = self._get_message_type(packet)
        print "[{}] {:>3} --{}-> {:<3} {}".format(msgtime, packet.srcAddress, msgtype, packet.destAddress, packet.toString())

    def __init__(self):
        pass
