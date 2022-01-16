from resource_pool import ResourcePool


def create_resource_pool():
    pool = ResourcePool()

    pool.add_resource("Ray Receiver", 8, 1)
    pool.add_resource("EM Rail Ejector", 6, 1)
    pool.add_resource("Small Carrier Rocket", 6, 1)
    pool.add_resource("Solar Sail", 4, 2)

    pool.add_resource("Gravity Matrix", 24, 2, fixed_facility_speed=1)
    pool.add_resource("Electromagnetic Matrix", 3, 1, fixed_facility_speed=1)
    pool.add_resource("Energy Matrix", 6, 1, fixed_facility_speed=1)
    pool.add_resource("Structure Matrix", 8, 1, fixed_facility_speed=1)
    pool.add_resource("Information Matrix", 10, 1, fixed_facility_speed=1)

    pool.add_resource("Graviton Lens", 6, 1)
    pool.add_resource("Dyson Sphere Component", 8, 1)
    pool.add_resource("Deuteron Fuel Rod", 12, 2)
    pool.add_resource("Frame Material", 6, 1)
    pool.add_resource("Quantum Chip", 6, 1)
    pool.add_resource("Strange Matter", 8, 1, fixed_facility_speed=1)
    pool.add_resource("Particle Broadband", 8, 1)
    pool.add_resource("Particle Container", 4, 1)
    pool.add_resource("Electromagnetic Turbine", 2, 1)
    pool.add_resource("Electric Motor", 2, 1)
    pool.add_resource("Super Magnetic Ring", 3, 1)
    pool.add_resource("Magnetic Coil", 1, 2)
    pool.add_resource("Processor", 3, 1)
    pool.add_resource("Carbon Nanotube", 4, 2, fixed_facility_speed=1)
    pool.add_resource("Plane Filter", 12, 1)
    pool.add_resource("Circuit Board", 1, 2)
    pool.add_resource("Microcrystalline Component", 2, 1)
    pool.add_resource("Photon Combiner", 3, 1)
    pool.add_resource("Casimir Crystal", 4, 1)
    pool.add_resource("Titanium Glass", 5, 2)
    pool.add_resource("Titanium Crystal", 4, 1)
    pool.add_resource("Gear", 1, 1)
    pool.add_resource("Prism", 2, 2)
    pool.add_resource("Steel", 3, 1)
    pool.add_resource("Energetic Graphite", 2, 1)
    pool.add_resource("Titanium Alloy", 12, 4)
    pool.add_resource("Copper Ingot", 1, 1)
    pool.add_resource("Iron Ingot", 1, 1)
    pool.add_resource("Titanium Ingot", 2, 1)
    pool.add_resource("High Purity Silicon", 2, 1)

    pool.add_resource("Organic Crystal")
    pool.add_resource("Crystal Silicon")
    pool.add_resource("Water")
    pool.add_resource("Plastic")
    pool.add_resource("Glass", 2, 1)
    pool.add_resource("Magnet", 1.5, 1)
    pool.add_resource("Graphene")
    pool.add_resource("Stone")
    pool.add_resource("Diamond")
    pool.add_resource("Deuterium")
    pool.add_resource("Hydrogen")
    pool.add_resource("Copper Ore")
    pool.add_resource("Iron Ore")
    pool.add_resource("Coal")
    pool.add_resource("Silicon Ore")
    pool.add_resource("Titanium Ore")
    pool.add_resource("Sulphuric Acid")

    pool.add_dependency("Copper Ingot", "Copper Ore", 1)
    pool.add_dependency("Iron Ingot", "Iron Ore", 1)
    pool.add_dependency("High Purity Silicon", "Silicon Ore", 2)
    pool.add_dependency("Titanium Ingot", "Titanium Ore", 2)

    pool.add_dependency("Energetic Graphite", "Coal", 2)

    pool.add_dependency("Titanium Alloy", "Titanium Ingot", 4)
    pool.add_dependency("Titanium Alloy", "Steel", 3)
    pool.add_dependency("Titanium Alloy", "Sulphuric Acid", 8)

    pool.add_dependency("Steel", "Iron Ingot", 3)

    pool.add_dependency("Ray Receiver", "Steel", 20)
    pool.add_dependency("Ray Receiver", "High Purity Silicon", 20)
    pool.add_dependency("Ray Receiver", "Photon Combiner", 10)
    pool.add_dependency("Ray Receiver", "Processor", 5)
    pool.add_dependency("Ray Receiver", "Super Magnetic Ring", 20)

    pool.add_dependency("EM Rail Ejector", "Steel", 20)
    pool.add_dependency("EM Rail Ejector", "Gear", 20)
    pool.add_dependency("EM Rail Ejector", "Processor", 5)
    pool.add_dependency("EM Rail Ejector", "Super Magnetic Ring", 10)

    pool.add_dependency("Solar Sail", "Graphene", 1)
    pool.add_dependency("Solar Sail", "Photon Combiner", 1)

    pool.add_dependency("Small Carrier Rocket", "Dyson Sphere Component", 2)
    pool.add_dependency("Small Carrier Rocket", "Deuteron Fuel Rod", 4)
    pool.add_dependency("Small Carrier Rocket", "Quantum Chip", 2)

    pool.add_dependency("Dyson Sphere Component", "Frame Material", 3)
    pool.add_dependency("Dyson Sphere Component", "Solar Sail", 3)
    pool.add_dependency("Dyson Sphere Component", "Processor", 3)

    pool.add_dependency("Deuteron Fuel Rod", "Titanium Alloy", 1)
    pool.add_dependency("Deuteron Fuel Rod", "Deuterium", 20)
    pool.add_dependency("Deuteron Fuel Rod", "Super Magnetic Ring", 1)

    pool.add_dependency("Frame Material", "Carbon Nanotube", 4)
    pool.add_dependency("Frame Material", "Titanium Alloy", 1)
    pool.add_dependency("Frame Material", "High Purity Silicon", 1)

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

    pool.add_dependency("Super Magnetic Ring", "Electromagnetic Turbine", 2)
    pool.add_dependency("Super Magnetic Ring", "Magnet", 3)
    pool.add_dependency("Super Magnetic Ring", "Energetic Graphite", 1)

    pool.add_dependency("Photon Combiner", "Prism", 2)
    pool.add_dependency("Photon Combiner", "Circuit Board", 1)

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

    pool.add_dependency("Prism", "Glass", 3)
    pool.add_dependency("Gear", "Iron Ingot", 1)

    pool.add_dependency("Magnet", "Iron Ore", 1)

    pool.add_dependency("Glass", "Stone", 2)

    pool.add_dependency("Circuit Board", "Iron Ingot", 2)
    pool.add_dependency("Circuit Board", "Copper Ingot", 1)

    pool.add_dependency("Microcrystalline Component", "High Purity Silicon", 2)
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
    return pool
