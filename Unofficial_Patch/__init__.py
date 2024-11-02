import unrealsdk

from pathlib import Path
from unrealsdk.hooks import Type
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc 
from mods_base.options import BaseOption, SliderOption
from mods_base import SETTINGS_DIR
from mods_base import build_mod
from unrealsdk import logging

bPatched = False
bPatched_volatile = False
Count = 0

def patch():

    # Titles & Prefixes

    unrealsdk.load_package("gd_weap_support_machinegun.Title.TitleM_SandS_Draco")

    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_sniper_rifle_semiauto.Title.Title_Damage1_Driver").ObjectFlags |= 0x4000
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_support_machinegun.Title.TitleM_SandS_Draco").ObjectFlags |= 0x4000
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_sniper_rifle_semiauto.Title.TitleM_Dahl1_Penetrator").ObjectFlags |= 0x4000
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_assault_shotgun.Title.TitleM_Maliwan1_Plague").ObjectFlags |= 0x4000
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_sniper_rifle_semiauto.Title.TitleM_Hyperion1_Executioner").ObjectFlags |= 0x4000
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").ObjectFlags |= 0x4000
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_combat_shotgun.Prefix.Prefix_Damage1_Terrible").ObjectFlags |= 0x4000
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_repeater_pistol.Prefix.Prefix_Nasty").ObjectFlags |= 0x4000
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_combat_shotgun.Prefix.Prefix_Acc1_Jagged").ObjectFlags |= 0x4000



    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_sniper_rifle_semiauto.Title.Title_Damage1_Driver").PartName = "Driver"
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_support_machinegun.Title.TitleM_SandS_Draco").Rarity.BaseValueAttribute = (unrealsdk.find_object("InventoryAttributeDefinition", "gd_Balance_Inventory.Rarity_Weapon.WeaponPartRarity6_Legendary"))
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_sniper_rifle_semiauto.Title.TitleM_Dahl1_Penetrator").Rarity.BaseValueAttribute = (unrealsdk.find_object("InventoryAttributeDefinition", "gd_Balance_Inventory.Rarity_Weapon.WeaponPartRarity6_Legendary"))
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_assault_shotgun.Title.TitleM_Maliwan1_Plague").PartName = "Plague"
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_sniper_rifle_semiauto.Title.TitleM_Hyperion1_Executioner").PartName = "Executioner"
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").Expressions[0].ConstantOperand2 = 0
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").Expressions.append(unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").Expressions[0])
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").Expressions.append(unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").Expressions[0])
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").Expressions.append(unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").Expressions[0])
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").Expressions[0].AttributeOperand1 = unrealsdk.find_object("AttributeDefinition", "d_attributes.WeaponDamageType.WeaponDamage_Is_Corrosive")
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").Expressions[1].AttributeOperand1 = unrealsdk.find_object("AttributeDefinition", "d_attributes.WeaponDamageType.WeaponDamage_Is_Explosive")
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").Expressions[2].AttributeOperand1 = unrealsdk.find_object("AttributeDefinition", "d_attributes.WeaponDamageType.WeaponDamage_Is_Incendiary")
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_patrol_smg.Prefix.Prefix_Barrel3_Twisted").Expressions[3].AttributeOperand1 = unrealsdk.find_object("AttributeDefinition", "d_attributes.WeaponDamageType.WeaponDamage_Is_Shock")
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_combat_shotgun.Prefix.Prefix_Damage1_Terrible").Expressions.append(unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_repeater_pistol.Prefix.Prefix_Nasty").Expressions[1])
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_combat_shotgun.Prefix.Prefix_Damage1_Terrible").Expressions[0].AttributeOperand1 = unrealsdk.find_object("AttributeDefinition", "d_attributes.Weapon.WeaponDamageNormalized")
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_combat_shotgun.Prefix.Prefix_Damage1_Terrible").Expressions[0].ConstantOperand2 = 2
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_repeater_pistol.Prefix.Prefix_Nasty").Expressions[1].AttributeOperand1 = unrealsdk.find_object("AttributeDefinition", "d_attributes.Weapon.WeaponDamageNormalized")
    unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_combat_shotgun.Prefix.Prefix_Acc1_Jagged").PartName = "Jagged"


    # Weapon Parts

    unrealsdk.load_package("gd_weap_patrol_smg.UniqueParts.BoneShredder_Material")
    unrealsdk.load_package("gd_weap_grenade_launcher.Barrel.barrel3_Dahl_Onslaught")

    unrealsdk.load_package("gd_weap_machine_pistol.UniqueParts.TheClipper_acc5_Incendiary")
    unrealsdk.load_package("gd_customweapons.PartCollections.PartCollection_SMG_BoneShredder")
    unrealsdk.load_package("dlc3_gd_weap_UniqueParts.SemiAutoSniper.acc2_KyrosPower")



    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_machine_pistol.UniqueParts.TheClipper_acc5_Incendiary").ObjectFlags |= 0x4000
    unrealsdk.find_object("WeaponPartListCollectionDefinition", "gd_customweapons.PartCollections.PartCollection_SMG_BoneShredder").ObjectFlags |= 0x4000
    unrealsdk.find_object("WeaponPartDefinition", "dlc3_gd_weap_UniqueParts.SemiAutoSniper.acc2_KyrosPower").ObjectFlags |= 0x4000
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_support_machinegun.acc.acc4_SandS_Draco_Incendiary").ObjectFlags |= 0x4000
    unrealsdk.find_object("WeaponPartListDefinition", "gd_weap_assault_shotgun.acc.Acc_PartList").ObjectFlags |= 0x4000
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_patrol_smg.Barrel.barrel5_Hyperion_Bitch").ObjectFlags |= 0x4000
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_machine_pistol.Barrel.barrel5_Vladof_Vengence").ObjectFlags |= 0x4000
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_machine_pistol.acc.acc1_Hyperion_Reaper").ObjectFlags |= 0x4000
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_repeater_pistol.acc.acc5_Corrosive").ObjectFlags |= 0x4000
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_repeater_pistol.UniqueParts.TheDove_barrel4").ObjectFlags |= 0x4000
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_rocket_launcher.acc.acc2_Evil").ObjectFlags |= 0x4000
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_assault_shotgun.acc.acc1_Spiked").ObjectFlags |= 0x4000
    unrealsdk.find_object("WeaponPartListDefinition", "gd_weap_grenade_launcher.Barrel.Barrel_PartList").ObjectFlags |= 0x4000



    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_support_machinegun.acc.acc4_SandS_Draco_Incendiary").TitleList.append(unrealsdk.find_object("WeaponNamePartDefinition", "gd_weap_support_machinegun.Title.TitleM_SandS_Draco"))
    unrealsdk.find_object("WeaponPartListDefinition", "gd_weap_assault_shotgun.acc.Acc_PartList").WeightedParts[7].DefaultWeight.BaseValueScaleConstant = 1
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_patrol_smg.Barrel.barrel5_Hyperion_Bitch").ExternalAttributeEffects[2].ModifierType = 1
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_patrol_smg.Barrel.barrel5_Hyperion_Bitch").ExternalAttributeEffects[2].BaseModifierValue.BaseValueConstant = 1.5
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_machine_pistol.Barrel.barrel5_Vladof_Vengence").ExternalAttributeEffects.append(unrealsdk.find_object("WeaponPartDefinition", "gd_weap_machine_pistol.Barrel.barrel5_Vladof_Vengence").WeaponAttributeEffects[4])
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_machine_pistol.Barrel.barrel5_Vladof_Vengence").WeaponAttributeEffects.pop(4)
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_machine_pistol.acc.acc1_Hyperion_Reaper").ExternalAttributeEffects.append(unrealsdk.find_object("WeaponPartDefinition", "gd_weap_machine_pistol.acc.acc1_Hyperion_Reaper").WeaponAttributeEffects[0])
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_machine_pistol.acc.acc1_Hyperion_Reaper").WeaponAttributeEffects.pop(0)
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_repeater_pistol.acc.acc5_Corrosive").TechAbilities[4].RequiredTechLevel = 15
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_machine_pistol.UniqueParts.TheClipper_acc5_Incendiary").ExternalAttributeEffects.append(unrealsdk.find_object("WeaponPartDefinition", "gd_weap_machine_pistol.UniqueParts.TheClipper_acc5_Incendiary").WeaponAttributeEffects[1])
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_machine_pistol.UniqueParts.TheClipper_acc5_Incendiary").WeaponAttributeEffects.pop(1)
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_repeater_pistol.UniqueParts.TheDove_barrel4").WeaponAttributeEffects[0].ModifierType = 0
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_repeater_pistol.UniqueParts.TheDove_barrel4").WeaponAttributeEffects[0].BaseModifierValue.BaseValueConstant = -10000
    unrealsdk.find_object("WeaponPartListCollectionDefinition", "gd_customweapons.PartCollections.PartCollection_SMG_BoneShredder").MaterialPartData.WeightedParts[0].Part = unrealsdk.find_object("WeaponPartDefinition", "gd_weap_patrol_smg.UniqueParts.BoneShredder_Material")
    unrealsdk.find_object("WeaponPartDefinition", "dlc3_gd_weap_UniqueParts.SemiAutoSniper.acc2_KyrosPower").CustomDamageTypeDefinition = unrealsdk.find_object("WillowDamageTypeDefinition", "gd_Explosive.DamageType.DmgType_Explosive")
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_rocket_launcher.acc.acc2_Evil").WeaponAttributeEffects.append(unrealsdk.find_object("WeaponPartDefinition", "gd_weap_machine_pistol.Barrel.barrel5_Vladof_Vengence").ExternalAttributeEffects[2])
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_rocket_launcher.acc.acc2_Evil").ExternalAttributeEffects.pop(2)
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_rocket_launcher.acc.acc2_Evil").WeaponAttributeEffects.append(unrealsdk.find_object("WeaponPartDefinition", "gd_weap_machine_pistol.Barrel.barrel5_Vladof_Vengence").ExternalAttributeEffects[1])
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_rocket_launcher.acc.acc2_Evil").ExternalAttributeEffects.pop(1)
    unrealsdk.find_object("WeaponPartDefinition", "gd_weap_assault_shotgun.acc.acc1_Spiked").ExternalAttributeEffects[0].ModifierType = 1
    unrealsdk.find_object("WeaponPartListDefinition", "gd_weap_grenade_launcher.Barrel.Barrel_PartList").WeightedParts.append(unrealsdk.find_object("WeaponPartListDefinition", "gd_weap_grenade_launcher.Barrel.Barrel_PartList").WeightedParts[10])
    unrealsdk.find_object("WeaponPartListDefinition", "gd_weap_grenade_launcher.Barrel.Barrel_PartList").WeightedParts[11].Part = unrealsdk.find_object("WeaponPartDefinition", "gd_weap_grenade_launcher.Barrel.barrel3_Dahl_Onslaught")
    unrealsdk.find_object("WeaponPartListDefinition", "gd_weap_grenade_launcher.Barrel.Barrel_PartList").WeightedParts[11].Manufacturers[1].Manufacturer = unrealsdk.find_object("ManufacturerDefinition", "gd_manufacturers.Manufacturers.Dahl")

    # Skills

    unrealsdk.find_object("SkillDefinition", "gd_Skills2_Brick.Blaster.Revenge").ObjectFlags |= 0x4000
    unrealsdk.find_object("SkillDefinition", "gd_Skills2_Brick.Blaster.RapidReload").ObjectFlags |= 0x4000
    unrealsdk.find_object("SkillDefinition", "gd_Skills2_Brick.Tank.Unbreakable").ObjectFlags |= 0x4000
    unrealsdk.find_object("SkillDefinition", "gd_Skills2_Lilith.Controller.GirlPower").ObjectFlags |= 0x4000
    unrealsdk.find_object("SkillDefinition", "gd_Skills2_Lilith.Elemental.Resilience").ObjectFlags |= 0x4000
    unrealsdk.find_object("AttributeInitializationDefinition", "gd_skills2_Roland.MiscData.QuickCharge_Init").ObjectFlags |= 0x4000


        # Brick
    unrealsdk.find_object("SkillDefinition", "gd_Skills2_Brick.Blaster.Revenge").SkillEffectDefinitions.append(unrealsdk.find_object("SkillDefinition", "gd_Skills2_Brick.Blaster.Revenge").SkillEffectDefinitions[1])
    unrealsdk.find_object("SkillDefinition", "gd_Skills2_Brick.Blaster.Revenge").SkillEffectDefinitions[2].AttributeToModify = unrealsdk.find_object("AttributeDefinition", "d_attributes.DamageSourceModifiers.InstigatedGrenadeDamageModifier")
    unrealsdk.find_object("SkillDefinition", "gd_Skills2_Brick.Blaster.RapidReload").SkillEffectDefinitions[1].BaseModifierValue.BaseValueConstant = -0.06
    unrealsdk.find_object("SkillDefinition", "gd_Skills2_Brick.Blaster.RapidReload").SkillEffectDefinitions[1].PerGradeUpgrade.BaseValueConstant = -0.06
    unrealsdk.find_object("SkillDefinition", "gd_Skills2_Brick.Tank.Unbreakable").bAvailableBerserk = True
    unrealsdk.find_object("SkillDefinition", "gd_Skills2_Brick.Tank.Unbreakable").bAvailableDuringActionSkill = True

        # Lilith
    unrealsdk.find_object("SkillDefinition", "gd_Skills2_Lilith.Controller.GirlPower").bAvailableAlways = True
    unrealsdk.find_object("SkillDefinition", "gd_Skills2_Lilith.Elemental.Resilience").SkillEffectDefinitions.append(unrealsdk.find_object("SkillDefinition", "gd_Skills2_Lilith.Elemental.Resilience").SkillEffectDefinitions[5])
    unrealsdk.find_object("SkillDefinition", "gd_Skills2_Lilith.Elemental.Resilience").SkillEffectDefinitions[6].AttributeToModify = unrealsdk.find_object("AttributeDefinition", "d_attributes.DamageTypeModifers.ShockPassiveDamageModifier")

        # Roland
    unrealsdk.find_object("AttributeInitializationDefinition", "gd_skills2_Roland.MiscData.QuickCharge_Init").ValueFormula.Level.BaseValueAttribute = unrealsdk.find_object("AttributeDefinition", "gd_skills2_Roland.SkillGradeModifiers.SkillGradeModifier_Roland_QuickCharge")
    unrealsdk.find_object("AttributeInitializationDefinition", "gd_skills2_Roland.MiscData.QuickCharge_Init").ValueFormula.Multiplier.BaseValueAttribute = unrealsdk.find_object("ResourcePoolAttributeDefinition", "d_attributes.ShieldResourcePool.ShieldMaxValue")



    # Class Mods


    unrealsdk.find_object("ItemPartDefinition", "gd_CommandDecks.RightSide.rightside3").ObjectFlags |= 0x4000
    unrealsdk.find_object("ItemPartDefinition", "gd_CommandDecks.RightSide.rightside4").ObjectFlags |= 0x4000
    unrealsdk.find_object("ItemPartDefinition", "gd_CommandDecks.RightSide.rightside5").ObjectFlags |= 0x4000
    unrealsdk.find_object("ItemPartDefinition", "dlc3_gd_CommandDecks.Body_Loyalty.Loyalty_Mordecai_Anshin").ObjectFlags |= 0x4000
    unrealsdk.find_object("ItemPartDefinition", "gd_CommandDecks.Body_Mordecai.Mordecai_Hunter").ObjectFlags |= 0x4000
    unrealsdk.find_object("ItemPartDefinition", "gd_CommandDecks.Body_Mordecai.Mordecai_Ranger").ObjectFlags |= 0x4000
    unrealsdk.find_object("ItemPartDefinition", "gd_CommandDecks.Body_Mordecai.Mordecai_Gunslinger").ObjectFlags |= 0x4000
    unrealsdk.find_object("ItemPartDefinition", "dlc3_gd_CommandDecks.Body_Loyalty.Loyalty_Brick_Pangolin").ObjectFlags |= 0x4000




    unrealsdk.find_object("ItemPartDefinition", "gd_CommandDecks.RightSide.rightside3").PartNumberAddend = 30
    unrealsdk.find_object("ItemPartDefinition", "gd_CommandDecks.RightSide.rightside4").PartNumberAddend = 40
    unrealsdk.find_object("ItemPartDefinition", "gd_CommandDecks.RightSide.rightside5").AttributeSlotUpgrades[1].GradeIncrease = 3
    unrealsdk.find_object("ItemPartDefinition", "gd_CommandDecks.RightSide.rightside5").AttributeSlotUpgrades[2].GradeIncrease = 3

        # Mordecai
    unrealsdk.find_object("ItemPartDefinition", "dlc3_gd_CommandDecks.Body_Loyalty.Loyalty_Mordecai_Anshin").AttributeSlotEffects[1].BaseModifierValue.BaseValueConstant = 0.2
    unrealsdk.find_object("ItemPartDefinition", "dlc3_gd_CommandDecks.Body_Loyalty.Loyalty_Mordecai_Anshin").AttributeSlotEffects[1].PerGradeUpgrade.BaseValueConstant = 0.04
    unrealsdk.find_object("ItemPartDefinition", "gd_CommandDecks.Body_Mordecai.Mordecai_Hunter").AttributeSlotEffects[2].BaseModifierValue.BaseValueConstant = 0.2
    unrealsdk.find_object("ItemPartDefinition", "gd_CommandDecks.Body_Mordecai.Mordecai_Hunter").AttributeSlotEffects[2].PerGradeUpgrade.BaseValueConstant = 0.04
    unrealsdk.find_object("ItemPartDefinition", "gd_CommandDecks.Body_Mordecai.Mordecai_Hunter").AttributeSlotEffects[2].AttributeToModify = unrealsdk.find_object("AttributeDefinition", "d_attributes.ActiveSkillCooldownResource.ActiveSkillCooldownConsumptionRate")
    unrealsdk.find_object("ItemPartDefinition", "gd_CommandDecks.Body_Mordecai.Mordecai_Ranger").AttributeSlotEffects[2].BaseModifierValue.BaseValueConstant = 0.3
    unrealsdk.find_object("ItemPartDefinition", "gd_CommandDecks.Body_Mordecai.Mordecai_Ranger").AttributeSlotEffects[2].PerGradeUpgrade.BaseValueConstant = 0.06
    unrealsdk.find_object("ItemPartDefinition", "gd_CommandDecks.Body_Mordecai.Mordecai_Gunslinger").AttributeSlotEffects[4].AttributeToModify = unrealsdk.find_object("AttributeDefinition", "gd_skills2_Mordecai.SkillGradeModifiers.SkillGradeModifier_Mordecai_BloodRage")

        # Brick
    unrealsdk.find_object("ItemPartDefinition", "dlc3_gd_CommandDecks.Body_Loyalty.Loyalty_Brick_Pangolin").AttributeSlotEffects[1].BaseModifierValue.BaseValueConstant = 0.2
    unrealsdk.find_object("ItemPartDefinition", "dlc3_gd_CommandDecks.Body_Loyalty.Loyalty_Brick_Pangolin").AttributeSlotEffects[1].PerGradeUpgrade.BaseValueConstant = 0.04

    # Rockets

    unrealsdk.find_object("ProjectileDefinition", "gd_weap_rocket_launcher.Rockets.Rocket_Helix").ObjectFlags |= 0x4000
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_rocket_launcher.Rockets.rocket_Leviathan").ObjectFlags |= 0x4000
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_rocket_launcher.Rockets.Rocket_Medium").ObjectFlags |= 0x4000
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_rocket_launcher.Rockets.Rocket_Medium_Mongol").ObjectFlags |= 0x4000
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_rocket_launcher.Rockets.Rocket_Medium_Nidhogg").ObjectFlags |= 0x4000
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_rocket_launcher.Rockets.Rocket_Medium_Rhino").ObjectFlags |= 0x4000
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_rocket_launcher.Rockets.rocket_mini").ObjectFlags |= 0x4000
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_combat_shotgun.Rockets.rocket_mini").ObjectFlags |= 0x4000
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_grenade_launcher.Grenades.Grenade_Large_Impact").ObjectFlags |= 0x4000
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_grenade_launcher.Grenades.Grenade_Large_Leviathan").ObjectFlags |= 0x4000
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_grenade_launcher.Grenades.Grenade_Medium").ObjectFlags |= 0x4000
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_grenade_launcher.Grenades.Grenade_Medium_Impact").ObjectFlags |= 0x4000
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_grenade_launcher.Grenades.Grenade_Medium_Rebounder").ObjectFlags |= 0x4000
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_grenade_launcher.Grenades.Grenade_Rainmaker_Children").ObjectFlags |= 0x4000
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_grenade_launcher.Grenades.Grenade_SandS_Rainmaker").ObjectFlags |= 0x4000
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_grenade_launcher.Grenades.Grenade_Sticky").ObjectFlags |= 0x4000





    unrealsdk.find_object("ProjectileDefinition", "gd_weap_rocket_launcher.Rockets.Rocket_Helix").bUseAccurateCollision = False
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_rocket_launcher.Rockets.rocket_Leviathan").bUseAccurateCollision = False
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_rocket_launcher.Rockets.Rocket_Medium").bUseAccurateCollision = False
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_rocket_launcher.Rockets.Rocket_Medium_Mongol").bUseAccurateCollision = False
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_rocket_launcher.Rockets.Rocket_Medium_Nidhogg").bUseAccurateCollision = False
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_rocket_launcher.Rockets.Rocket_Medium_Rhino").bUseAccurateCollision = False
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_rocket_launcher.Rockets.rocket_mini").bUseAccurateCollision = False
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_combat_shotgun.Rockets.rocket_mini").bUseAccurateCollision = False
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_grenade_launcher.Grenades.Grenade_Large_Impact").bUseAccurateCollision = False
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_grenade_launcher.Grenades.Grenade_Large_Leviathan").bUseAccurateCollision = False
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_grenade_launcher.Grenades.Grenade_Medium").bUseAccurateCollision = False
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_grenade_launcher.Grenades.Grenade_Medium_Impact").bUseAccurateCollision = False
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_grenade_launcher.Grenades.Grenade_Medium_Rebounder").bUseAccurateCollision = False
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_grenade_launcher.Grenades.Grenade_Rainmaker_Children").bUseAccurateCollision = False
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_grenade_launcher.Grenades.Grenade_SandS_Rainmaker").bUseAccurateCollision = False
    unrealsdk.find_object("ProjectileDefinition", "gd_weap_grenade_launcher.Grenades.Grenade_Sticky").bUseAccurateCollision = False

    unrealsdk.find_object("ProjectileDefinition", "gd_weap_grenade_launcher.Grenades.Grenade_SandS_Rainmaker").DefaultBehaviorSet.OnExplode[1].ChildProjectileBaseValues.append(unrealsdk.find_object("ProjectileDefinition", "gd_grenades.Longbow.HandGrenade_LongBow").DefaultBehaviorSet.OnExplode[2].ChildProjectileBaseValues[0])





    # Misc

    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_Pistol_LevelBonus").ObjectFlags |= 0x4000
    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_Shotgun_LevelBonus").ObjectFlags |= 0x4000
    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_Sniper_LevelBonus").ObjectFlags |= 0x4000
    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_SMG_LevelBonus").ObjectFlags |= 0x4000
    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_RocketLauncer_LevelBonus").ObjectFlags |= 0x4000
    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_Eridan_LevelBonus").ObjectFlags |= 0x4000
    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_CombatRifle_LevelBonus").ObjectFlags |= 0x4000
    unrealsdk.find_object("AttributeDefinition", "d_attributes.Inventory.ShieldItemLevel").ObjectFlags |= 0x4000
    unrealsdk.find_object("AttributePresentationDefinition", "gd_AttributePresentation.Skills_Mordecai.AttrPresent_SkillGradeModifier_Mordecai_BloodRage").ObjectFlags |= 0x4000

    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_Pistol_LevelBonus").ValueResolverChain.append(unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_Gear_LevelBonus").ValueResolverChain[0])
    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_Pistol_LevelBonus").ValueResolverChain.pop(0)
    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_Shotgun_LevelBonus").ValueResolverChain.append(unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_Gear_LevelBonus").ValueResolverChain[0])
    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_Shotgun_LevelBonus").ValueResolverChain.pop(0)
    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_Sniper_LevelBonus").ValueResolverChain.append(unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_Gear_LevelBonus").ValueResolverChain[0])
    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_Sniper_LevelBonus").ValueResolverChain.pop(0)
    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_SMG_LevelBonus").ValueResolverChain.append(unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_Gear_LevelBonus").ValueResolverChain[0])
    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_SMG_LevelBonus").ValueResolverChain.pop(0)
    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_RocketLauncer_LevelBonus").ValueResolverChain.append(unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_Gear_LevelBonus").ValueResolverChain[0])
    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_RocketLauncer_LevelBonus").ValueResolverChain.pop(0)
    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_Eridan_LevelBonus").ValueResolverChain.append(unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_Gear_LevelBonus").ValueResolverChain[0])
    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_Eridan_LevelBonus").ValueResolverChain.pop(0)
    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_CombatRifle_LevelBonus").ValueResolverChain.append(unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_Gear_LevelBonus").ValueResolverChain[0])
    unrealsdk.find_object("AttributeDefinition", "gd_Balance.LevelLimits.Proficiency_CombatRifle_LevelBonus").ValueResolverChain.pop(0)
    unrealsdk.find_object("AttributeDefinition", "d_attributes.Inventory.ShieldItemLevel").ContextResolverChain[0].InventoryDefinition = None
    unrealsdk.find_object("AttributePresentationDefinition", "gd_AttributePresentation.Skills_Mordecai.AttrPresent_SkillGradeModifier_Mordecai_BloodRage").Description = "Hair Trigger Skill"


def patch_volatile():

    #ItemPools
    unrealsdk.load_package("gd_itempools_Shop.Items.shoppool_FeaturedItem_WeaponMachine")
    unrealsdk.load_package("gd_itempools_Shop.Items.shoppool_Weapons_flatChance")

    unrealsdk.find_object("ItemPoolDefinition", "gd_itempools_Shop.Items.shoppool_FeaturedItem_WeaponMachine").BalancedItems.append(unrealsdk.find_object("ItemPoolDefinition", "gd_itempools_Shop.Items.shoppool_FeaturedItem_WeaponMachine").BalancedItems[5])
    unrealsdk.find_object("ItemPoolDefinition", "gd_itempools_Shop.Items.shoppool_FeaturedItem_WeaponMachine").BalancedItems[10].InvBalanceDefinition = unrealsdk.find_object("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_SupportMachineGun")
    unrealsdk.find_object("ItemPoolDefinition", "gd_itempools_Shop.Items.shoppool_Weapons_flatChance").BalancedItems.append(unrealsdk.find_object("ItemPoolDefinition", "gd_itempools_Shop.Items.shoppool_Weapons_flatChance").BalancedItems[5])
    unrealsdk.find_object("ItemPoolDefinition", "gd_itempools_Shop.Items.shoppool_Weapons_flatChance").BalancedItems[10].InvBalanceDefinition = unrealsdk.find_object("InventoryBalanceDefinition", "gd_itemgrades.Weapons.ItemGrade_Weapon_SupportMachineGun")

    # Enemies
    unrealsdk.load_package("gd_itempools.CrimsonLance.Infantry_Weapons")
    unrealsdk.load_package("gd_itempools.CrimsonLance.Infantry_Weapons_Badass")
    unrealsdk.load_package("dlc3_gd_itempools.CrimsonLance.Infantry_Weapons_Badass_enhance")


    unrealsdk.find_object("ItemPoolDefinition", "gd_itempools.CrimsonLance.Infantry_Weapons").BalancedItems[1].bDropOnDeath = True
    unrealsdk.find_object("ItemPoolDefinition", "gd_itempools.CrimsonLance.Infantry_Weapons_Badass").BalancedItems[0].bDropOnDeath = True
    unrealsdk.find_object("ItemPoolDefinition", "dlc3_gd_itempools.CrimsonLance.Infantry_Weapons_Badass_enhance").BalancedItems[0].bDropOnDeath = True


    """     unrealsdk.load_package("dlc3_gd_population_enemies.Drifters.DrifterSquad_Drifter")
    unrealsdk.load_package("dlc3_gd_balance_enemies.Drifters.Pawn_Balance_BadassDrifter")
    unrealsdk.load_package("gd_Balance.WeightingPlayerCount.Enemy_MajorUpgrade_PerPlayer")



    unrealsdk.find_object("PopulationDefinition", "dlc3_gd_population_enemies.Drifters.DrifterSquad_Drifter").ActorArchetypeList.append(unrealsdk.find_object("PopulationDefinition", "dlc3_gd_population_enemies.Drifters.DrifterSquad_Drifter").ActorArchetypeList[0])
    unrealsdk.find_object("PopulationDefinition", "dlc3_gd_population_enemies.Drifters.DrifterSquad_Drifter").ActorArchetypeList[1].SpawnFactory.PawnBalanceDefinition = unrealsdk.find_object("AIPawnBalanceDefinition", "dlc3_gd_balance_enemies.Drifters.Pawn_Balance_BadassDrifter")
    unrealsdk.find_object("PopulationDefinition", "dlc3_gd_population_enemies.Drifters.DrifterSquad_Drifter").ActorArchetypeList[1].Probability.BaseValueScaleConstant = 0.08
    unrealsdk.find_object("PopulationDefinition", "dlc3_gd_population_enemies.Drifters.DrifterSquad_Drifter").ActorArchetypeList[1].Probability.InitializationDefinition = unrealsdk.find_object("AttributeInitializationDefinition", "gd_Balance.WeightingPlayerCount.Enemy_MajorUpgrade_PerPlayer")
    """
    # Misc
    unrealsdk.load_package("gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive")
    unrealsdk.load_package("gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Explosive")
    unrealsdk.load_package("gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Incendiary")
    unrealsdk.load_package("gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Shock")
    unrealsdk.load_package("gd_balance_objects.FuelTanks.ObjectGrade_ExplodingFuelTank")
    unrealsdk.load_package("dlc3_gd_explosives.SeaMine.BalanceDef_SeaMine")


    unrealsdk.find_object("InteractiveObjectBalanceDefinition", "gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades.append(unrealsdk.find_object("InteractiveObjectBalanceDefinition", "gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[9])
    unrealsdk.find_object("InteractiveObjectBalanceDefinition", "gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[10].GameStageRequirement.MinGameStage = 53
    unrealsdk.find_object("InteractiveObjectBalanceDefinition", "gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[10].GameStageRequirement.MaxGameStage = 100
    unrealsdk.find_object("InteractiveObjectBalanceDefinition", "gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Explosive").Grades.append(unrealsdk.find_object("InteractiveObjectBalanceDefinition", "gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[10])
    unrealsdk.find_object("InteractiveObjectBalanceDefinition", "gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Incendiary").Grades.append(unrealsdk.find_object("InteractiveObjectBalanceDefinition", "gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[10])
    unrealsdk.find_object("InteractiveObjectBalanceDefinition", "gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Shock").Grades.append(unrealsdk.find_object("InteractiveObjectBalanceDefinition", "gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[10])
    unrealsdk.find_object("InteractiveObjectBalanceDefinition", "gd_balance_objects.FuelTanks.ObjectGrade_ExplodingFuelTank").Grades.append(unrealsdk.find_object("InteractiveObjectBalanceDefinition", "gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[10])
    unrealsdk.find_object("InteractiveObjectBalanceDefinition", "dlc3_gd_explosives.SeaMine.BalanceDef_SeaMine").Grades[5].GameStageRequirement.MaxGameStage = 100


patch()


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
    global bPatched
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



# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]

build_mod(
    # These are defaulted
    # inject_version_from_pyproject=True, # This is True by default
    # version_info_parser=lambda v: tuple(int(x) for x in v.split(".")),
    # deregister_same_settings=True,      # This is True by default
    keybinds=[],
    hooks=[on_level_loaded, on_commit_map_change],
    commands=[],
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/Unofficial_Patch.json"),
)

logging.info(f"Unofficial Patch Loaded: {__version__}, {__version_info__}")
