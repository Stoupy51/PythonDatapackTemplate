
#> your_namespace:custom_blocks/raw_super_iron_block/replace_item
#
# @within	your_namespace:custom_blocks/raw_super_iron_block/destroy
#

data modify entity @s Item.components set from storage your_namespace:items all.raw_super_iron_block.components
data modify entity @s Item.id set from storage your_namespace:items all.raw_super_iron_block.id

