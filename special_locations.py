#!/usr/bin/env python2
#
# Use available logging data to determine where "home" and "work" are, without
# use of user-defined HOMELOC data.
#
# Copyright (C) 2014 George C. Privon
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import magellan
import argparse


parser = argparse.ArgumentParser(description='Discern special locations for \
                                 a given timeframe. Includes a home location \
                                 and a work location.')
parser.add_argument('-p', '--period', action='store', type=str default='week',
                    help='Analysis period. Options: week (default) or month.')
parser.add_argument('-w', '--week', action='store', type=int,
                    default=False, help='Week to analyze (default, uses most \
                    recent week)')
parser.add_argument('-m', '--month', action='store', type=int,
                    default=False, help='Month to analyze')
parser.add_argument('-y', '--year', action='store', type=int,
                    default=False, help='Year. If not given, the current year \
                    is used.')
args = parser.parse_args()

# Work flow
# 1. Weed out traveling data
#    a. Load data from requested time interval and a longer interval (e.g.,
#       user requests week, load also previous month's worth of data)
#    b. Determine local timezone and time for each record.
#    c. Collect all location records by (nighttime, working time) for longer
#       interval.
#    d. Iteratively average and sigma-clip to remove traveling points.
#    e. Use remaining data to establish a baseline prior for home and work
#       locations.
# 2. Categorize individual events from the desired time period by their status
#    b. Use average night time (11pm – 5am) location to determine home location
#    c. Use average daytime (11am – 4pm) location, plus some distance sigma-
#       clipping to determine work location.
# 3. User verification
#    a. Use OSM nomatim to look up a name for the averaged location
#    b. Propose new work and home locations, displaying OSM nomatim result
#       and GPS locations.

# Open questions with the above method
# - track night by night in order to determine if many successive nights were
#   spent in the same place?
# - use long-term data to add some "intertia" to the determination of home and
#   work locations? I.e., if there has been a fairly consistent night-time
#   location before, it will take a longer period of time in a new location
#   to force a suggestion.
# - Apply some sort of probability to the old location and the new location and
#   use this when suggesting a location to the user.
