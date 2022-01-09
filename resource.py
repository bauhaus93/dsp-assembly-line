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
