#!/bin/env python3

import sys

from default_pool import create_resource_pool

if __name__ == "__main__":
    pool = create_resource_pool()

    TARGET_RATE = 2
    FACILITY_SPEED = 1
    resources = [
        "Electromagnetic Matrix",
        "Energy Matrix",
        "Structure Matrix",
        "Information Matrix",
        "Gravity Matrix",
    ]
    pool.create_resource_graph(
        resources, requested_rate=TARGET_RATE, facility_speed=FACILITY_SPEED
    )
