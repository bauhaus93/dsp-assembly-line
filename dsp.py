#!/bin/env python3

import sys

from default_pool import create_resource_pool

MATRICES = [
    "Gravity Matrix",
    "Electromagnetic Matrix",
    "Energy Matrix",
    "Structure Matrix",
    "Information Matrix",
]

if __name__ == "__main__":
    pool = create_resource_pool()

    TARGET_RATE = 0.5
    FACILITY_SPEED = 1
    resources = ["Small Carrier Rocket"]

    pool.create_resource_graph(
        resources, requested_rate=TARGET_RATE, facility_speed=FACILITY_SPEED
    )
