#!/bin/env python3

import sys
import uuid
from math import ceil


class Resource:
    def __init__(
        self,
        name: str,
        cycle_time: float = None,
        cycle_output: float = None,
        fixed_facility_speed: float = None,
    ):
        self.name = name
        self.cycle_time = cycle_time
        self.cycle_output = cycle_output
        self.fixed_facility_speed = fixed_facility_speed
        self.inputs = []

    def add_input(self, resource, cycle_input=1) -> None:
        self.inputs.append((resource, cycle_input))

    def output_rate(self, facility_speed: float) -> float:
        return self.cycle_output / (
            self.cycle_time / (self.fixed_facility_speed or facility_speed)
        )

    def create_resource_graph(
        self,
        target_output_rate: float,
        facility_speed=1,
    ) -> (str, float):
        effective_cycle_time = (
            self.cycle_time
            and self.cycle_time / (self.fixed_facility_speed or facility_speed)
            or None
        )
        output_facility_count = (
            effective_cycle_time
            and ceil(target_output_rate / self.output_rate(facility_speed))
            or None
        )
        node_name = "node_" + str(uuid.uuid4()).replace("-", "_")
        color = "aliceblue" if effective_cycle_time else "grey"
        print(f'{node_name} [label="{self.name}" fillcolor={color}; style=filled]')
        for (res, cycle_amount) in self.inputs:
            needed_input = (output_facility_count / effective_cycle_time) * cycle_amount
            sub_node_name, facility_count = res.create_resource_graph(
                needed_input, facility_speed
            )
            facility_label = f' [label="{facility_count}"]' if facility_count else ""
            print(f"{sub_node_name} -> {node_name}{facility_label};")
        return (node_name, output_facility_count)


class ResourcePool:
    def __init__(self):
        self.resource = {}

    def add_resource(
        self,
        name: str,
        cycle_time: float = None,
        cycle_output: float = None,
        fixed_facility_speed: float = None,
    ) -> None:
        self.resource[name] = Resource(
            name, cycle_time, cycle_output, fixed_facility_speed
        )

    def add_dependency(
        self, target_res_name: str, input_res_name: str, input_amount: float
    ) -> None:
        self.resource[target_res_name].add_input(
            self.resource[input_res_name], input_amount
        )

    def create_resource_graph(
        self, resource_names: [str], requested_rate: float, facility_speed: float = 1
    ) -> None:
        print(f"digraph resource_graph" + " {\nnode [shape=record];")
        for res_name in resource_names:
            name = res_name.replace(" ", "_").lower()
            print(f"subgraph resource_graph_{name} {{")
            self.resource[res_name].create_resource_graph(
                requested_rate, facility_speed
            )
            print("}")
        print("}")


pool = ResourcePool()
pool.add_resource("Gravity Matrix", 24, 2)
pool.add_resource("Electromagnetic Matrix", 3, 1)
pool.add_resource("Energy Matrix", 6, 1)
pool.add_resource("Structure Matrix", 8, 1)
pool.add_resource("Information Matrix", 10, 1)
pool.add_resource("Graviton Lens", 6, 1)
pool.add_resource("Quantum Chip", 6, 1)
pool.add_resource("Strange Matter", 8, 1, fixed_facility_speed=1)
pool.add_resource("Particle Broadband", 8, 1)
pool.add_resource("Particle Container", 4, 1)
pool.add_resource("Electromagnetic Turbine", 2, 1)
pool.add_resource("Electric Motor", 2, 1)
pool.add_resource("Magnetic Coil", 1, 2)
pool.add_resource("Processor", 3, 1)
pool.add_resource("Carbon Nanotube", 4, 2)
pool.add_resource("Plane Filter", 12, 1)
pool.add_resource("Circuit Board", 1, 2)
pool.add_resource("Microcrystalline Component", 2, 1)
pool.add_resource("Casimir Crystal", 4, 1)
pool.add_resource("Titanium Glass", 5, 2)
pool.add_resource("Titanium Crystal", 4, 1)
pool.add_resource("Gear", 1, 1)
pool.add_resource("Energetic Graphite", 2, 1)
pool.add_resource("Copper Ingot")
pool.add_resource("Iron Ingot")
pool.add_resource("Titanium Ingot")
pool.add_resource("High Purity Silicon")
pool.add_resource("Organic Crystal")
pool.add_resource("Crystal Silicon")
pool.add_resource("Water")
pool.add_resource("Plastic")
pool.add_resource("Glass")
pool.add_resource("Magnet")
pool.add_resource("Graphene")
pool.add_resource("Diamond")
pool.add_resource("Deuterium")
pool.add_resource("Hydrogen")

pool.add_dependency("Gravity Matrix", "Graviton Lens", 1)
pool.add_dependency("Gravity Matrix", "Quantum Chip", 1)

pool.add_dependency("Electromagnetic Matrix", "Magnetic Coil", 1)
pool.add_dependency("Electromagnetic Matrix", "Circuit Board", 1)

pool.add_dependency("Energy Matrix", "Energetic Graphite", 2)
pool.add_dependency("Energy Matrix", "Hydrogen", 2)

pool.add_dependency("Structure Matrix", "Diamond", 1)
pool.add_dependency("Structure Matrix", "Titanium Crystal", 1)


pool.add_dependency("Information Matrix", "Processor", 2)
pool.add_dependency("Information Matrix", "Particle Broadband", 1)

pool.add_dependency("Graviton Lens", "Diamond", 4)
pool.add_dependency("Graviton Lens", "Strange Matter", 1)


pool.add_dependency("Particle Broadband", "Carbon Nanotube", 2)
pool.add_dependency("Particle Broadband", "Crystal Silicon", 2)
pool.add_dependency("Particle Broadband", "Plastic", 1)

pool.add_dependency("Strange Matter", "Particle Container", 2)
pool.add_dependency("Strange Matter", "Iron Ingot", 2)
pool.add_dependency("Strange Matter", "Deuterium", 10)

pool.add_dependency("Particle Container", "Electromagnetic Turbine", 2)
pool.add_dependency("Particle Container", "Copper Ingot", 2)
pool.add_dependency("Particle Container", "Graphene", 2)

pool.add_dependency("Electromagnetic Turbine", "Electric Motor", 2)
pool.add_dependency("Electromagnetic Turbine", "Magnetic Coil", 2)

pool.add_dependency("Magnetic Coil", "Magnet", 2)
pool.add_dependency("Magnetic Coil", "Copper Ingot", 1)

pool.add_dependency("Electric Motor", "Iron Ingot", 2)
pool.add_dependency("Electric Motor", "Gear", 1)
pool.add_dependency("Electric Motor", "Magnetic Coil", 1)

pool.add_dependency("Quantum Chip", "Processor", 2)
pool.add_dependency("Quantum Chip", "Plane Filter", 2)

pool.add_dependency("Carbon Nanotube", "Graphene", 3)
pool.add_dependency("Carbon Nanotube", "Titanium Ingot", 1)

pool.add_dependency("Processor", "Circuit Board", 2)
pool.add_dependency("Processor", "Microcrystalline Component", 2)

pool.add_dependency("Circuit Board", "Iron Ingot", 2)
pool.add_dependency("Circuit Board", "Copper Ingot", 1)

pool.add_dependency("Microcrystalline Component", "Titanium Ingot", 2)
pool.add_dependency("Microcrystalline Component", "Copper Ingot", 1)

pool.add_dependency("Plane Filter", "Casimir Crystal", 1)
pool.add_dependency("Plane Filter", "Titanium Glass", 2)

pool.add_dependency("Casimir Crystal", "Titanium Crystal", 1)
pool.add_dependency("Casimir Crystal", "Graphene", 2)
pool.add_dependency("Casimir Crystal", "Hydrogen", 12)

pool.add_dependency("Titanium Crystal", "Organic Crystal", 1)
pool.add_dependency("Titanium Crystal", "Titanium Ingot", 3)

pool.add_dependency("Titanium Glass", "Glass", 2)
pool.add_dependency("Titanium Glass", "Titanium Ingot", 2)
pool.add_dependency("Titanium Glass", "Water", 2)

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
