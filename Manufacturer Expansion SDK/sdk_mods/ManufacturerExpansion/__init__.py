import unrealsdk

from pathlib import Path
from unrealsdk.hooks import Type
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc 
from mods_base.options import BaseOption, BoolOption
from mods_base import SETTINGS_DIR
from mods_base import build_mod
from unrealsdk import logging
import os

bPatched = False
bPatched_volatile = False
Count = 0
current_obj = None

struct = unrealsdk.make_struct


def obj (definition:str, object:str):
    global current_obj
    unrealsdk.load_package(object)
    unrealsdk.find_object(definition, object).ObjectFlags |= 0x4000
    current_obj = unrealsdk.find_object(definition, object)
    return unrealsdk.find_object(definition, object)

# Gets applied when a game starts
def patch():
    # Enabling the KeepAlive flag so the object stay in memory when using the Startup file for mods

    obj("ItemPartListDefinition","gd_CommandDecks.Body_Brick.BodyParts_Brick").ObjectFlags |= 0x4000
    obj("ItemPartDefinition", "gd_corazza.coms.Body_Brick.Brick_Brute").ObjectFlags |= 0x4000
    obj("ItemPartDefinition", "gd_corazza.coms.Body_Brick.Brick_Rocketeer").ObjectFlags |= 0x4000
    obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza").ObjectFlags |= 0x4000
    obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris").ObjectFlags |= 0x4000
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Lilith.BodyParts_Lilith").ObjectFlags |= 0x4000
    obj("ItemPartDefinition", "gd_corazza.coms.Body_Lilith.Lilith_Stinger").ObjectFlags |= 0x4000
    obj("ItemPartDefinition", "gd_corazza.coms.Body_Lilith.Lilith_StormBringer").ObjectFlags |= 0x4000
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Mordecai.BodyParts_Mordecai").ObjectFlags |= 0x4000
    obj("ItemPartDefinition", "gd_corazza.coms.Body_Mordecai.Mordecai_EagleEye").ObjectFlags |= 0x4000
    obj("ItemPartDefinition", "gd_corazza.coms.Body_Mordecai.Mordecai_Predator").ObjectFlags |= 0x4000
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Roland.BodyParts_Roland").ObjectFlags |= 0x4000
    obj("ItemPartDefinition", "gd_corazza.coms.Body_Roland.Roland_DevilDog").ObjectFlags |= 0x4000
    obj("ItemPartDefinition", "gd_corazza.coms.Body_Roland.Roland_Grenadier").ObjectFlags |= 0x4000
    obj("ItemPartListDefinition","dlc3_gd_CommandDecks.Body_Loyalty.BodyParts_Lilith").ObjectFlags |= 0x4000
    obj("ItemPartListDefinition","dlc3_gd_CommandDecks.Body_Loyalty.BodyParts_Roland").ObjectFlags |= 0x4000
    obj("ItemPartDefinition", "gd_corazza.coms.Body_Roland.Roland_Pioneer_Corazza_Loyalty").ObjectFlags |= 0x4000
    obj("ItemPartDefinition", "gd_corazza.coms.Body_Lilith.Lilith_Starlight_Polaris_Loyalty").ObjectFlags |= 0x4000
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_ComDeck_Brick").ObjectFlags |= 0x4000
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_ComDeck_Lilith").ObjectFlags |= 0x4000
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_ComDeck_Mordecai").ObjectFlags |= 0x4000
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_ComDeck_Roland").ObjectFlags |= 0x4000
    obj("ItemPartDefinition","gd_polaris.Materials.coms.Material_Polaris_1").ObjectFlags |= 0x4000
    obj("ItemPartDefinition","gd_polaris.Materials.coms.Material_Polaris_2").ObjectFlags |= 0x4000
    obj("ItemPartDefinition","gd_polaris.Materials.coms.Material_Polaris_3").ObjectFlags |= 0x4000
    obj("ItemPartDefinition","gd_corazza.Materials.coms.Material_Corazza_1").ObjectFlags |= 0x4000
    obj("ItemPartDefinition","gd_corazza.Materials.coms.Material_Corazza_2").ObjectFlags |= 0x4000
    obj("ItemPartDefinition","gd_corazza.Materials.coms.Material_Corazza_3").ObjectFlags |= 0x4000



    # Class Mods

        # Brick
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Brick.BodyParts_Brick").WeightedParts.append(current_obj.WeightedParts[6])
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Brick.BodyParts_Brick").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_corazza.coms.Body_Brick.Brick_Brute")
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Brick.BodyParts_Brick").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Brick.BodyParts_Brick").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("ItemPartListDefinition","gd_CommandDecks.Body_Brick.BodyParts_Brick").WeightedParts.append(current_obj.WeightedParts[6])
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Brick.BodyParts_Brick").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_corazza.coms.Body_Brick.Brick_Rocketeer")
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Brick.BodyParts_Brick").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Brick.BodyParts_Brick").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_ComDeck_Brick").Manufacturers.append(current_obj.Manufacturers[4])
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_ComDeck_Brick").Manufacturers[len(current_obj.Manufacturers) - 1].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_ComDeck_Brick").Manufacturers.append(current_obj.Manufacturers[1])
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_ComDeck_Brick").Manufacturers[len(current_obj.Manufacturers) - 1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts.append(current_obj.WeightedParts[30])

    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Part = obj("ItemPartDefinition","gd_polaris.Materials.coms.Material_Polaris_1")
    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition","gd_polaris.Manufacturers.Polaris")

    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts.append(current_obj.WeightedParts[31])

    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Part = obj("ItemPartDefinition","gd_polaris.Materials.coms.Material_Polaris_2")
    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition","gd_polaris.Manufacturers.Polaris")

    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts.append(current_obj.WeightedParts[32])

    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Part = obj("ItemPartDefinition","gd_polaris.Materials.coms.Material_Polaris_3")
    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition","gd_polaris.Manufacturers.Polaris")

    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts.append(current_obj.WeightedParts[30])

    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Part = obj("ItemPartDefinition","gd_corazza.Materials.coms.Material_Corazza_1")
    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition","gd_corazza.Manufacturers.Corazza")

    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts.append(current_obj.WeightedParts[31])

    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Part = obj("ItemPartDefinition","gd_corazza.Materials.coms.Material_Corazza_2")
    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition","gd_corazza.Manufacturers.Corazza")

    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts.append(current_obj.WeightedParts[32])

    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Part = obj("ItemPartDefinition","gd_corazza.Materials.coms.Material_Corazza_3")
    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition","gd_corazza.Manufacturers.Corazza")



        # Lilith
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Lilith.BodyParts_Lilith").WeightedParts.append(current_obj.WeightedParts[6])
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Lilith.BodyParts_Lilith").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_corazza.coms.Body_Lilith.Lilith_Stinger")
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Lilith.BodyParts_Lilith").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Lilith.BodyParts_Lilith").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("ItemPartListDefinition","gd_CommandDecks.Body_Lilith.BodyParts_Lilith").WeightedParts.append(current_obj.WeightedParts[6])
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Lilith.BodyParts_Lilith").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_corazza.coms.Body_Lilith.Lilith_StormBringer")
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Lilith.BodyParts_Lilith").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Lilith.BodyParts_Lilith").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("ItemPartListDefinition","dlc3_gd_CommandDecks.Body_Loyalty.BodyParts_Lilith").WeightedParts.append(current_obj.WeightedParts[2])
    obj("ItemPartListDefinition","dlc3_gd_CommandDecks.Body_Loyalty.BodyParts_Lilith").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_corazza.coms.Body_Lilith.Lilith_Starlight_Polaris_Loyalty")
    obj("ItemPartListDefinition","dlc3_gd_CommandDecks.Body_Loyalty.BodyParts_Lilith").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_ComDeck_Lilith").Manufacturers.append(current_obj.Manufacturers[4])
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_ComDeck_Lilith").Manufacturers[len(current_obj.Manufacturers) - 1].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_ComDeck_Lilith").Manufacturers.append(current_obj.Manufacturers[1])
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_ComDeck_Lilith").Manufacturers[len(current_obj.Manufacturers) - 1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

        # Mordecai
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Mordecai.BodyParts_Mordecai").WeightedParts.append(current_obj.WeightedParts[6])
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Mordecai.BodyParts_Mordecai").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_corazza.coms.Body_Mordecai.Mordecai_EagleEye")
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Mordecai.BodyParts_Mordecai").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Mordecai.BodyParts_Mordecai").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("ItemPartListDefinition","gd_CommandDecks.Body_Mordecai.BodyParts_Mordecai").WeightedParts.append(current_obj.WeightedParts[6])
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Mordecai.BodyParts_Mordecai").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_corazza.coms.Body_Mordecai.Mordecai_Predator")
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Mordecai.BodyParts_Mordecai").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Mordecai.BodyParts_Mordecai").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_ComDeck_Mordecai").Manufacturers.append(current_obj.Manufacturers[4])
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_ComDeck_Mordecai").Manufacturers[len(current_obj.Manufacturers) - 1].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_ComDeck_Mordecai").Manufacturers.append(current_obj.Manufacturers[1])
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_ComDeck_Mordecai").Manufacturers[len(current_obj.Manufacturers) - 1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

        # Roland
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Roland.BodyParts_Roland").WeightedParts.append(current_obj.WeightedParts[6])
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Roland.BodyParts_Roland").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_corazza.coms.Body_Roland.Roland_Grenadier")
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Roland.BodyParts_Roland").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Roland.BodyParts_Roland").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("ItemPartListDefinition","gd_CommandDecks.Body_Roland.BodyParts_Roland").WeightedParts.append(current_obj.WeightedParts[6])
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Roland.BodyParts_Roland").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_corazza.coms.Body_Roland.Roland_DevilDog")
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Roland.BodyParts_Roland").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")
    obj("ItemPartListDefinition","gd_CommandDecks.Body_Roland.BodyParts_Roland").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("ItemPartListDefinition","dlc3_gd_CommandDecks.Body_Loyalty.BodyParts_Roland").WeightedParts.append(current_obj.WeightedParts[2])
    obj("ItemPartListDefinition","dlc3_gd_CommandDecks.Body_Loyalty.BodyParts_Roland").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_corazza.coms.Body_Roland.Roland_Pioneer_Corazza_Loyalty")
    obj("ItemPartListDefinition","dlc3_gd_CommandDecks.Body_Loyalty.BodyParts_Roland").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")

    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_ComDeck_Roland").Manufacturers.append(current_obj.Manufacturers[4])
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_ComDeck_Roland").Manufacturers[len(current_obj.Manufacturers) - 1].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_ComDeck_Roland").Manufacturers.append(current_obj.Manufacturers[1])
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_ComDeck_Roland").Manufacturers[len(current_obj.Manufacturers) - 1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    # KeepAlive

    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").ObjectFlags |= 0x4000
    obj("ItemPartDefinition", "gd_corazza.ManufacturerMaterials.Material_Corazza_2").ObjectFlags |= 0x4000
    obj("ItemPartDefinition", "gd_corazza.ManufacturerMaterials.Material_Corazza_3").ObjectFlags |= 0x4000
    obj("ItemPartDefinition", "gd_polaris.ShieldMaterials.Material_Polaris_2").ObjectFlags |= 0x4000
    obj("ItemPartDefinition", "gd_polaris.ShieldMaterials.Material_Polaris_3").ObjectFlags |= 0x4000
    obj("ItemPartDefinition", "gd_corazza.ManufacturerMaterials.Material_Corazza_1").ObjectFlags |= 0x4000
    obj("ItemPartDefinition", "gd_polaris.ShieldMaterials.Material_Polaris_1").ObjectFlags |= 0x4000
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").ObjectFlags |= 0x4000
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Corrosive_large").ObjectFlags |= 0x4000
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Corrosive_medium").ObjectFlags |= 0x4000
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Corrosive_small").ObjectFlags |= 0x4000
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Incendiary_large").ObjectFlags |= 0x4000
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Incendiary_medium").ObjectFlags |= 0x4000
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Incendiary_small").ObjectFlags |= 0x4000
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Shock_large").ObjectFlags |= 0x4000
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Shock_medium").ObjectFlags |= 0x4000
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Shock_small").ObjectFlags |= 0x4000

    # Shields
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Corrosive_large").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.BaseValueAttribute = obj("ResourcePoolAttributeDefinition","d_attributes.ShieldResourcePool.ShieldMaxValue")
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Corrosive_large").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.InitializationDefinition = obj("AttributeInitializationDefinition","gd_Balance_HealthAndDamage.HealthAndDamage.ShieldDamageFormula")
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Corrosive_large").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.BaseValueScaleConstant = 0.75

    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Corrosive_medium").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.BaseValueAttribute = obj("ResourcePoolAttributeDefinition","d_attributes.ShieldResourcePool.ShieldMaxValue")
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Corrosive_medium").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.InitializationDefinition = obj("AttributeInitializationDefinition","gd_Balance_HealthAndDamage.HealthAndDamage.ShieldDamageFormula")
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Corrosive_medium").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.BaseValueScaleConstant = 0.5


    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Corrosive_small").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.BaseValueAttribute = obj("ResourcePoolAttributeDefinition","d_attributes.ShieldResourcePool.ShieldMaxValue")
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Corrosive_small").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.InitializationDefinition = obj("AttributeInitializationDefinition","gd_Balance_HealthAndDamage.HealthAndDamage.ShieldDamageFormula")
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Corrosive_small").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.BaseValueScaleConstant = 0.25


    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Incendiary_large").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.BaseValueAttribute = obj("ResourcePoolAttributeDefinition","d_attributes.ShieldResourcePool.ShieldMaxValue")
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Incendiary_large").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.InitializationDefinition = obj("AttributeInitializationDefinition","gd_Balance_HealthAndDamage.HealthAndDamage.ShieldDamageFormula")
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Incendiary_large").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.BaseValueScaleConstant = 0.75


    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Incendiary_medium").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.BaseValueAttribute = obj("ResourcePoolAttributeDefinition","d_attributes.ShieldResourcePool.ShieldMaxValue")
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Incendiary_medium").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.InitializationDefinition = obj("AttributeInitializationDefinition","gd_Balance_HealthAndDamage.HealthAndDamage.ShieldDamageFormula")
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Incendiary_medium").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.BaseValueScaleConstant = 0.5


    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Incendiary_small").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.BaseValueAttribute = obj("ResourcePoolAttributeDefinition","d_attributes.ShieldResourcePool.ShieldMaxValue")
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Incendiary_small").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.InitializationDefinition = obj("AttributeInitializationDefinition","gd_Balance_HealthAndDamage.HealthAndDamage.ShieldDamageFormula")
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Incendiary_small").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.BaseValueScaleConstant = 0.25


    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Shock_large").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.BaseValueAttribute = obj("ResourcePoolAttributeDefinition","d_attributes.ShieldResourcePool.ShieldMaxValue")
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Shock_large").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.InitializationDefinition = obj("AttributeInitializationDefinition","gd_Balance_HealthAndDamage.HealthAndDamage.ShieldDamageFormula")
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Shock_large").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.BaseValueScaleConstant = 0.75


    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Shock_medium").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.BaseValueAttribute = obj("ResourcePoolAttributeDefinition","d_attributes.ShieldResourcePool.ShieldMaxValue")
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Shock_medium").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.InitializationDefinition = obj("AttributeInitializationDefinition","gd_Balance_HealthAndDamage.HealthAndDamage.ShieldDamageFormula")
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Shock_medium").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.BaseValueScaleConstant = 0.5

    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Shock_small").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.BaseValueAttribute = obj("ResourcePoolAttributeDefinition","d_attributes.ShieldResourcePool.ShieldMaxValue")
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Shock_small").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.InitializationDefinition = obj("AttributeInitializationDefinition","gd_Balance_HealthAndDamage.HealthAndDamage.ShieldDamageFormula")
    obj("SkillDefinition","gd_shields.Skills.Skill_Nova_Shock_small").Behaviors.DamagedEvents[0].Behaviors[0].DamageFormula.BaseValueScaleConstant = 0.25


    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers.append(current_obj.Manufacturers[4])
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[0].GradeModifiers.ExpLevel = 17
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[0].GameStageRequirement.MinGameStage = 15
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[0].GameStageRequirement.MaxGameStage = 19
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[1].GradeModifiers.ExpLevel = 22
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[1].GameStageRequirement.MinGameStage = 20
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[1].GameStageRequirement.MaxGameStage = 24
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[2].GradeModifiers.ExpLevel = 27
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[2].GameStageRequirement.MinGameStage = 25
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[2].GameStageRequirement.MaxGameStage = 39
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[3].GradeModifiers.ExpLevel = 32
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[3].GameStageRequirement.MinGameStage = 30
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[3].GameStageRequirement.MaxGameStage = 49
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[4].GradeModifiers.ExpLevel = 50
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[4].GameStageRequirement.MinGameStage = 50
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[4].GameStageRequirement.MaxGameStage = 100
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades.pop(5)




    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers.append(current_obj.Manufacturers[1])
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[0].GradeModifiers.ExpLevel = 24
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[0].GameStageRequirement.MinGameStage = 22
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[0].GameStageRequirement.MaxGameStage = 30
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[1].GradeModifiers.ExpLevel = 33
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[1].GameStageRequirement.MinGameStage = 31
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[1].GameStageRequirement.MaxGameStage = 39
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[2].GradeModifiers.ExpLevel = 42
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[2].GameStageRequirement.MinGameStage = 40
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[2].GameStageRequirement.MaxGameStage = 49
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[3].GradeModifiers.ExpLevel = 50
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[3].GameStageRequirement.MinGameStage = 50
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades[3].GameStageRequirement.MaxGameStage = 100
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades.pop(5)
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_Shield").Manufacturers[len(current_obj.Manufacturers) - 1].Grades.pop(4)


        # Reward
    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[18])
    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_corazza.ManufacturerMaterials.Material_Corazza_2")
    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")
    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].MinGameStage.BaseValueAttribute = obj("AttributeDefinition", "gd_Balance.MinSpawnLevels.MinLevel_Tech_Explosive")
    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].MinGameStage.BaseValueConstant = 0

    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[19])
    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_corazza.ManufacturerMaterials.Material_Corazza_3")
    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")
    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].MinGameStage.BaseValueAttribute = obj("AttributeDefinition", "gd_Balance.MinSpawnLevels.MinLevel_Tech_Explosive")
    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].MinGameStage.BaseValueConstant = 0

    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[18])
    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_polaris.ShieldMaterials.Material_Polaris_2")
    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")
    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].MinGameStage.BaseValueAttribute = obj("AttributeDefinition", "gd_Balance.MinSpawnLevels.MinLevel_Tech_Explosive")
    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].MinGameStage.BaseValueConstant = 0

    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[19])
    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_polaris.ShieldMaterials.Material_Polaris_3")
    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")
    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].MinGameStage.BaseValueAttribute = obj("AttributeDefinition", "gd_Balance.MinSpawnLevels.MinLevel_Tech_Explosive")
    obj("ItemPartListCollectionDefinition","gd_customitems.PartCollections.PartCollection_reward_shield").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].MinGameStage.BaseValueConstant = 0



    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts.append(current_obj.WeightedParts[27])
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_corazza.ManufacturerMaterials.Material_Corazza_1")
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].MinGameStage.BaseValueAttribute = obj("AttributeDefinition", "gd_Balance.MinSpawnLevels.MinLevel_Tech_Explosive")
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].MinGameStage.BaseValueConstant = 0

    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts.append(current_obj.WeightedParts[28])
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_corazza.ManufacturerMaterials.Material_Corazza_2")
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].MinGameStage.BaseValueAttribute = obj("AttributeDefinition", "gd_Balance.MinSpawnLevels.MinLevel_Tech_Explosive")
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].MinGameStage.BaseValueConstant = 0

    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts.append(current_obj.WeightedParts[29])
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_corazza.ManufacturerMaterials.Material_Corazza_3")
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].MinGameStage.BaseValueAttribute = obj("AttributeDefinition", "gd_Balance.MinSpawnLevels.MinLevel_Tech_Explosive")
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].MinGameStage.BaseValueConstant = 0

    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts.append(current_obj.WeightedParts[27])
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_polaris.ShieldMaterials.Material_Polaris_1")
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].MinGameStage.BaseValueAttribute = obj("AttributeDefinition", "gd_Balance.MinSpawnLevels.MinLevel_Tech_Explosive")
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].MinGameStage.BaseValueConstant = 0

    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts.append(current_obj.WeightedParts[28])
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_polaris.ShieldMaterials.Material_Polaris_2")
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].MinGameStage.BaseValueAttribute = obj("AttributeDefinition", "gd_Balance.MinSpawnLevels.MinLevel_Tech_Explosive")
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].MinGameStage.BaseValueConstant = 0

    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts.append(current_obj.WeightedParts[29])
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_polaris.ShieldMaterials.Material_Polaris_3")
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].MinGameStage.BaseValueAttribute = obj("AttributeDefinition", "gd_Balance.MinSpawnLevels.MinLevel_Tech_Explosive")
    obj("ItemPartListDefinition","gd_shields.MaterialPartsLists.OrbShieldMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].MinGameStage.BaseValueConstant = 0

    # KeepAlive

    obj("ItemPartListDefinition","gd_tunercuffs.MaterialPartsLists.GrenadeModulatorMaterialPartList").ObjectFlags |= 0x4000
    obj("ItemPartDefinition", "gd_corazza.Homing.Material_Corazza_1").ObjectFlags |= 0x4000
    obj("ItemPartDefinition", "gd_polaris.Singularity.Material_Polaris_1").ObjectFlags |= 0x4000
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_GrenadeMODs").ObjectFlags |= 0x4000


    # Grenade Mods

    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_GrenadeMODs").Manufacturers.append(current_obj.Manufacturers[4])
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_GrenadeMODs").Manufacturers[len(current_obj.Manufacturers) - 1].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_GrenadeMODs").Manufacturers.append(current_obj.Manufacturers[1])
    obj("InventoryBalanceDefinition", "gd_itemgrades.Gear.ItemGrade_Gear_GrenadeMODs").Manufacturers[len(current_obj.Manufacturers) - 1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("ItemPartListDefinition","gd_tunercuffs.MaterialPartsLists.GrenadeModulatorMaterialPartList").WeightedParts.append(current_obj.WeightedParts[9])
    obj("ItemPartListDefinition","gd_tunercuffs.MaterialPartsLists.GrenadeModulatorMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_corazza.Homing.Material_Corazza_1")
    obj("ItemPartListDefinition","gd_tunercuffs.MaterialPartsLists.GrenadeModulatorMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_corazza.Manufacturers.Corazza")

    obj("ItemPartListDefinition","gd_tunercuffs.MaterialPartsLists.GrenadeModulatorMaterialPartList").WeightedParts.append(current_obj.WeightedParts[9])
    obj("ItemPartListDefinition","gd_tunercuffs.MaterialPartsLists.GrenadeModulatorMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("ItemPartDefinition", "gd_polaris.Singularity.Material_Polaris_1")
    obj("ItemPartListDefinition","gd_tunercuffs.MaterialPartsLists.GrenadeModulatorMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    # KeepAlive

    obj("WeaponPartListDefinition","gd_weap_assault_shotgun.acc.Acc_PartList").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","gd_polaris.Weapons.legendary.acc.acc5_Polaris_RedSpot").ObjectFlags |= 0x4000
    obj("WeaponPartListDefinition","gd_weap_assault_shotgun.Grip.Grip_PartList").ObjectFlags |= 0x4000
    obj("WeaponPartListDefinition","gd_weap_grenade_launcher.Barrel.Barrel_PartList").ObjectFlags |= 0x4000
    obj("WeaponPartListDefinition","gd_weap_grenade_launcher.Grip.Grip_PartList").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","gd_polaris.Weapons.legendary.Barrel.barrel4_Polaris_Supernova").ObjectFlags |= 0x4000
    obj("WeaponPartListDefinition","gd_weap_machine_pistol.acc.Acc_PartList").ObjectFlags |= 0x4000
    obj("WeaponPartListDefinition","gd_weap_machine_pistol.Grip.Grip_PartList").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","gd_polaris.Weapons.legendary.acc.acc5_Corrosive_Venera").ObjectFlags |= 0x4000
    obj("WeaponPartListDefinition","gd_weap_patrol_smg.Barrel.Barrel_PartList").ObjectFlags |= 0x4000
    obj("WeaponPartListDefinition","gd_weap_patrol_smg.Grip.Grip_PartList").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","gd_polaris.Weapons.legendary.Barrel.barrel2_Polaris_AsteroidBelt").ObjectFlags |= 0x4000
    obj("WeaponPartListDefinition","gd_weap_repeater_pistol.acc.Acc_PartList").ObjectFlags |= 0x4000
    obj("WeaponPartListDefinition","gd_weap_repeater_pistol.Grip.Grip_PartList").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","gd_polaris.Weapons.legendary.acc.acc5_Incendiary_Expanse").ObjectFlags |= 0x4000
    obj("WeaponPartListDefinition","gd_weap_sniper_rifle_semiauto.acc.Acc_PartList").ObjectFlags |= 0x4000
    obj("WeaponPartListDefinition","gd_weap_sniper_rifle_semiauto.Grip.Grip_PartList").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","gd_polaris.Weapons.legendary.acc.acc1_Polaris_LightYear").ObjectFlags |= 0x4000




    # Weapon Parts

        # Assault Shotgun
    obj("WeaponPartListDefinition","gd_weap_assault_shotgun.acc.Acc_PartList").WeightedParts.append(current_obj.WeightedParts[10])
    obj("WeaponPartListDefinition","gd_weap_assault_shotgun.acc.Acc_PartList").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("WeaponPartDefinition","gd_polaris.Weapons.legendary.acc.acc5_Polaris_RedSpot")
    obj("WeaponPartListDefinition","gd_weap_assault_shotgun.acc.Acc_PartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListDefinition","gd_weap_assault_shotgun.Grip.Grip_PartList").WeightedParts.append(current_obj.WeightedParts[2])
    obj("WeaponPartListDefinition","gd_weap_assault_shotgun.Grip.Grip_PartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

        # Grenade Launcher
    obj("WeaponPartListDefinition","gd_weap_grenade_launcher.Barrel.Barrel_PartList").WeightedParts.append(current_obj.WeightedParts[10])
    obj("WeaponPartListDefinition","gd_weap_grenade_launcher.Barrel.Barrel_PartList").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("WeaponPartDefinition","gd_polaris.Weapons.legendary.Barrel.barrel4_Polaris_Supernova")
    obj("WeaponPartListDefinition","gd_weap_grenade_launcher.Barrel.Barrel_PartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListDefinition","gd_weap_grenade_launcher.Grip.Grip_PartList").WeightedParts.append(current_obj.WeightedParts[1])
    obj("WeaponPartListDefinition","gd_weap_grenade_launcher.Grip.Grip_PartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

        # Machine Pistol
    obj("WeaponPartListDefinition","gd_weap_machine_pistol.acc.Acc_PartList").WeightedParts.append(current_obj.WeightedParts[10])
    obj("WeaponPartListDefinition","gd_weap_machine_pistol.acc.Acc_PartList").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("WeaponPartDefinition","gd_polaris.Weapons.legendary.acc.acc5_Corrosive_Venera")
    obj("WeaponPartListDefinition","gd_weap_machine_pistol.acc.Acc_PartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListDefinition","gd_weap_machine_pistol.Grip.Grip_PartList").WeightedParts.append(current_obj.WeightedParts[0])
    obj("WeaponPartListDefinition","gd_weap_machine_pistol.Grip.Grip_PartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

        # SMG
    obj("WeaponPartListDefinition","gd_weap_patrol_smg.Barrel.Barrel_PartList").WeightedParts.append(current_obj.WeightedParts[7])
    obj("WeaponPartListDefinition","gd_weap_patrol_smg.Barrel.Barrel_PartList").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("WeaponPartDefinition","gd_polaris.Weapons.legendary.Barrel.barrel2_Polaris_AsteroidBelt")
    obj("WeaponPartListDefinition","gd_weap_patrol_smg.Barrel.Barrel_PartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListDefinition","gd_weap_patrol_smg.Grip.Grip_PartList").WeightedParts.append(current_obj.WeightedParts[3])
    obj("WeaponPartListDefinition","gd_weap_patrol_smg.Grip.Grip_PartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

        # Repeater Pistol
    obj("WeaponPartListDefinition","gd_weap_repeater_pistol.acc.Acc_PartList").WeightedParts.append(current_obj.WeightedParts[13])
    obj("WeaponPartListDefinition","gd_weap_repeater_pistol.acc.Acc_PartList").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("WeaponPartDefinition","gd_polaris.Weapons.legendary.acc.acc5_Incendiary_Expanse")
    obj("WeaponPartListDefinition","gd_weap_repeater_pistol.acc.Acc_PartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListDefinition","gd_weap_repeater_pistol.Grip.Grip_PartList").WeightedParts.append(current_obj.WeightedParts[2])
    obj("WeaponPartListDefinition","gd_weap_repeater_pistol.Grip.Grip_PartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

        # Semi-Auto Sniper Rifle
    obj("WeaponPartListDefinition","gd_weap_sniper_rifle_semiauto.acc.Acc_PartList").WeightedParts.append(current_obj.WeightedParts[9])
    obj("WeaponPartListDefinition","gd_weap_sniper_rifle_semiauto.acc.Acc_PartList").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("WeaponPartDefinition","gd_polaris.Weapons.legendary.acc.acc1_Polaris_LightYear")
    obj("WeaponPartListDefinition","gd_weap_sniper_rifle_semiauto.acc.Acc_PartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListDefinition","gd_weap_sniper_rifle_semiauto.Grip.Grip_PartList").WeightedParts.append(current_obj.WeightedParts[0])
    obj("WeaponPartListDefinition","gd_weap_sniper_rifle_semiauto.Grip.Grip_PartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")


    # KeepAlive

    obj("WeaponPartListDefinition","gd_weap_shared_materialparts.MaterialPartsLists.SharedMaterialPartList").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_1").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_2").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_3").ObjectFlags |= 0x4000
    obj("WeaponPartListDefinition","gd_weap_shared_materialparts.MaterialPartsLists.SharedMaterialPartList_Reward").ObjectFlags |= 0x4000
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_AssaultShotgun").ObjectFlags |= 0x4000
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_CombatRifle").ObjectFlags |= 0x4000
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_CombatShotgun").ObjectFlags |= 0x4000
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_Launcher_Rocket").ObjectFlags |= 0x4000
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_MachinePistol").ObjectFlags |= 0x4000
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_PatrolSMG").ObjectFlags |= 0x4000
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_RepeaterPistol").ObjectFlags |= 0x4000
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_RevolverPistol").ObjectFlags |= 0x4000
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SemiAutoSniperRifle").ObjectFlags |= 0x4000
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SniperRifle").ObjectFlags |= 0x4000
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SupportMachineGun").ObjectFlags |= 0x4000
    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_AssaultShotgun").ObjectFlags |= 0x4000
    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_CombatRifle").ObjectFlags |= 0x4000
    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_CombatShotgun").ObjectFlags |= 0x4000
    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_Launcher_Rocket").ObjectFlags |= 0x4000
    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_MachinePistol").ObjectFlags |= 0x4000
    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_PatrolSMG").ObjectFlags |= 0x4000
    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_RepeaterPistol").ObjectFlags |= 0x4000
    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_RevolverPistol").ObjectFlags |= 0x4000
    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_SemiAutoSniperRifle").ObjectFlags |= 0x4000
    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_SniperRifle").ObjectFlags |= 0x4000
    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_SupportMachineGun").ObjectFlags |= 0x4000


    # Weapon Material And Manufacturers

    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_AssaultShotgun").Manufacturers.append(current_obj.Manufacturers[3])
    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_AssaultShotgun").Manufacturers[len(current_obj.Manufacturers) - 1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_Launcher_Grenade").Manufacturers.append(current_obj.Manufacturers[1])
    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_Launcher_Grenade").Manufacturers[len(current_obj.Manufacturers) - 1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_MachinePistol").Manufacturers.append(current_obj.Manufacturers[2])
    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_MachinePistol").Manufacturers[len(current_obj.Manufacturers) - 1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_PatrolSMG").Manufacturers.append(current_obj.Manufacturers[3])
    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_PatrolSMG").Manufacturers[len(current_obj.Manufacturers) - 1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_RepeaterPistol").Manufacturers.append(current_obj.Manufacturers[6])
    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_RepeaterPistol").Manufacturers[len(current_obj.Manufacturers) - 1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_SemiAutoSniperRifle").Manufacturers.append(current_obj.Manufacturers[2])
    obj("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_SemiAutoSniperRifle").Manufacturers[len(current_obj.Manufacturers) - 1].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

        # Shared Material
    obj("WeaponPartListDefinition","gd_weap_shared_materialparts.MaterialPartsLists.SharedMaterialPartList").WeightedParts.append(current_obj.WeightedParts[28])
    obj("WeaponPartListDefinition","gd_weap_shared_materialparts.MaterialPartsLists.SharedMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_1")
    obj("WeaponPartListDefinition","gd_weap_shared_materialparts.MaterialPartsLists.SharedMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListDefinition","gd_weap_shared_materialparts.MaterialPartsLists.SharedMaterialPartList").WeightedParts.append(current_obj.WeightedParts[29])
    obj("WeaponPartListDefinition","gd_weap_shared_materialparts.MaterialPartsLists.SharedMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_2")
    obj("WeaponPartListDefinition","gd_weap_shared_materialparts.MaterialPartsLists.SharedMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListDefinition","gd_weap_shared_materialparts.MaterialPartsLists.SharedMaterialPartList").WeightedParts.append(current_obj.WeightedParts[30])
    obj("WeaponPartListDefinition","gd_weap_shared_materialparts.MaterialPartsLists.SharedMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_3")
    obj("WeaponPartListDefinition","gd_weap_shared_materialparts.MaterialPartsLists.SharedMaterialPartList").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListDefinition","gd_weap_shared_materialparts.MaterialPartsLists.SharedMaterialPartList_Reward").WeightedParts.append(current_obj.WeightedParts[28])
    obj("WeaponPartListDefinition","gd_weap_shared_materialparts.MaterialPartsLists.SharedMaterialPartList_Reward").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_1")
    obj("WeaponPartListDefinition","gd_weap_shared_materialparts.MaterialPartsLists.SharedMaterialPartList_Reward").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListDefinition","gd_weap_shared_materialparts.MaterialPartsLists.SharedMaterialPartList_Reward").WeightedParts.append(current_obj.WeightedParts[29])
    obj("WeaponPartListDefinition","gd_weap_shared_materialparts.MaterialPartsLists.SharedMaterialPartList_Reward").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_2")
    obj("WeaponPartListDefinition","gd_weap_shared_materialparts.MaterialPartsLists.SharedMaterialPartList_Reward").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListDefinition","gd_weap_shared_materialparts.MaterialPartsLists.SharedMaterialPartList_Reward").WeightedParts.append(current_obj.WeightedParts[30])
    obj("WeaponPartListDefinition","gd_weap_shared_materialparts.MaterialPartsLists.SharedMaterialPartList_Reward").WeightedParts[len(current_obj.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_3")
    obj("WeaponPartListDefinition","gd_weap_shared_materialparts.MaterialPartsLists.SharedMaterialPartList_Reward").WeightedParts[len(current_obj.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

        # Assault Shotgun Reward Material
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_AssaultShotgun").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[19])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_AssaultShotgun").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_2")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_AssaultShotgun").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_AssaultShotgun").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[20])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_AssaultShotgun").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_3")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_AssaultShotgun").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

        # Combat Rifle Reward Material
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_CombatRifle").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[19])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_CombatRifle").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_2")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_CombatRifle").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_CombatRifle").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[20])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_CombatRifle").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_3")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_CombatRifle").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

        # Combat Shotgun Reward Material
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_CombatShotgun").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[19])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_CombatShotgun").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_2")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_CombatShotgun").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_CombatShotgun").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[20])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_CombatShotgun").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_3")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_CombatShotgun").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

        # Rocket Launcher Reward Material
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_Launcher_Rocket").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[19])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_Launcher_Rocket").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_2")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_Launcher_Rocket").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_Launcher_Rocket").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[20])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_Launcher_Rocket").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_3")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_Launcher_Rocket").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

        # Machine Pistol Reward Material
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_MachinePistol").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[19])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_MachinePistol").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_2")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_MachinePistol").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_MachinePistol").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[20])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_MachinePistol").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_3")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_MachinePistol").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

        # SMG Reward Material
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_PatrolSMG").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[19])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_PatrolSMG").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_2")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_PatrolSMG").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_PatrolSMG").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[20])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_PatrolSMG").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_3")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_PatrolSMG").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

        # Repeater Pistol Reward Material
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_RepeaterPistol").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[19])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_RepeaterPistol").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_2")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_RepeaterPistol").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_RepeaterPistol").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[20])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_RepeaterPistol").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_3")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_RepeaterPistol").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

        # Revolver Pistol Reward Material
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_RevolverPistol").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[19])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_RevolverPistol").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_2")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_RevolverPistol").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_RevolverPistol").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[20])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_RevolverPistol").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_3")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_RevolverPistol").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

        # Semi-Auto Sniper Rifle Reward Material
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SemiAutoSniperRifle").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[19])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SemiAutoSniperRifle").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_2")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SemiAutoSniperRifle").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SemiAutoSniperRifle").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[20])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SemiAutoSniperRifle").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_3")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SemiAutoSniperRifle").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

        # Sniper Rifle Reward Material
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SniperRifle").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[19])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SniperRifle").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_2")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SniperRifle").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SniperRifle").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[20])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SniperRifle").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_3")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SniperRifle").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

        # Support Machinegun Reward Material
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SupportMachineGun").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[19])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SupportMachineGun").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_2")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SupportMachineGun").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")

    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SupportMachineGun").MaterialPartData.WeightedParts.append(current_obj.MaterialPartData.WeightedParts[20])
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SupportMachineGun").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Part = obj("WeaponPartDefinition", "gd_polaris.WeaponMaterials.Material_Polaris_3")
    obj("WeaponPartListCollectionDefinition","gd_customweapons.Reward_PartCollections.PartCollection_reward_SupportMachineGun").MaterialPartData.WeightedParts[len(current_obj.MaterialPartData.WeightedParts) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition", "gd_polaris.Manufacturers.Polaris")


# Gets reapplied at every level transistion
def patch_volatile():
    # ItemPools

        # Fortress
    obj("ItemPoolDefinition", "dlc3_gd_itempools.Pearlescent.dlc3_Pool_UniqueShields").BalancedItems.append(struct("BalancedInventoryData", ItmPoolDefinition=None, InvBalanceDefinition=obj("InventoryBalanceDefinition", "dlc3_gd_corazza.Items.CustomItem_Shield_Corazza_Fortress"), Probability=struct("AttributeInitializationData",BaseValueConstant=1.0000000,BaseValueAttribute=None,InitializationDefinition=obj("AttributeInitializationDefinition","gd_Balance.Weighting.Weight_1_Common"),BaseValueScaleConstant=1.0000000), bDropOnDeath=True))

        #Callisto
    obj("ItemPoolDefinition", "dlc3_gd_itempools.Bandits.Heavy_Badass_Weapons_enhance").BalancedItems.append(struct("BalancedInventoryData", ItmPoolDefinition=None, InvBalanceDefinition=obj("InventoryBalanceDefinition", "dlc3_gd_polaris.Pearlescent_Weapons.CustomWeap_AssaultShotgun_PolarisElpis"), Probability=struct("AttributeInitializationData",BaseValueConstant=0.0000000,BaseValueAttribute=None,InitializationDefinition=obj("AttributeInitializationDefinition","gd_Balance.Weighting.Weight_5_VeryRare"),BaseValueScaleConstant=0.050000), bDropOnDeath=True))

    obj("ItemPoolDefinition", "dlc3_gd_itempools.Pearlescent.dlc3_Pool_Pearlescent_AllWeapons").BalancedItems.append(struct("BalancedInventoryData", ItmPoolDefinition=None, InvBalanceDefinition=obj("InventoryBalanceDefinition", "dlc3_gd_polaris.Pearlescent_Weapons.CustomWeap_AssaultShotgun_PolarisElpis"), Probability=struct("AttributeInitializationData",BaseValueConstant=0.0000000,BaseValueAttribute=None,InitializationDefinition=obj("AttributeInitializationDefinition","gd_Balance.Weighting.Weight_1_Common"),BaseValueScaleConstant=1.000000), bDropOnDeath=True))

    obj("ItemPoolDefinition", "dlc3_gd_itempools.Pearlescent.dlc3_Pool_Pearlescent_CombatRifles").BalancedItems.append(struct("BalancedInventoryData", ItmPoolDefinition=None, InvBalanceDefinition=obj("InventoryBalanceDefinition", "dlc3_gd_polaris.Pearlescent_Weapons.CustomWeap_AssaultShotgun_PolarisElpis"), Probability=struct("AttributeInitializationData",BaseValueConstant=0.0000000,BaseValueAttribute=None,InitializationDefinition=obj("AttributeInitializationDefinition","gd_Balance.Weighting.Weight_1_Common"),BaseValueScaleConstant=1.000000), bDropOnDeath=True))

    obj("ItemPoolDefinition", "dlc3_gd_itempools.Pearlescent.dlc3_Pool_Pearlescent_LongGuns").BalancedItems.append(struct("BalancedInventoryData", ItmPoolDefinition=None, InvBalanceDefinition=obj("InventoryBalanceDefinition", "dlc3_gd_polaris.Pearlescent_Weapons.CustomWeap_AssaultShotgun_PolarisElpis"), Probability=struct("AttributeInitializationData",BaseValueConstant=0.0000000,BaseValueAttribute=None,InitializationDefinition=obj("AttributeInitializationDefinition","gd_Balance.Weighting.Weight_1_Common"),BaseValueScaleConstant=1.000000), bDropOnDeath=True))

    obj("ItemPoolDefinition", "dlc3_gd_itempools.Treasure_ChestPools.Chest_Weapons_Shotguns_enhance").BalancedItems.append(struct("BalancedInventoryData", ItmPoolDefinition=None, InvBalanceDefinition=obj("InventoryBalanceDefinition", "dlc3_gd_polaris.Pearlescent_Weapons.CustomWeap_AssaultShotgun_PolarisElpis"), Probability=struct("AttributeInitializationData",BaseValueConstant=0.0000000,BaseValueAttribute=None,InitializationDefinition=obj("AttributeInitializationDefinition","gd_Balance.Weighting.Weight_5_VeryRare"),BaseValueScaleConstant=0.200000), bDropOnDeath=True))




@hook(
    hook_func="Engine.WorldInfo:CommitMapChange",
    hook_type=Type.POST,
)
def on_commit_map_change(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global bPatched_volatile
    bPatched_volatile = False

@hook(
    hook_func="Engine.WorldInfo:PostBeginPlay",
    hook_type=Type.POST,
)
def on_level_loaded(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global bPatched_volatile
    global Count
    if Count >= 2:
        Count = 0
        if bPatched_volatile != True:
            bPatched_volatile = True
            #patch_volatile()
    else:
        Count = Count + 1

@hook(
    hook_func="Engine.WorldInfo:IsMenuLevel",
    hook_type=Type.PRE,
)
def on_startgame(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    global bPatched
    if bPatched is False:
        bPatched = True
        patch()
        patch_volatile()






# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]

build_mod(
    # These are defaulted
    # inject_version_from_pyproject=True, # This is True by default
    # version_info_parser=lambda v: tuple(int(x) for x in v.split(".")),
    # deregister_same_settings=True,      # This is True by default
    keybinds=[],
    hooks=[on_level_loaded, on_commit_map_change, on_startgame],
    commands=[],
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/ManufacturerExpansion.json"),
)

logging.info(f"Manufacturer Expansion - Corazza and Polaris SDK Loaded: {__version__}, {__version_info__}")
