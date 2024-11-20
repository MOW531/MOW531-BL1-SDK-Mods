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

TEXT_MOD_FOLDER = "./Mods/BadTextModLoader/TextMods/"

setcommands = []
rsetcommands = []
bPatched = False
bPatched_volatile = False
Count = 0
current_obj = None

struct = unrealsdk.make_struct


def obj (definition:str, object:str):
    global current_obj
    unrealsdk.load_package(object)
    current_obj = unrealsdk.find_object(definition, object)
    return unrealsdk.find_object(definition, object)


def patch():
    # Enabling the KeepAlive flag so the object stay in memory when using the Startup file for mods

    obj("WeaponNamePartDefinition","gd_weap_sniper_rifle_semiauto.Title.Title_Damage1_Driver").ObjectFlags |= 0x4000
    obj("WeaponNamePartDefinition","gd_weap_support_machinegun.Title.TitleM_SandS_Draco").ObjectFlags |= 0x4000
    obj("WeaponNamePartDefinition","gd_weap_sniper_rifle_semiauto.Title.TitleM_Dahl1_Penetrator").ObjectFlags |= 0x4000
    obj("WeaponNamePartDefinition","gd_weap_assault_shotgun.Title.TitleM_Maliwan1_Plague").ObjectFlags |= 0x4000
    obj("WeaponNamePartDefinition","gd_weap_sniper_rifle_semiauto.Title.TitleM_Hyperion1_Executioner").ObjectFlags |= 0x4000
    obj("WeaponNamePartDefinition","gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").ObjectFlags |= 0x4000
    obj("WeaponNamePartDefinition","gd_weap_combat_shotgun.Prefix.Prefix_Damage1_Terrible").ObjectFlags |= 0x4000
    obj("WeaponNamePartDefinition","gd_weap_repeater_pistol.Prefix.Prefix_Nasty").ObjectFlags |= 0x4000
    obj("WeaponNamePartDefinition","gd_weap_combat_shotgun.Prefix.Prefix_Acc1_Jagged").ObjectFlags |= 0x4000
    obj("WeaponNamePartDefinition","gd_weap_grenade_launcher.Prefix.Prefix_Acc4_Mad").ObjectFlags |= 0x4000
    obj("WeaponNamePartDefinition","gd_weap_grenade_launcher.Prefix.Prefix_Barrel_Sticky").ObjectFlags |= 0x4000

    # Titles and Prefixes

    obj("WeaponNamePartDefinition","gd_weap_sniper_rifle_semiauto.Title.Title_Damage1_Driver").PartName = "Driver"
    obj("WeaponNamePartDefinition","gd_weap_support_machinegun.Title.TitleM_SandS_Draco").Rarity.BaseValueAttribute = (obj("InventoryAttributeDefinition","gd_Balance_Inventory.Rarity_Weapon.WeaponPartRarity6_Legendary"))
    obj("WeaponNamePartDefinition","gd_weap_sniper_rifle_semiauto.Title.TitleM_Dahl1_Penetrator").Rarity.BaseValueAttribute = (obj("InventoryAttributeDefinition","gd_Balance_Inventory.Rarity_Weapon.WeaponPartRarity6_Legendary"))
    obj("WeaponNamePartDefinition","gd_weap_assault_shotgun.Title.TitleM_Maliwan1_Plague").PartName = "Plague"
    obj("WeaponNamePartDefinition","gd_weap_sniper_rifle_semiauto.Title.TitleM_Hyperion1_Executioner").PartName = "Executioner"
    obj("WeaponNamePartDefinition","gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").Expressions[0].ConstantOperand2 = 0
    obj("WeaponNamePartDefinition","gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").Expressions[(len(current_obj.Expressions)) - 1].AttributeOperand1 = obj("AttributeDefinition","d_attributes.WeaponDamageType.WeaponDamage_Is_Corrosive")
    obj("WeaponNamePartDefinition","gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").Expressions.append(current_obj.Expressions[0])
    obj("WeaponNamePartDefinition","gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").Expressions[(len(current_obj.Expressions)) - 1].AttributeOperand1 = obj("AttributeDefinition","d_attributes.WeaponDamageType.WeaponDamage_Is_Explosive")
    obj("WeaponNamePartDefinition","gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").Expressions.append(current_obj.Expressions[0])
    obj("WeaponNamePartDefinition","gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").Expressions[(len(current_obj.Expressions)) - 1].AttributeOperand1 = obj("AttributeDefinition","d_attributes.WeaponDamageType.WeaponDamage_Is_Incendiary")
    obj("WeaponNamePartDefinition","gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").Expressions.append(current_obj.Expressions[0])
    obj("WeaponNamePartDefinition","gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").Expressions[(len(current_obj.Expressions)) - 1].AttributeOperand1 = obj("AttributeDefinition","d_attributes.WeaponDamageType.WeaponDamage_Is_Shock")
    obj("WeaponNamePartDefinition","gd_weap_combat_shotgun.Prefix.Prefix_Damage1_Terrible").Expressions.append(obj("WeaponNamePartDefinition","gd_weap_repeater_pistol.Prefix.Prefix_Nasty").Expressions[1])
    obj("WeaponNamePartDefinition","gd_weap_combat_shotgun.Prefix.Prefix_Damage1_Terrible").Expressions[(len(current_obj.Expressions)) - 1].AttributeOperand1 = obj("AttributeDefinition","d_attributes.Weapon.WeaponDamageNormalized")
    obj("WeaponNamePartDefinition","gd_weap_combat_shotgun.Prefix.Prefix_Damage1_Terrible").Expressions[(len(current_obj.Expressions)) - 1].ConstantOperand2 = 2
    obj("WeaponNamePartDefinition","gd_weap_repeater_pistol.Prefix.Prefix_Nasty").Expressions[1].AttributeOperand1 = obj("AttributeDefinition","d_attributes.Weapon.WeaponDamageNormalized")
    obj("WeaponNamePartDefinition","gd_weap_combat_shotgun.Prefix.Prefix_Acc1_Jagged").PartName = "Jagged"
    obj("WeaponNamePartDefinition","gd_weap_grenade_launcher.Prefix.Prefix_Acc4_Mad").PartName = "Mad"
    obj("WeaponNamePartDefinition","gd_weap_grenade_launcher.Prefix.Prefix_Acc4_Mad").Priority = 3
    obj("WeaponNamePartDefinition","gd_weap_grenade_launcher.Prefix.Prefix_Barrel_Sticky").PartName = "Sticky"

    # KeepAlive

    obj("WeaponPartDefinition","gd_weap_machine_pistol.UniqueParts.TheClipper_acc5_Incendiary").ObjectFlags |= 0x4000
    obj("WeaponPartListCollectionDefinition","gd_customweapons.PartCollections.PartCollection_SMG_BoneShredder").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","dlc3_gd_weap_UniqueParts.SemiAutoSniper.acc2_KyrosPower").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","gd_weap_support_machinegun.acc.acc4_SandS_Draco_Incendiary").ObjectFlags |= 0x4000
    obj("WeaponPartListDefinition","gd_weap_assault_shotgun.acc.Acc_PartList").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","gd_weap_patrol_smg.Barrel.barrel5_Hyperion_Bitch").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","gd_weap_machine_pistol.Barrel.barrel5_Vladof_Vengence").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","gd_weap_machine_pistol.acc.acc1_Hyperion_Reaper").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","gd_weap_repeater_pistol.acc.acc5_Corrosive").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","gd_weap_repeater_pistol.UniqueParts.TheDove_barrel4").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","gd_weap_rocket_launcher.acc.acc2_Evil").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","gd_weap_assault_shotgun.acc.acc1_Spiked").ObjectFlags |= 0x4000
    obj("WeaponPartListDefinition","gd_weap_grenade_launcher.Barrel.Barrel_PartList").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","gd_weap_grenade_launcher.acc.acc2_Blitz").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","gd_weap_combat_rifle.UniqueParts.Sentinel_sight4").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","gd_weap_combat_rifle.Barrel.barrel5_Hyperion_Destroyer").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","gd_weap_sniper_rifle_semiauto.UniqueParts.ReaversEdge_sight4").ObjectFlags |= 0x4000
    obj("WeaponPartDefinition","dlc3_gd_weap_UniqueParts.RepeaterPistol.barrel5_AthenasWisdom").ObjectFlags |= 0x4000

    # Weapon parts

    obj("WeaponPartDefinition","gd_weap_support_machinegun.acc.acc4_SandS_Draco_Incendiary").TitleList.append(obj("WeaponNamePartDefinition","gd_weap_support_machinegun.Title.TitleM_SandS_Draco"))
    obj("WeaponPartListDefinition","gd_weap_assault_shotgun.acc.Acc_PartList").WeightedParts[7].DefaultWeight.BaseValueScaleConstant = 1
    obj("WeaponPartDefinition","gd_weap_patrol_smg.Barrel.barrel5_Hyperion_Bitch").ExternalAttributeEffects[2].ModifierType = 1
    obj("WeaponPartDefinition","gd_weap_patrol_smg.Barrel.barrel5_Hyperion_Bitch").ExternalAttributeEffects[2].BaseModifierValue.BaseValueConstant = 1.5
    obj("WeaponPartDefinition","gd_weap_machine_pistol.Barrel.barrel5_Vladof_Vengence").ExternalAttributeEffects.append(current_obj.WeaponAttributeEffects[4])
    obj("WeaponPartDefinition","gd_weap_machine_pistol.acc.acc1_Hyperion_Reaper").ExternalAttributeEffects.append(current_obj.WeaponAttributeEffects[0])
    obj("WeaponPartDefinition","gd_weap_repeater_pistol.acc.acc5_Corrosive").TechAbilities[4].RequiredTechLevel = 15
    obj("WeaponPartDefinition","gd_weap_machine_pistol.UniqueParts.TheClipper_acc5_Incendiary").ExternalAttributeEffects.append(current_obj.WeaponAttributeEffects[1])
    obj("WeaponPartDefinition","gd_weap_repeater_pistol.UniqueParts.TheDove_barrel4").WeaponAttributeEffects[0].ModifierType = 0
    obj("WeaponPartDefinition","gd_weap_repeater_pistol.UniqueParts.TheDove_barrel4").WeaponAttributeEffects[0].BaseModifierValue.BaseValueConstant = -10000
    obj("WeaponPartListCollectionDefinition","gd_customweapons.PartCollections.PartCollection_SMG_BoneShredder").MaterialPartData.WeightedParts[0].Part = obj("WeaponPartDefinition","gd_weap_patrol_smg.UniqueParts.BoneShredder_Material")
    obj("WeaponPartDefinition","dlc3_gd_weap_UniqueParts.SemiAutoSniper.acc2_KyrosPower").CustomDamageTypeDefinition = obj("WillowDamageTypeDefinition","gd_Explosive.DamageType.DmgType_Explosive")
    obj("WeaponPartDefinition","gd_weap_rocket_launcher.acc.acc2_Evil").WeaponAttributeEffects.append(current_obj.ExternalAttributeEffects[2])
    obj("WeaponPartDefinition","gd_weap_rocket_launcher.acc.acc2_Evil").WeaponAttributeEffects.append(current_obj.ExternalAttributeEffects[1])
    obj("WeaponPartDefinition","gd_weap_assault_shotgun.acc.acc1_Spiked").ExternalAttributeEffects[0].ModifierType = 1
    obj("WeaponPartListDefinition","gd_weap_grenade_launcher.Barrel.Barrel_PartList").WeightedParts.append(current_obj.WeightedParts[10])
    obj("WeaponPartListDefinition","gd_weap_grenade_launcher.Barrel.Barrel_PartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Part = obj("WeaponPartDefinition","gd_weap_grenade_launcher.Barrel.barrel3_Dahl_Onslaught")
    obj("WeaponPartListDefinition","gd_weap_grenade_launcher.Barrel.Barrel_PartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Manufacturers[1].Manufacturer = obj("ManufacturerDefinition","gd_manufacturers.Manufacturers.Dahl")
    obj("WeaponPartDefinition","gd_weap_grenade_launcher.acc.acc2_Blitz").WeaponAttributeEffects.append(current_obj.ExternalAttributeEffects[2])
    obj("WeaponPartDefinition","gd_weap_grenade_launcher.acc.acc2_Blitz").WeaponAttributeEffects.append(current_obj.ExternalAttributeEffects[1])
    obj("WeaponPartDefinition","gd_weap_combat_rifle.UniqueParts.Sentinel_sight4").WeaponCardAttributes.append(obj("WeaponPartDefinition","gd_weap_combat_rifle.Sight.sight4").WeaponCardAttributes[0])
    obj("WeaponPartDefinition","gd_weap_combat_rifle.Barrel.barrel5_Hyperion_Destroyer").CustomPresentations.append(obj("AttributePresentationDefinition","gd_weap_sniper_rifle_semiauto.mag.mag5_Hyperion_Executioner:AttributePresentationDefinition_0"))
    obj("WeaponTypeDefinition","gd_weap_revolver_pistol.A_Weapon.WeaponType_revolver_pistol").CustomPresentations.append(obj("AttributePresentationDefinition","gd_weap_sniper_rifle_semiauto.A_Weapon.WeaponType_sniper_rifle_semiauto:AttributePresentationDefinition_0"))
    obj("WeaponPartDefinition","gd_weap_sniper_rifle_semiauto.UniqueParts.ReaversEdge_sight4").WeaponCardAttributes.append(obj("WeaponPartDefinition","gd_weap_sniper_rifle.Sight.sight4").WeaponCardAttributes[0])
    obj("WeaponPartDefinition","dlc3_gd_weap_UniqueParts.CombatRifle.TedioreAvenger_sight5").WeaponCardAttributes.append(obj("WeaponPartDefinition","gd_weap_combat_shotgun.Body.body3_Tediore_Defender").WeaponCardAttributes[0])
    obj("WeaponPartDefinition","dlc3_gd_weap_UniqueParts.RepeaterPistol.barrel5_AthenasWisdom").CustomPresentations.append(obj("AttributePresentationDefinition","gd_weap_sniper_rifle_semiauto.A_Weapon.WeaponType_sniper_rifle_semiauto:AttributePresentationDefinition_0"))

    # KeepAlive

    obj("ItemPartDefinition","gd_shields.UniqueParts.Shield_WeeWee_Material").ObjectFlags |= 0x4000
    obj("ItemPartDefinition","UP_Assets.UniqueParts.Shield_WeeWee_Material").ObjectFlags |= 0x4000

    # Shields

    obj("ItemPartDefinition","gd_shields.UniqueParts.Shield_WeeWee_Material").CustomPresentations.append(obj("AttributePresentationDefinition","UP_Assets.UniqueParts.Shield_WeeWee_Material:AttributePresentationDefinition_1"))
    obj("ItemPartDefinition","gd_shields.UniqueParts.Shield_WeeWee_Material").CustomPresentations.append(obj("AttributePresentationDefinition","UP_Assets.UniqueParts.Shield_WeeWee_Material:AttributePresentationDefinition_0"))

    # KeepAlive

    obj("SkillDefinition","gd_Skills2_Brick.Blaster.Revenge").ObjectFlags |= 0x4000
    obj("SkillDefinition","gd_Skills2_Brick.Blaster.RapidReload").ObjectFlags |= 0x4000
    obj("SkillDefinition","gd_Skills2_Brick.Tank.Unbreakable").ObjectFlags |= 0x4000
    obj("SkillDefinition","gd_Skills2_Lilith.Controller.GirlPower").ObjectFlags |= 0x4000
    obj("SkillDefinition","gd_Skills2_Lilith.Elemental.Resilience").ObjectFlags |= 0x4000
    obj("AttributeInitializationDefinition","gd_skills2_Roland.MiscData.QuickCharge_Init").ObjectFlags |= 0x4000

    # Skills

        # Brick
    obj("SkillDefinition","gd_Skills2_Brick.Blaster.Revenge").SkillEffectDefinitions.append(current_obj.SkillEffectDefinitions[1])
    obj("SkillDefinition","gd_Skills2_Brick.Blaster.Revenge").SkillEffectDefinitions[(len(current_obj.SkillEffectDefinitions)) - 1].AttributeToModify = obj("AttributeDefinition","d_attributes.DamageSourceModifiers.InstigatedGrenadeDamageModifier")
    obj("SkillDefinition","gd_Skills2_Brick.Blaster.RapidReload").SkillEffectDefinitions[1].BaseModifierValue.BaseValueConstant = -0.06
    obj("SkillDefinition","gd_Skills2_Brick.Blaster.RapidReload").SkillEffectDefinitions[1].PerGradeUpgrade.BaseValueConstant = -0.06
    obj("SkillDefinition","gd_Skills2_Brick.Tank.Unbreakable").bAvailableBerserk = True
    obj("SkillDefinition","gd_Skills2_Brick.Tank.Unbreakable").bAvailableDuringActionSkill = True

        # Lilith
    obj("SkillDefinition","gd_Skills2_Lilith.Controller.GirlPower").bAvailableAlways = True
    obj("SkillDefinition","gd_Skills2_Lilith.Elemental.Resilience").SkillEffectDefinitions.append(current_obj.SkillEffectDefinitions[5])
    obj("SkillDefinition","gd_Skills2_Lilith.Elemental.Resilience").SkillEffectDefinitions[(len(current_obj.SkillEffectDefinitions)) - 1].AttributeToModify = obj("AttributeDefinition","d_attributes.DamageTypeModifers.ShockPassiveDamageModifier")

        # Roland
    obj("AttributeInitializationDefinition","gd_skills2_Roland.MiscData.QuickCharge_Init").ValueFormula.Level.BaseValueAttribute = obj("AttributeDefinition","gd_skills2_Roland.SkillGradeModifiers.SkillGradeModifier_Roland_QuickCharge")
    obj("AttributeInitializationDefinition","gd_skills2_Roland.MiscData.QuickCharge_Init").ValueFormula.Multiplier.BaseValueAttribute = obj("ResourcePoolAttributeDefinition","d_attributes.ShieldResourcePool.ShieldMaxValue")

    # KeepAlive

    obj("ItemPartDefinition","gd_CommandDecks.RightSide.rightside3").ObjectFlags |= 0x4000
    obj("ItemPartDefinition","gd_CommandDecks.RightSide.rightside4").ObjectFlags |= 0x4000
    obj("ItemPartDefinition","gd_CommandDecks.RightSide.rightside5").ObjectFlags |= 0x4000
    obj("ItemPartDefinition","dlc3_gd_CommandDecks.Body_Loyalty.Loyalty_Mordecai_Anshin").ObjectFlags |= 0x4000
    obj("ItemPartDefinition","gd_CommandDecks.Body_Mordecai.Mordecai_Hunter").ObjectFlags |= 0x4000
    obj("ItemPartDefinition","gd_CommandDecks.Body_Mordecai.Mordecai_Ranger").ObjectFlags |= 0x4000
    obj("ItemPartDefinition","gd_CommandDecks.Body_Mordecai.Mordecai_Gunslinger").ObjectFlags |= 0x4000
    obj("ItemPartDefinition","dlc3_gd_CommandDecks.Body_Loyalty.Loyalty_Brick_Pangolin").ObjectFlags |= 0x4000
    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").ObjectFlags |= 0x4000
    obj("ItemPartDefinition","UP_Assets.ManufacturerMaterials.Material_alien_1").ObjectFlags |= 0x4000
    obj("ItemPartDefinition","UP_Assets.ManufacturerMaterials.Material_alien_2").ObjectFlags |= 0x4000
    obj("ItemPartDefinition","UP_Assets.ManufacturerMaterials.Material_alien_3").ObjectFlags |= 0x4000

    # Class mods

        # General
    obj("ItemPartDefinition","gd_CommandDecks.RightSide.rightside3").PartNumberAddend = 30
    obj("ItemPartDefinition","gd_CommandDecks.RightSide.rightside4").PartNumberAddend = 40
    obj("ItemPartDefinition","gd_CommandDecks.RightSide.rightside5").AttributeSlotUpgrades[1].GradeIncrease = 3
    obj("ItemPartDefinition","gd_CommandDecks.RightSide.rightside5").AttributeSlotUpgrades[2].GradeIncrease = 3
    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts.append(current_obj.WeightedParts[30])

    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Part = obj("ItemPartDefinition","UP_Assets.ManufacturerMaterials.Material_alien_1")
    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition","gd_manufacturers.Manufacturers.Eridian")

    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts.append(current_obj.WeightedParts[31])

    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Part = obj("ItemPartDefinition","UP_Assets.ManufacturerMaterials.Material_alien_2")
    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition","gd_manufacturers.Manufacturers.Eridian")

    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts.append(current_obj.WeightedParts[32])

    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Part = obj("ItemPartDefinition","UP_Assets.ManufacturerMaterials.Material_alien_3")
    obj("ItemPartListDefinition","gd_CommandDecks.MaterialPartsLists.CommandDeckMaterialPartList").WeightedParts[(len(current_obj.WeightedParts)) - 1].Manufacturers[0].Manufacturer = obj("ManufacturerDefinition","gd_manufacturers.Manufacturers.Eridian")



        # Mordecai
    obj("ItemPartDefinition","dlc3_gd_CommandDecks.Body_Loyalty.Loyalty_Mordecai_Anshin").AttributeSlotEffects[1].BaseModifierValue.BaseValueConstant = 0.2
    obj("ItemPartDefinition","dlc3_gd_CommandDecks.Body_Loyalty.Loyalty_Mordecai_Anshin").AttributeSlotEffects[1].PerGradeUpgrade.BaseValueConstant = 0.04
    obj("ItemPartDefinition","gd_CommandDecks.Body_Mordecai.Mordecai_Hunter").AttributeSlotEffects[2].BaseModifierValue.BaseValueConstant = 0.2
    obj("ItemPartDefinition","gd_CommandDecks.Body_Mordecai.Mordecai_Hunter").AttributeSlotEffects[2].PerGradeUpgrade.BaseValueConstant = 0.04
    obj("ItemPartDefinition","gd_CommandDecks.Body_Mordecai.Mordecai_Hunter").AttributeSlotEffects[2].AttributeToModify = obj("AttributeDefinition","d_attributes.ActiveSkillCooldownResource.ActiveSkillCooldownConsumptionRate")
    obj("ItemPartDefinition","gd_CommandDecks.Body_Mordecai.Mordecai_Ranger").AttributeSlotEffects[2].BaseModifierValue.BaseValueConstant = 0.3
    obj("ItemPartDefinition","gd_CommandDecks.Body_Mordecai.Mordecai_Ranger").AttributeSlotEffects[2].PerGradeUpgrade.BaseValueConstant = 0.06
    obj("ItemPartDefinition","gd_CommandDecks.Body_Mordecai.Mordecai_Gunslinger").AttributeSlotEffects[4].AttributeToModify = obj("AttributeDefinition","gd_skills2_Mordecai.SkillGradeModifiers.SkillGradeModifier_Mordecai_BloodRage")

        # Brick
    obj("ItemPartDefinition","dlc3_gd_CommandDecks.Body_Loyalty.Loyalty_Brick_Pangolin").AttributeSlotEffects[1].BaseModifierValue.BaseValueConstant = 0.2
    obj("ItemPartDefinition","dlc3_gd_CommandDecks.Body_Loyalty.Loyalty_Brick_Pangolin").AttributeSlotEffects[1].PerGradeUpgrade.BaseValueConstant = 0.04

    # KeepAlive

    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Helix").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.rocket_Leviathan").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Medium").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Medium_Mongol").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Medium_Nidhogg").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Medium_Rhino").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.rocket_mini").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_combat_shotgun.Rockets.rocket_mini").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Large_Impact").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Large_Leviathan").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Medium").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Medium_Impact").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Medium_Rebounder").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Rainmaker_Children").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_SandS_Rainmaker").ObjectFlags |= 0x4000
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Sticky").ObjectFlags |= 0x4000

    #Projectiles

    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Helix").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.rocket_Leviathan").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Medium").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Medium_Mongol").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Medium_Nidhogg").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Medium_Rhino").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.rocket_mini").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_combat_shotgun.Rockets.rocket_mini").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Large_Impact").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Large_Leviathan").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Medium").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Medium_Impact").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Medium_Rebounder").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Rainmaker_Children").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_SandS_Rainmaker").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_Sticky").bUseAccurateCollision = False


    obj("ProjectileDefinition","gd_weap_grenade_launcher.Grenades.Grenade_SandS_Rainmaker").DefaultBehaviorSet.OnExplode[1].ChildProjectileBaseValues.append(obj("ProjectileDefinition","gd_grenades.Longbow.HandGrenade_LongBow").DefaultBehaviorSet.OnExplode[2].ChildProjectileBaseValues[0])

    # KeepAlive

    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_Pistol_LevelBonus").ObjectFlags |= 0x4000
    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_Shotgun_LevelBonus").ObjectFlags |= 0x4000
    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_Sniper_LevelBonus").ObjectFlags |= 0x4000
    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_SMG_LevelBonus").ObjectFlags |= 0x4000
    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_RocketLauncer_LevelBonus").ObjectFlags |= 0x4000
    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_Eridan_LevelBonus").ObjectFlags |= 0x4000
    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_CombatRifle_LevelBonus").ObjectFlags |= 0x4000
    obj("AttributeDefinition","d_attributes.Inventory.ShieldItemLevel").ObjectFlags |= 0x4000
    obj("AttributePresentationDefinition","gd_AttributePresentation.Skills_Mordecai.AttrPresent_SkillGradeModifier_Mordecai_BloodRage").ObjectFlags |= 0x4000
    obj("AttributeInitializationDefinition","dlc3_gd_Balance.GamestageCap.AmmoVending_GamestageCap_50").ObjectFlags |= 0x4000
    obj("AttributeInitializationDefinition","dlc4_gd_items.GamestageCap.AmmoVending_GamestageCap_50").ObjectFlags |= 0x4000
    obj("HUDDefinition","d_hud_MOD.TestHUDClass").ObjectFlags |= 0x4000
    obj("PlayerClassDefinition","gd_Roland.Character.CharacterClass_Roland").ObjectFlags |= 0x4000
    obj("PlayerClassDefinition","gd_lilith.Character.CharacterClass_Lilith").ObjectFlags |= 0x4000
    obj("PlayerClassDefinition","gd_Brick.Character.CharacterClass_Brick").ObjectFlags |= 0x4000
    obj("PlayerClassDefinition","gd_mordecai.Character.CharacterClass_Mordecai").ObjectFlags |= 0x4000
    obj("GlobalsDefinition","gd_globals.General.Globals").ObjectFlags |= 0x4000
    obj("AttributePresentationDefinition","gd_AttributePresentation.Weapons.AttrPresent_AccuracyOnIdleRegenerationRate").ObjectFlags |= 0x4000


    # Misc

    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_Pistol_LevelBonus").ValueResolverChain.append(obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_Gear_LevelBonus").ValueResolverChain[0])
    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_Pistol_LevelBonus").ValueResolverChain.pop(0)
    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_Shotgun_LevelBonus").ValueResolverChain.append(obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_Gear_LevelBonus").ValueResolverChain[0])
    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_Shotgun_LevelBonus").ValueResolverChain.pop(0)
    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_Sniper_LevelBonus").ValueResolverChain.append(obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_Gear_LevelBonus").ValueResolverChain[0])
    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_Sniper_LevelBonus").ValueResolverChain.pop(0)
    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_SMG_LevelBonus").ValueResolverChain.append(obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_Gear_LevelBonus").ValueResolverChain[0])
    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_SMG_LevelBonus").ValueResolverChain.pop(0)
    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_RocketLauncer_LevelBonus").ValueResolverChain.append(obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_Gear_LevelBonus").ValueResolverChain[0])
    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_RocketLauncer_LevelBonus").ValueResolverChain.pop(0)
    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_Eridan_LevelBonus").ValueResolverChain.append(obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_Gear_LevelBonus").ValueResolverChain[0])
    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_Eridan_LevelBonus").ValueResolverChain.pop(0)
    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_CombatRifle_LevelBonus").ValueResolverChain.append(obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_Gear_LevelBonus").ValueResolverChain[0])
    obj("AttributeDefinition","gd_Balance.LevelLimits.Proficiency_CombatRifle_LevelBonus").ValueResolverChain.pop(0)
    obj("AttributeDefinition","d_attributes.Inventory.ShieldItemLevel").ContextResolverChain[0].InventoryDefinition = None
    obj("AttributePresentationDefinition","gd_AttributePresentation.Skills_Mordecai.AttrPresent_SkillGradeModifier_Mordecai_BloodRage").Description = "Hair Trigger Skill"
    obj("AttributeInitializationDefinition","dlc3_gd_Balance.GamestageCap.AmmoVending_GamestageCap_50").RangeRestriction.MaxValue.BaseValueConstant = 69
    obj("AttributeInitializationDefinition","dlc4_gd_items.GamestageCap.AmmoVending_GamestageCap_50").RangeRestriction.MaxValue.BaseValueConstant = 69
    obj("GlobalsDefinition","gd_globals.General.Globals").AttributePresentationTranslation="<font size='13'>$NUMBER$ $CONSTRAINT$ $DESCRIPTION$</font>"
    obj("AttributePresentationDefinition","gd_AttributePresentation.Weapons.AttrPresent_AccuracyOnIdleRegenerationRate").bBiggerIsBetter = True
    obj("GlobalsDefinition","gd_globals.General.Globals").WeaponProficiencySkills.append(obj("SkillDefinition","CritFix.CritFix"))

    obj("PlayerClassDefinition","gd_Roland.Character.CharacterClass_Roland").HUDDefinition = obj("HUDDefinition","d_hud_MOD.TestHUDClass")
    obj("PlayerClassDefinition","gd_lilith.Character.CharacterClass_Lilith").HUDDefinition = obj("HUDDefinition","d_hud_MOD.TestHUDClass")
    obj("PlayerClassDefinition","gd_Brick.Character.CharacterClass_Brick").HUDDefinition = obj("HUDDefinition","d_hud_MOD.TestHUDClass")
    obj("PlayerClassDefinition","gd_mordecai.Character.CharacterClass_Mordecai").HUDDefinition = obj("HUDDefinition","d_hud_MOD.TestHUDClass")


def patch_volatile():
    # Itempools

        # Shops
    obj("ItemPoolDefinition","gd_itempools_Shop.Items.shoppool_FeaturedItem_WeaponMachine").BalancedItems.append(current_obj.BalancedItems[5])
    obj("ItemPoolDefinition","gd_itempools_Shop.Items.shoppool_FeaturedItem_WeaponMachine").BalancedItems[(len(current_obj.BalancedItems)) - 1].InvBalanceDefinition = obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_SupportMachineGun")
    obj("ItemPoolDefinition","gd_itempools_Shop.Items.shoppool_Weapons_flatChance").BalancedItems.append(current_obj.BalancedItems[5])
    obj("ItemPoolDefinition","gd_itempools_Shop.Items.shoppool_Weapons_flatChance").BalancedItems[(len(current_obj.BalancedItems)) - 1].InvBalanceDefinition = obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_SupportMachineGun")

        # Enemies
    obj("ItemPoolDefinition","gd_itempools.CrimsonLance.Infantry_Weapons").BalancedItems[1].bDropOnDeath = True
    obj("ItemPoolDefinition","gd_itempools.CrimsonLance.Infantry_Weapons_Badass").BalancedItems[0].bDropOnDeath = True
    obj("ItemPoolDefinition","dlc3_gd_itempools.CrimsonLance.Infantry_Weapons_Badass_enhance").BalancedItems[0].bDropOnDeath = True

        # Misc
    obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades.append(obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[9])
    obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[(len(current_obj.Grades)) - 1].GameStageRequirement.MinGameStage = 53
    obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[(len(current_obj.Grades)) - 1].GameStageRequirement.MaxGameStage = 100
    obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Explosive").Grades.append(obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[10])
    obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Incendiary").Grades.append(obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[10])
    obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Shock").Grades.append(obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[10])
    obj("InteractiveObjectBalanceDefinition","gd_balance_objects.FuelTanks.ObjectGrade_ExplodingFuelTank").Grades.append(obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[10])
    obj("InteractiveObjectBalanceDefinition","dlc3_gd_explosives.SeaMine.BalanceDef_SeaMine").Grades[5].GameStageRequirement.MaxGameStage = 100

    # Enemies

    obj("PopulationDefinition","dlc3_gd_population_enemies.Drifters.DrifterSquad_Drifter").ActorArchetypeList.append(obj("PopulationDefinition","dlc3_gd_population_enemies.Drifters.DrifterSquad_BadassDrifter").ActorArchetypeList[0])




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
            patch_volatile()
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
    settings_file=Path(f"{SETTINGS_DIR}/UnofficialPatchSDK.json"),
)

logging.info(f"Unofficial Patch SDK Loaded: {__version__}, {__version_info__}")
