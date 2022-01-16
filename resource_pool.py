from math import ceil, floor
from resource import Resource


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
        print("fontname=Courier;")

        input_per_resource = self.calculate_resource_input(
            resource_names, requested_rate, facility_speed
        )
        title = ""
        for res in input_per_resource:
            res_data = input_per_resource[res]
            title += f"{res}:{' ' * (30-len(res))}{floor(res_data['output']):5}/m\l"
            res_inputs = res_data["inputs"]
            sorted_inputs = sorted(
                res_inputs.items(), key=lambda kv: kv[1], reverse=True
            )
            for input_res, input_val in sorted_inputs:
                title += (
                    f"{input_res}:{' ' * (30-len(input_res))}{ceil(input_val):5}/m\l"
                )
            title += ("+" * 38) + "\l"

        print(f'label="{title}";')
        print(f"labelloc=top;")
        print(f"labeljust=left;")
        for res_name in resource_names:
            name = res_name.replace(" ", "_").lower()
            print(f"subgraph resource_graph_{name} {{")
            self.resource[res_name].create_resource_graph(
                requested_rate, facility_speed=facility_speed, is_root=True
            )
            print("}")
        print("}")

    def calculate_resource_input(
        self, resource_names: [str], requested_rate: float, facility_speed: float = 1
    ) -> dict:
        inputs_per_resource = {}
        for res_name in resource_names:
            inputs = self.resource[res_name].calculate_resource_input(
                requested_rate, facility_speed
            )
            for key in inputs:
                inputs[key] *= 60
            inputs_per_resource[res_name] = {
                "output": requested_rate * 60,
                "inputs": inputs,
            }
        return inputs_per_resource
