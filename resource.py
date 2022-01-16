import uuid
from math import ceil


class Resource:

    _next_id = 1

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

    @staticmethod
    def get_next_id():
        Resource._next_id += 1
        return Resource._next_id - 1

    def add_input(self, resource, cycle_input=1) -> None:
        self.inputs.append((resource, cycle_input))

    def output_rate(self, facility_speed: float) -> float:
        return self.cycle_output / (
            self.cycle_time / (self.fixed_facility_speed or facility_speed)
        )

    def get_effective_cycle_time(self, facility_speed: float) -> float:
        return (
            self.cycle_time
            and self.cycle_time / (self.fixed_facility_speed or facility_speed)
            or None
        )

    def get_output_facility_count(
        self, target_output_rate: float, facility_speed: float
    ) -> int:
        return (
            self.get_effective_cycle_time(facility_speed)
            and ceil(target_output_rate / self.output_rate(facility_speed))
            or None
        )

    def create_resource_graph(
        self, target_output_rate: float, facility_speed: float = 1, is_root=False
    ) -> (str, float):

        effective_cycle_time = self.get_effective_cycle_time(facility_speed)
        output_facility_count = self.get_output_facility_count(
            target_output_rate, facility_speed
        )

        node_name = "node_" + str(Resource.get_next_id())
        color = "aliceblue" if effective_cycle_time else "grey"
        label = (f"{output_facility_count} x " if is_root else "") + self.name
        print(f'{node_name} [label="{label}" fillcolor={color}; style=filled]')
        for (res, cycle_amount) in self.inputs:
            needed_input = (output_facility_count / effective_cycle_time) * cycle_amount
            sub_node_name, facility_count = res.create_resource_graph(
                needed_input, facility_speed
            )
            facility_label = (
                f' [label="{facility_count or ""}({needed_input * 60:.0f}/m)"]'
            )
            print(f"{sub_node_name} -> {node_name}{facility_label};")
        return (node_name, output_facility_count)

    def calculate_resource_input(
        self, requested_rate: float, facility_speed: float = 1
    ) -> dict:
        effective_cycle_time = self.get_effective_cycle_time(facility_speed)
        output_facility_count = self.get_output_facility_count(
            requested_rate, facility_speed
        )
        if not output_facility_count or not self.inputs:
            return {self.name: requested_rate}
        else:
            input_dict = {}
            for (res, cycle_amount) in self.inputs:
                needed_input = (
                    output_facility_count / effective_cycle_time
                ) * cycle_amount
                need_dict = res.calculate_resource_input(needed_input, facility_speed)
                for key in need_dict:
                    input_dict[key] = input_dict.get(key, 0) + need_dict[key]
            return input_dict
