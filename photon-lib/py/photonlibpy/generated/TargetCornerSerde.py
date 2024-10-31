###############################################################################
## Copyright (C) Photon Vision.
###############################################################################
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <https://www.gnu.org/licenses/>.
###############################################################################

###############################################################################
## THIS FILE WAS AUTO-GENERATED BY ./photon-serde/generate_messages.py.
##                        --> DO NOT MODIFY <--
###############################################################################

from ..targeting import *


class TargetCornerSerde:

    # Message definition md5sum. See photon_packet.adoc for details
    MESSAGE_VERSION = "16f6ac0dedc8eaccb951f4895d9e18b6"
    MESSAGE_FORMAT = "float64 x;float64 y;"

    @staticmethod
    def unpack(packet: "Packet") -> "TargetCorner":
        ret = TargetCorner()

        # x is of intrinsic type float64
        ret.x = packet.decodeDouble()

        # y is of intrinsic type float64
        ret.y = packet.decodeDouble()

        return ret


# Hack ourselves into the base class
TargetCorner.photonStruct = TargetCornerSerde()
