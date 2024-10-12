
# Here is a useful link if you want to override autogenerated models: https://github.com/PixiGeko/Minecraft-default-assets/tree/latest/assets/minecraft/models/block

# Import database helper and setup constants
from python_datapack.utils.database_helper import *
from python_datapack.utils.ingredients import *
from python_datapack.constants import *
STARTING_CMD: int = 30000	# Prefix for custom_model_data

# Configuration to generate everything about the material based on "steel_ingot"
ORES_CONFIGS: dict[str, EquipmentsConfig|None] = {
	"steel_ingot":	EquipmentsConfig(
		# This steel is equivalent to iron,
		equivalent_to = DEFAULT_ORE.IRON,

		# But, has more durability (3 times more)
		pickaxe_durability = 3 * VanillaEquipments.PICKAXE.value[DEFAULT_ORE.IRON]["durability"],

		# And, does 1 more damage per hit (mainhand), and has 0.5 more armor, and mines 20% faster (pickaxe)
		attributes = {"generic.attack_damage": 1, "generic.armor": 0.5, "player.mining_efficiency": 0.2}
	),

	# Simple material stone, this will automatically detect stone stick and rod textures.
	"minecraft:stone": None,
}

# Main function should return a database
def main(config: dict) -> dict[str, dict]:
	database: dict[str,dict] = {}
	namespace: str = config["namespace"]

	# Generate ores in database (add every stuff related to steel and stone found in the textures folder to the database)
	generate_everything_about_these_materials(config, database, ORES_CONFIGS)

	# Generate custom disc records
	generate_custom_records(config, database, "auto")

	# Add a super stone block that can be crafted with 9 deepslate or stone, and has stone as base block
	database["super_stone"] = {
		"id": CUSTOM_BLOCK_VANILLA,											# Placeholder for the base block
		VANILLA_BLOCK: {"id": "minecraft:stone", "apply_facing": False},	# Base block
		RESULT_OF_CRAFTING: [												# Crafting recipes (shaped and shapeless examples)
			{"type":"crafting_shaped","result_count":1,"group":"super_stone","category":"blocks","shape":["XXX","XXX","XXX"],"ingredients": {"X": ingr_repr("minecraft:stone")}},
			{"type":"crafting_shapeless","result_count":1,"group":"super_stone","category":"blocks","ingredients": 9 * [ingr_repr("minecraft:deepslate")] },
		],
	}

	# Don't forget to add the vanilla blocks for the custom blocks (not automatic even though they was recognized by generate_everything_about_these_materials())
	database["steel_block"][VANILLA_BLOCK] = {"id": "minecraft:iron_block", "apply_facing": False}			# Placeholder for the base block
	database["raw_steel_block"][VANILLA_BLOCK] = {"id": "minecraft:raw_iron_block", "apply_facing": False}	# Placeholder for the base block
	for ore in ["steel_ore","deepslate_steel_ore"]:
		database[ore][VANILLA_BLOCK] = VANILLA_BLOCK_FOR_ORES	# Placeholder for the base block (required for custom ores)
		database[ore][NO_SILK_TOUCH_DROP] = "raw_steel"			# Drop without silk touch (raw_steel is an item in the database)

	# Add a recipe for the future generated manual (the manual recipe will show up in itself)
	manual_name: str = config.get("manual_name", "Manual")
	database["manual"] = {
		"id": "minecraft:written_book", "category": "misc", "item_name": f'"{manual_name}"',
		RESULT_OF_CRAFTING: [
			# Put a book and a steel ingot in the crafting grid to get the manual
			{"type":"crafting_shapeless","result_count":1,"group":"manual","category":"misc","ingredients": [ingr_repr("minecraft:book"), ingr_repr("steel_ingot", namespace)]},

			# Put the manual in the crafting grid to get the manual back (update the manual)
			{"type":"crafting_shapeless","result_count":1,"group":"manual","category":"misc","ingredients": [ingr_repr("manual", namespace)]},
		],
	}
	
	# Add item categories to the remaining items (should select 'shazinho' and 'super_stone')
	for item in database.values():
		if not item.get("category"):
			item["category"] = "misc"

	# Final adjustments, you definitively should keep them!
	deterministic_custom_model_data(config, database, STARTING_CMD, black_list = ["item_names","you_don't_want","in_that","list"])
	add_item_name_and_lore_if_missing(config, database)
	add_private_custom_data_for_namespace(config, database)		# Add a custom namespace for easy item detection
	add_smithed_ignore_vanilla_behaviours_convention(database)	# Smithed items convention
	print()

	# Return database
	return database

