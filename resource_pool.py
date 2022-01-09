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
        for res_name in resource_names:
            name = res_name.replace(" ", "_").lower()
            print(f"subgraph resource_graph_{name} {{")
            self.resource[res_name].create_resource_graph(
                requested_rate, facility_speed
            )
            print("}")
        print("}")
