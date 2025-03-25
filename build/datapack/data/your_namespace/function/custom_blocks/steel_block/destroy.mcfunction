
#> your_namespace:custom_blocks/steel_block/destroy
#
# @within	your_namespace:custom_blocks/_groups/minecraft_iron_block
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:iron_block"}},distance=..1] run function your_namespace:custom_blocks/steel_block/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks your_namespace.data 1
scoreboard players remove #total_vanilla_iron_block your_namespace.data 1
scoreboard players remove #total_steel_block your_namespace.data 1

# Kill the custom block entity
kill @s

