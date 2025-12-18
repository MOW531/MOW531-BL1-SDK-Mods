import unrealsdk

from pathlib import Path
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook, get_pc, SETTINGS_DIR, build_mod, ENGINE
from mods_base.options import BaseOption, BoolOption
from unrealsdk import logging

bPatched = False
current_obj = None

struct = unrealsdk.make_struct
wclass = unrealsdk.find_class


def obj (definition:str, object:str):
    global current_obj
    object_class = unrealsdk.find_class(definition)
    current_obj = ENGINE.DynamicLoadObject(object, object_class, False)
    current_obj.ObjectFlags |= 0x4000
    return current_obj

def make_weightdata(part, BaseValueConstant, BaseValueAttribute, InitializationDefinition, BaseValueScaleConstant):
    WeightData = struct("PartGradeWeightData", Part=part)
    WeightData.MinGameStage.BaseValueConstant = 1
    WeightData.MinGameStage.BaseValueScaleConstant = 1
    WeightData.MaxGameStage.BaseValueConstant = 100
    WeightData.MaxGameStage.BaseValueScaleConstant = 1
    WeightData.DefaultWeight.BaseValueConstant = BaseValueConstant
    WeightData.DefaultWeight.BaseValueAttribute = BaseValueAttribute
    WeightData.DefaultWeight.InitializationDefinition = InitializationDefinition
    WeightData.DefaultWeight.BaseValueScaleConstant = BaseValueScaleConstant
    return WeightData


def patch():

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
    obj("WeaponNamePartDefinition","gd_weap_combat_shotgun.Prefix.Prefix_Firerate1_Riot").Priority = 2.3
    obj("WeaponNamePartDefinition","gd_weap_repeater_pistol.Prefix.Prefix_Nasty").Expressions[1].AttributeOperand1 = obj("AttributeDefinition","d_attributes.Weapon.WeaponDamageNormalized")
    obj("WeaponNamePartDefinition","gd_weap_combat_shotgun.Prefix.Prefix_Acc1_Jagged").PartName = "Jagged"


    # Weapon parts

    DestroyerPresentation = unrealsdk.construct_object("AttributePresentationDefinition",obj("WeaponPartDefinition","gd_weap_combat_rifle.Barrel.barrel5_Hyperion_Destroyer"))
    DestroyerPresentation.Description = "Burst Fire while zoomed."
    DestroyerPresentation.bDontDisplayNumber = True
    DestroyerPresentation.Attribute = obj("AttributeDefinition","d_attributes.Weapon.WeaponAutomaticBurstCount")
    DestroyerPresentation.BasePriority = 3

    InvaderPresentation = unrealsdk.construct_object("AttributePresentationDefinition",obj("WeaponPartDefinition","gd_weap_repeater_pistol.Sight.sight5_Hyperion_Invader"))
    InvaderPresentation.Description = "Burst Fire while zoomed."
    InvaderPresentation.bDontDisplayNumber = True
    InvaderPresentation.Attribute = obj("AttributeDefinition","d_attributes.Weapon.WeaponAutomaticBurstCount")
    InvaderPresentation.BasePriority = 3

    RevolverCritPresentation = unrealsdk.construct_object("AttributePresentationDefinition",obj("WeaponTypeDefinition","gd_weap_revolver_pistol.A_Weapon.WeaponType_revolver_pistol"))
    RevolverCritPresentation.Description = "Critical Hit Damage"
    RevolverCritPresentation.RoundingMode = 0
    RevolverCritPresentation.Attribute = obj("AttributeDefinition","d_attributes.GameplayAttributes.PlayerCriticalHitBonus")
    RevolverCritPresentation.BasePriority = 1
    
    AthenasWisdomCritPresentation = unrealsdk.construct_object("AttributePresentationDefinition",obj("WeaponPartDefinition","dlc3_gd_weap_UniqueParts.RepeaterPistol.barrel5_AthenasWisdom"))
    AthenasWisdomCritPresentation.Description = "Critical Hit Damage"
    AthenasWisdomCritPresentation.RoundingMode = 0
    AthenasWisdomCritPresentation.Attribute = obj("AttributeDefinition","d_attributes.GameplayAttributes.PlayerCriticalHitBonus")
    AthenasWisdomCritPresentation.BasePriority = 1

    KromsSidearmPresentation = unrealsdk.construct_object("AttributePresentationDefinition",obj("WeaponPartDefinition","gd_weap_repeater_pistol.UniqueParts.KromsSidearm_barrel5"))
    KromsSidearmPresentation.Description = "Burst Fire while zoomed."
    KromsSidearmPresentation.bDontDisplayNumber = True
    KromsSidearmPresentation.Attribute = obj("AttributeDefinition","d_attributes.Weapon.WeaponAutomaticBurstCount")
    KromsSidearmPresentation.BasePriority = 3


    FangedWeightData = struct("PartGradeWeightData", Part=obj("WeaponPartDefinition","gd_weap_repeater_pistol.acc.acc1_Fanged"))
    FangedWeightData.MinGameStage.BaseValueConstant = 1
    FangedWeightData.MinGameStage.BaseValueScaleConstant = 1
    FangedWeightData.MaxGameStage.BaseValueConstant = 100
    FangedWeightData.MaxGameStage.BaseValueScaleConstant = 1

    obj("WeaponPartDefinition","gd_weap_support_machinegun.acc.acc4_SandS_Draco_Incendiary").TitleList.append(obj("WeaponNamePartDefinition","gd_weap_support_machinegun.Title.TitleM_SandS_Draco"))
    obj("WeaponPartListDefinition","gd_weap_assault_shotgun.acc.Acc_PartList").WeightedParts[7].DefaultWeight.BaseValueScaleConstant = 1
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
    obj("WeaponPartDefinition","gd_weap_combat_rifle.UniqueParts.Sentinel_sight4").WeaponCardAttributes.append(obj("WeaponPartDefinition","gd_weap_combat_rifle.Sight.sight4").WeaponCardAttributes[0])
    obj("WeaponPartDefinition","gd_weap_combat_rifle.Barrel.barrel5_Hyperion_Destroyer").CustomPresentations.append(DestroyerPresentation)
    obj("WeaponTypeDefinition","gd_weap_revolver_pistol.A_Weapon.WeaponType_revolver_pistol").CustomPresentations.append(RevolverCritPresentation)
    obj("WeaponPartDefinition","gd_weap_sniper_rifle_semiauto.UniqueParts.ReaversEdge_sight4").WeaponCardAttributes.append(obj("WeaponPartDefinition","gd_weap_sniper_rifle.Sight.sight4").WeaponCardAttributes[0])
    obj("WeaponPartDefinition","dlc3_gd_weap_UniqueParts.CombatRifle.TedioreAvenger_sight5").WeaponCardAttributes.append(obj("WeaponPartDefinition","gd_weap_combat_shotgun.Body.body3_Tediore_Defender").WeaponCardAttributes[0])
    obj("WeaponPartDefinition","dlc3_gd_weap_UniqueParts.RepeaterPistol.barrel5_AthenasWisdom").CustomPresentations.append(AthenasWisdomCritPresentation)
    obj("WeaponPartDefinition","gd_weap_revolver_pistol.Barrel.barrel5_Jakobs_Unforgiven").WeaponCardAttributes.pop(0)
    obj("WeaponPartDefinition","gd_weap_repeater_pistol.Sight.sight5_Hyperion_Invader").CustomPresentations.append(InvaderPresentation)
    obj("WeaponTypeDefinition","gd_weap_combat_shotgun.A_Weapon.WeaponType_combat_shotgun").PrefixList.pop(6)
    obj("WeaponPartDefinition","gd_weap_combat_shotgun.Grip.grip2").PrefixList.pop(0)
    obj("WeaponPartDefinition","gd_weap_combat_shotgun.Grip.grip2a_Torgue").PrefixList.pop(0)
    obj("WeaponPartListDefinition","gd_weap_revolver_pistol.Body.Body_PartList").WeightedParts[5].Manufacturers[0].DefaultWeight.InitializationDefinition = obj("AttributeInitializationDefinition","gd_Balance.Weighting.Weight_Awesome_6_Legendary")
    obj("WeaponPartListDefinition","gd_weap_assault_shotgun.acc.Acc_PartList").WeightedParts[7].DefaultWeight.InitializationDefinition = obj("AttributeInitializationDefinition","gd_Balance.Weighting.Weight_Awesome_3_Uncommoner")
    obj("WeaponPartDefinition","gd_weap_repeater_pistol.UniqueParts.KromsSidearm_barrel5").CustomPresentations.append(KromsSidearmPresentation)
    obj("AttributePresentationDefinition","gd_weap_repeater_pistol.Title.TitleU_Krom_KromsSidearm:AttributePresentationDefinition_6").NoConstraintText = "A gift from Papa Krom"
    obj("WeaponPartListCollectionDefinition","gd_customweapons.PartCollections.PartCollection_EridanCannon_MegaCannon").PartReplacementMode = 1
    obj("WeaponPartListCollectionDefinition","gd_customweapons.PartCollections.PartCollection_EridanCannon_MegaCannon").BarrelPartData.bEnabled = True
    obj("WeaponPartListCollectionDefinition","gd_customweapons.PartCollections.PartCollection_EridanCannon_MegaCannon").BarrelPartData.WeightedParts.append(make_weightdata(obj("WeaponPartDefinition","gd_weap_alien_rifle.Barrel.barrel5_MegaCannon"), 0, None, None, 1))
    #obj("ItemPoolDefinition","gd_itempools.Level50Pools.Slither_TheDove").BalancedItems[0].InvBalanceDefinition = obj("InventoryBalanceDefinition","UP_Assets.Retail_Weapons.CustomWeap_repeater_TheDove")
    #obj("ItemPoolDefinition","gd_itempools.WeaponPools.Weapons_Retail").BalancedItems[2].InvBalanceDefinition = obj("InventoryBalanceDefinition","UP_Assets.Retail_Weapons.CustomWeap_repeater_TheDove")



    # This is to fix the crit boost that some weapons get with the main critfix

    obj("WeaponTypeDefinition","gd_weap_sniper_rifle.A_Weapon.WeaponType_sniper_rifle").ExternalAttributeEffects.append(struct("AttributeEffectData", AttributeToModify=obj("AttributeDefinition","d_attributes.GameplayAttributes.PlayerCriticalHitBonus"), ModifierType=1, BaseModifierValue=struct("AttributeInitializationData", BaseValueConstant=-1.0000000, BaseValueAttribute=None, InitializationDefinition=None, BaseValueScaleConstant=1.0000000)))
    obj("WeaponTypeDefinition","gd_weap_sniper_rifle.A_Weapon.WeaponType_sniper_rifle").ExternalAttributeEffects.append(struct("AttributeEffectData", AttributeToModify=obj("AttributeDefinition","d_attributes.GameplayAttributes.PlayerCriticalHitBonus"), ModifierType=2, BaseModifierValue=struct("AttributeInitializationData", BaseValueConstant=1.0000000, BaseValueAttribute=None, InitializationDefinition=None, BaseValueScaleConstant=1.0000000)))

    obj("WeaponTypeDefinition","gd_weap_sniper_rifle_semiauto.A_Weapon.WeaponType_sniper_rifle_semiauto").ExternalAttributeEffects.append(struct("AttributeEffectData", AttributeToModify=obj("AttributeDefinition","d_attributes.GameplayAttributes.PlayerCriticalHitBonus"), ModifierType=1, BaseModifierValue=struct("AttributeInitializationData", BaseValueConstant=-1.0000000, BaseValueAttribute=None, InitializationDefinition=None, BaseValueScaleConstant=1.0000000)))
    obj("WeaponTypeDefinition","gd_weap_sniper_rifle_semiauto.A_Weapon.WeaponType_sniper_rifle_semiauto").ExternalAttributeEffects.append(struct("AttributeEffectData", AttributeToModify=obj("AttributeDefinition","d_attributes.GameplayAttributes.PlayerCriticalHitBonus"), ModifierType=2, BaseModifierValue=struct("AttributeInitializationData", BaseValueConstant=1.0000000, BaseValueAttribute=None, InitializationDefinition=None, BaseValueScaleConstant=1.0000000)))

    obj("WeaponTypeDefinition","gd_weap_revolver_pistol.A_Weapon.WeaponType_revolver_pistol").ExternalAttributeEffects.append(struct("AttributeEffectData", AttributeToModify=obj("AttributeDefinition","d_attributes.GameplayAttributes.PlayerCriticalHitBonus"), ModifierType=1, BaseModifierValue=struct("AttributeInitializationData", BaseValueConstant=-1.0000000, BaseValueAttribute=None, InitializationDefinition=None, BaseValueScaleConstant=1.0000000)))
    obj("WeaponTypeDefinition","gd_weap_revolver_pistol.A_Weapon.WeaponType_revolver_pistol").ExternalAttributeEffects.append(struct("AttributeEffectData", AttributeToModify=obj("AttributeDefinition","d_attributes.GameplayAttributes.PlayerCriticalHitBonus"), ModifierType=2, BaseModifierValue=struct("AttributeInitializationData", BaseValueConstant=1.0000000, BaseValueAttribute=None, InitializationDefinition=None, BaseValueScaleConstant=1.0000000)))

    obj("WeaponPartDefinition","gd_weap_combat_rifle.acc.acc2_Intense").ExternalAttributeEffects.append(struct("AttributeEffectData", AttributeToModify=obj("AttributeDefinition","d_attributes.GameplayAttributes.PlayerCriticalHitBonus"), ModifierType=1, BaseModifierValue=struct("AttributeInitializationData", BaseValueConstant=-1.0000000, BaseValueAttribute=None, InitializationDefinition=None, BaseValueScaleConstant=1.0000000)))
    obj("WeaponPartDefinition","gd_weap_combat_rifle.acc.acc2_Intense").ExternalAttributeEffects.append(struct("AttributeEffectData", AttributeToModify=obj("AttributeDefinition","d_attributes.GameplayAttributes.PlayerCriticalHitBonus"), ModifierType=2, BaseModifierValue=struct("AttributeInitializationData", BaseValueConstant=1.0000000, BaseValueAttribute=None, InitializationDefinition=None, BaseValueScaleConstant=1.0000000)))


    # Shields
    

    SuperBoosterLine1 = unrealsdk.construct_object("AttributePresentationDefinition",obj("ItemPartDefinition","gd_shields.UniqueParts.Shield_WeeWee_Material"))
    SuperBoosterLine1.NoConstraintText = "Health Boost 15%"
    SuperBoosterLine1.bDontDisplayNumber = True
    SuperBoosterLine1.BasePriority = 2
    SuperBoosterLine2 = unrealsdk.construct_object("AttributePresentationDefinition",obj("ItemPartDefinition","gd_shields.UniqueParts.Shield_WeeWee_Material"))
    SuperBoosterLine2.NoConstraintText = "Very quick Health Regeneration!"
    SuperBoosterLine2.bDontDisplayNumber = True
    SuperBoosterLine2.BasePriority = 1

    #unrealsdk.load_package("UP_Assets.UniqueParts.Shield_WeeWee_Material")
    obj("ItemPartDefinition","gd_shields.UniqueParts.Shield_WeeWee_Material").CustomPresentations.append(SuperBoosterLine1)
    obj("ItemPartDefinition","gd_shields.UniqueParts.Shield_WeeWee_Material").CustomPresentations.append(SuperBoosterLine2)

    # Skills

        # Brick
    obj("SkillDefinition","gd_Skills2_Brick.Blaster.RapidReload").SkillEffectDefinitions[1].BaseModifierValue.BaseValueConstant = -0.06
    obj("SkillDefinition","gd_Skills2_Brick.Blaster.RapidReload").SkillEffectDefinitions[1].PerGradeUpgrade.BaseValueConstant = -0.06
    obj("SkillDefinition","gd_Skills2_Brick.Tank.Unbreakable").bAvailableBerserk = True
    obj("SkillDefinition","gd_Skills2_Brick.Tank.Unbreakable").bAvailableDuringActionSkill = True

        # Lilith
    obj("SkillDefinition","gd_Skills2_Lilith.Controller.GirlPower").bAvailableAlways = True
    obj("SkillDefinition","gd_Skills2_Lilith.Elemental.Resilience").SkillEffectDefinitions.append(current_obj.SkillEffectDefinitions[5])
    obj("SkillDefinition","gd_Skills2_Lilith.Elemental.Resilience").SkillEffectDefinitions[(len(current_obj.SkillEffectDefinitions)) - 1].AttributeToModify = obj("AttributeDefinition","d_attributes.DamageTypeModifers.ShockPassiveDamageModifier")
    obj("AttributeInitializationDefinition","gd_Skills2_Lilith.MiscData.GirlPower_ShieldRegenRate").ValueFormula.Multiplier.BaseValueScaleConstant = 0.015

        # Roland
    obj("AttributeInitializationDefinition","gd_skills2_Roland.MiscData.QuickCharge_Init").ValueFormula.Level.BaseValueAttribute = obj("AttributeDefinition","gd_skills2_Roland.SkillGradeModifiers.SkillGradeModifier_Roland_QuickCharge")
    obj("AttributeInitializationDefinition","gd_skills2_Roland.MiscData.QuickCharge_Init").ValueFormula.Multiplier.BaseValueAttribute = obj("ResourcePoolAttributeDefinition","d_attributes.ShieldResourcePool.ShieldMaxValue")
    obj("AttributeInitializationDefinition","gd_skills2_Roland.MiscData.QuickCharge_Init").ValueFormula.Multiplier.BaseValueScaleConstant = 0.015


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
    obj("ItemPartDefinition","gd_CommandDecks.Body_Brick.Brick_Warmonger").AttributeSlotEffects[0].ConstraintAttribute = obj("AttributeDefinition","UP_Assets.Presentations.ATT_TeamConstraint_Weapon")

        # Lilith
    obj("ItemPartDefinition","gd_CommandDecks.Body_Lilith.Lilith_Catalyst").AttributeSlotEffects[1].AttributeToModify = obj("ResourcePoolAttributeDefinition","d_attributes.ShieldResourcePool.ShieldOnIdleRegenerationRate")


    #Projectiles

    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Helix").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.rocket_Leviathan").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Medium").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Medium_Mongol").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Medium_Nidhogg").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Medium_Rhino").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.rocket_mini").bUseAccurateCollision = False
    obj("ProjectileDefinition","gd_weap_combat_shotgun.Rockets.rocket_mini").bUseAccurateCollision = False

    obj("WeaponTypeDefinition","gd_weap_rocket_launcher.A_Weapon.WeaponType_rocket_launcher").InstantHitDamageType = wclass("WillowDmgSource_Rocket")


    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rhino_Exploder").DefaultBehaviorSet.OnExplode[0].DamageSource = wclass("WillowDmgSource_Rocket")
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Helix").DefaultBehaviorSet.OnExplode[0].DamageSource = wclass("WillowDmgSource_Rocket")
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Large_Redemption").DefaultBehaviorSet.OnExplode[0].DamageSource = wclass("WillowDmgSource_Rocket")
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.rocket_Leviathan").DefaultBehaviorSet.OnExplode[0].DamageSource = wclass("WillowDmgSource_Rocket")
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Medium").DefaultBehaviorSet.OnExplode[0].DamageSource = wclass("WillowDmgSource_Rocket")
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Medium_Mongol").DefaultBehaviorSet.OnExplode[0].DamageSource = wclass("WillowDmgSource_Rocket")
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Medium_Nidhogg").DefaultBehaviorSet.OnExplode[0].DamageSource = wclass("WillowDmgSource_Rocket")
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.Rocket_Medium_Rhino").DefaultBehaviorSet.OnExplode[0].DamageSource = wclass("WillowDmgSource_Rocket")
    obj("ProjectileDefinition","gd_weap_rocket_launcher.Rockets.rocket_mini").DefaultBehaviorSet.OnExplode[0].DamageSource = wclass("WillowDmgSource_Rocket")
    obj("ProjectileDefinition","gd_weap_combat_shotgun.Rockets.rocket_mini").DefaultBehaviorSet.OnExplode[0].DamageSource = wclass("WillowDmgSource_Rocket")


    # Missions
    #obj("MissionDefinition","Z1_Missions.Missions.M_HeathensGodlessMonsters").ItemRewards = (obj("InventoryBalanceDefinition","UP_Assets.Retail_Weapons.CustomWeap_repeater_TheDove"), None, None, None, None)
    obj("MissionDefinition","I1_Missions.Missions.M_Powerlines").bPlotCritical = True
    obj("MissionDefinition","dlc3_CircleMissions.MainMissions.M_dlc3_Circle_Wave3").MissionDescription = "You're moving up the ranks. Time to really put you to the test. When you are ready, enter the center of the red Crimson Lance logo. I hope you've been training."

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

    obj("AttributePresentationListDefinition","gd_AttributePresentation._AttributeList.DefaultPresentationList").Attributes.append(obj("AttributePresentationDefinition","UP_Assets.Presentations.AttrPresent_Weapon_Is_Atlas"))
    obj("AttributePresentationListDefinition","gd_AttributePresentation._AttributeList.DefaultPresentationList").Attributes.append(obj("AttributePresentationDefinition","UP_Assets.Presentations.AttrPresent_Weapon_Is_Dahl"))
    obj("AttributePresentationListDefinition","gd_AttributePresentation._AttributeList.DefaultPresentationList").Attributes.append(obj("AttributePresentationDefinition","UP_Assets.Presentations.AttrPresent_Weapon_Is_Eridian"))
    obj("AttributePresentationListDefinition","gd_AttributePresentation._AttributeList.DefaultPresentationList").Attributes.append(obj("AttributePresentationDefinition","UP_Assets.Presentations.AttrPresent_Weapon_Is_Gearbox"))
    obj("AttributePresentationListDefinition","gd_AttributePresentation._AttributeList.DefaultPresentationList").Attributes.append(obj("AttributePresentationDefinition","UP_Assets.Presentations.AttrPresent_Weapon_Is_Hyperion"))
    obj("AttributePresentationListDefinition","gd_AttributePresentation._AttributeList.DefaultPresentationList").Attributes.append(obj("AttributePresentationDefinition","UP_Assets.Presentations.AttrPresent_Weapon_Is_Jakobs"))
    obj("AttributePresentationListDefinition","gd_AttributePresentation._AttributeList.DefaultPresentationList").Attributes.append(obj("AttributePresentationDefinition","UP_Assets.Presentations.AttrPresent_Weapon_Is_Maliwan"))
    obj("AttributePresentationListDefinition","gd_AttributePresentation._AttributeList.DefaultPresentationList").Attributes.append(obj("AttributePresentationDefinition","UP_Assets.Presentations.AttrPresent_Weapon_Is_SandS"))
    obj("AttributePresentationListDefinition","gd_AttributePresentation._AttributeList.DefaultPresentationList").Attributes.append(obj("AttributePresentationDefinition","UP_Assets.Presentations.AttrPresent_Weapon_Is_Tediore"))
    obj("AttributePresentationListDefinition","gd_AttributePresentation._AttributeList.DefaultPresentationList").Attributes.append(obj("AttributePresentationDefinition","UP_Assets.Presentations.AttrPresent_Weapon_Is_Torgue"))
    obj("AttributePresentationListDefinition","gd_AttributePresentation._AttributeList.DefaultPresentationList").Attributes.append(obj("AttributePresentationDefinition","UP_Assets.Presentations.AttrPresent_Weapon_Is_Vladof"))
    obj("AttributePresentationListDefinition","gd_AttributePresentation._AttributeList.DefaultPresentationList").Attributes.append(obj("AttributePresentationDefinition","UP_Assets.Presentations.AttrPresent_ATT_TeamConstraint_Weapon"))


    # Descriptions

        # Skills
        
            # Roland
    obj("SkillDefinition","gd_skills2_Roland.Action.A_DeployScorpio").SkillEffectPresentations[0].Description = "Cooldown: $NUMBER$ seconds."

    obj("SkillDefinition","gd_skills2_Roland.Support.Impact").SkillEffectPresentations[0].Description = "Bullet Damage."
    obj("SkillDefinition","gd_skills2_Roland.Infantry.Sentry").SkillEffectPresentations[0].Description = "Scorpio Turret Damage."
    obj("SkillDefinition","gd_skills2_Roland.Support.Defense").SkillEffectPresentations[0].Description = "Shield Recharge Speed."
    obj("SkillDefinition","gd_skills2_Roland.Support.Defense").SkillDescription = "Increases how quickly your shield recharges."
    obj("SkillDefinition","gd_skills2_Roland.Support.Stockpile").SkillDescription = "Allies near the Scorpio Turret regenerate ammo for the weapon currently in their hands."
    obj("SkillDefinition","gd_skills2_Roland.Support.Stockpile").SkillEffectPresentations[0].Description = "Ammo Regeneration Rate."
    obj("SkillDefinition","gd_skills2_Roland.Medic.Fitness").SkillEffectPresentations[0].Description = "Maximum Health."
    obj("SkillDefinition","gd_skills2_Roland.Medic.AidStation").SkillEffectPresentations[0].bDontDisplayPlusSign = True
    obj("SkillDefinition","gd_skills2_Roland.Medic.AidStation").SkillEffectPresentations[0].Description = "Regenerates $NUMBER$ of your Health per second."
    obj("SkillDefinition","gd_skills2_Roland.Infantry.Scattershot").SkillDescription = "Increases Shotgun Damage and decreases Spread."
    obj("SkillDefinition","gd_skills2_Roland.Infantry.Scattershot").SkillEffectPresentations[0].Description = "Shotgun Damage."
    obj("SkillDefinition","gd_skills2_Roland.Infantry.Scattershot").SkillEffectPresentations[1].Description = "Shotgun Spread."
    obj("SkillDefinition","gd_skills2_Roland.Infantry.MetalStorm").SkillEffectPresentations[0].Description = "Fire Rate."
    obj("SkillDefinition","gd_skills2_Roland.Infantry.MetalStorm").SkillEffectPresentations[1].Description = "Recoil Reduction."
    obj("SkillDefinition","gd_skills2_Roland.Support.QuickCharge").SkillEffectPresentations[0].Description = "Regenerates $NUMBER$ of your Shield per second."
    obj("SkillDefinition","gd_skills2_Roland.Support.QuickCharge").SkillEffectPresentations[0].bDontDisplayPlusSign = True
    obj("SkillDefinition","gd_skills2_Roland.Support.QuickCharge").SkillEffectPresentations[0].bUseCustomNumberPlacement = True
    obj("SkillDefinition","gd_skills2_Roland.Support.QuickCharge").SkillEffectPresentations[0].RoundingMode = 0
    obj("SkillDefinition","gd_skills2_Roland.Support.QuickCharge").SkillDescription = "Killing an enemy causes your shield to quickly regenerate for a few seconds."
    obj("SkillDefinition","gd_skills2_Roland.Support.Barrage").SkillEffectPresentations[0].Description = "Shots fired per burst."
    obj("SkillDefinition","gd_skills2_Roland.Medic.Overload").SkillDescription = "Increases the Magazine Size of all weapon types."
    obj("SkillDefinition","gd_skills2_Roland.Medic.Overload").SkillEffectPresentations[0].Description = "Magazine Size."
    obj("SkillDefinition","gd_skills2_Roland.Medic.Cauterize").SkillEffectPresentations[0].bDontDisplayPlusSign = True
    obj("SkillDefinition","gd_skills2_Roland.Medic.Cauterize").SkillDescription = "Shooting an ally heals them.  This effect also works with grenades and rockets."
    obj("SkillDefinition","gd_skills2_Roland.Medic.Cauterize").SkillEffectPresentations[0].Description = "Converts $NUMBER$ of damage to health."
    obj("SkillDefinition","gd_skills2_Roland.Infantry.Refire").SkillEffectPresentations[0].Description = "Cooldown reduction per hit: $NUMBER$ (in seconds)."
    obj("SkillDefinition","gd_skills2_Roland.Infantry.Assault").SkillDescription = "Increases Magazine Size and reduces Recoil with Combat Rifles and Support Machine guns."
    obj("SkillDefinition","gd_skills2_Roland.Infantry.Assault").SkillEffectPresentations[0].Description = "Magazine Size and Recoil Reduction."
    obj("SkillDefinition","gd_skills2_Roland.Support.Grenadier").SkillDescription = "Killing an enemy increases your Grenade Damage and causes you to regenerate grenades for a few seconds."
    obj("SkillDefinition","gd_skills2_Roland.Support.Grenadier").SkillEffectPresentations[0].Description = "Grenades per minute."
    obj("SkillDefinition","gd_skills2_Roland.Support.Grenadier").SkillEffectPresentations[1].Description = "Grenade Damage."
    obj("SkillDefinition","gd_skills2_Roland.Support.deploy").SkillDescription = "Reduces the Cooldown of your Scorpio Turret."
    obj("SkillDefinition","gd_skills2_Roland.Support.deploy").SkillEffectPresentations[0].Description = "Cooldown reduction."
    obj("SkillDefinition","gd_skills2_Roland.Support.deploy").SkillEffectPresentations[0].bUseCustomNumberPlacement = False
    obj("SkillDefinition","gd_skills2_Roland.Medic.Revive").SkillDescription = "The Scorpio Turret has a chance to instantly revive nearby crippled allies when deployed."
    obj("SkillDefinition","gd_skills2_Roland.Medic.Revive").SkillEffectPresentations[0].Description = "Revival Chance."
    obj("SkillDefinition","gd_skills2_Roland.Medic.Grit").SkillEffectPresentations[0].Description = "Bullet Resistance."
    obj("SkillDefinition","gd_skills2_Roland.Support.SupplyDrop").SkillEffectPresentations[0].Description = "Supply drop every $NUMBER$ seconds."
    obj("SkillDefinition","gd_skills2_Roland.Medic.Stat").SkillDescription = "Killing an enemy causes your and nearby allies health to quickly regenerate for a few seconds."
    obj("SkillDefinition","gd_skills2_Roland.Medic.Stat").SkillEffectPresentations[0].Description = "Regenerates $NUMBER$ health per second."
    obj("SkillDefinition","gd_skills2_Roland.Medic.Stat").SkillEffectPresentations[0].bDontDisplayPlusSign = True

            # Lilith
    obj("SkillDefinition","gd_Skills2_Lilith.Action.A_PhaseWalk").SkillEffectPresentations[0].Description = "Cooldown: $NUMBER$ seconds."

    obj("SkillDefinition","gd_Skills2_Lilith.Controller.Diva").SkillDescription = "Increases your Shield Capacity."
    obj("SkillDefinition","gd_Skills2_Lilith.Controller.Diva").SkillEffectPresentations[0].Description = "Shield Capacity."
    obj("SkillDefinition","gd_Skills2_Lilith.Controller.Diva").SkillEffectPresentations[0].bUseCustomNumberPlacement = False
    obj("SkillDefinition","gd_Skills2_Lilith.Controller.Striking").SkillEffectPresentations[0].Description = "Chance to Daze (vs an equal level enemy)."
    obj("SkillDefinition","gd_Skills2_Lilith.Controller.Striking").SkillEffectPresentations[0].bUseCustomNumberPlacement = False
    obj("SkillDefinition","gd_Skills2_Lilith.Assassin.SilentResolve").SkillDescription = "Increases your Damage Resistance for a few seconds after Phasewalking."
    obj("SkillDefinition","gd_Skills2_Lilith.Controller.InnerGlow").SkillEffectPresentations[0].bDontDisplayPlusSign = True
    obj("SkillDefinition","gd_Skills2_Lilith.Controller.DramaticEntrance").SkillEffectPresentations[0].Description = "Chance to Daze (vs an enemy of equal level)."
    obj("SkillDefinition","gd_Skills2_Lilith.Controller.DramaticEntrance").SkillEffectPresentations[0].bUseCustomNumberPlacement = False
    obj("SkillDefinition","gd_Skills2_Lilith.Elemental.Resilience").SkillEffectPresentations[0].Description = "Elemental Resistance."
    obj("SkillDefinition","gd_Skills2_Lilith.Elemental.Resilience").SkillEffectPresentations[0].bUseCustomNumberPlacement = False
    obj("SkillDefinition","gd_Skills2_Lilith.Elemental.Radiance").SkillEffectPresentations[0].Description = "Shock Damage."
    obj("SkillDefinition","gd_Skills2_Lilith.Elemental.Radiance").SkillEffectPresentations[0].bUseCustomNumberPlacement = False
    obj("SkillDefinition","gd_Skills2_Lilith.Assassin.Enforcer").SkillDescription = "Killing an enemy increases your Accuracy and Bullet Damage for a few seconds."
    obj("SkillDefinition","gd_Skills2_Lilith.Assassin.HitAndRun").SkillDescription = "Gain increased Melee Damage and Phasewalk duration."
    obj("SkillDefinition","gd_Skills2_Lilith.Assassin.HitAndRun").SkillEffectPresentations[1].Description = "Phasewalk duration (in seconds)."
    obj("SkillDefinition","gd_Skills2_Lilith.Elemental.Intuition").SkillDescription = "Killing an enemy increases your Movement Speed and the experience you and your team earn for a few seconds."
    obj("SkillDefinition","gd_Skills2_Lilith.Assassin.Blackout").SkillEffectPresentations[0].Description = "Cooldown reduction per kill: $NUMBER$ seconds."
    obj("SkillDefinition","gd_Skills2_Lilith.Controller.MindGames").SkillEffectPresentations[0].Description = "Chance to Daze (vs an equal level enemy)."
    obj("SkillDefinition","gd_Skills2_Lilith.Controller.MindGames").SkillEffectPresentations[0].bUseCustomNumberPlacement = False
    obj("SkillDefinition","gd_Skills2_Lilith.Elemental.Phoenix").SkillEffectPresentations[1].Description = "Fire Damage."
    obj("SkillDefinition","gd_Skills2_Lilith.Elemental.Phoenix").SkillEffectPresentations[1].bUseCustomNumberPlacement = False

            # Brick
    obj("SkillDefinition","gd_Skills2_Brick.Action.A_Berserk").SkillEffectPresentations[0].Description = "Cooldown: $NUMBER$ seconds."

    obj("SkillDefinition","gd_Skills2_Brick.Brawler.IronFist").SkillDescription = "Increases the Melee Damage you deal."
    obj("SkillDefinition","gd_Skills2_Brick.Tank.Hardened").SkillDescription = "Increases your Maximum Health."
    obj("SkillDefinition","gd_Skills2_Brick.Brawler.StingLikeaBee").SkillEffectPresentations[0].Description = "Dash Distance: $NUMBER$ feet."
    obj("SkillDefinition","gd_Skills2_Brick.Brawler.HeavyHanded").SkillDescription = "Killing an enemy greatly increases your Melee Damage for a few seconds."
    obj("SkillDefinition","gd_Skills2_Brick.Tank.Bash").SkillEffectPresentations[0].Description = "Chance to Daze."
    obj("SkillDefinition","gd_Skills2_Brick.Tank.Bash").SkillEffectPresentations[0].bUseCustomNumberPlacement = False
    obj("SkillDefinition","gd_Skills2_Brick.Blaster.Revenge").SkillDescription = "Killing an enemy increases your Damage with all weapons for a few seconds."
    obj("SkillDefinition","gd_Skills2_Brick.Brawler.ShortFuse").SkillDescription = "Reduces the Cooldown of Berserk."
    obj("SkillDefinition","gd_Skills2_Brick.Tank.PayBack").SkillDescription = "After your shields become depleted you gain a Damage bonus for 10 seconds."
    obj("SkillDefinition","gd_Skills2_Brick.Blaster.Liquidate").SkillEffectPresentations[0].Description = "Cooldown reduction per hit: $NUMBER$ (in seconds)."
    obj("SkillDefinition","gd_Skills2_Brick.Blaster.CastIron").SkillDescription = "Increases your Resistance to Explosive Damage."

            # Mordecai
    obj("SkillDefinition","gd_skills2_Mordecai.Action.A_LaunchBloodwing").SkillEffectPresentations[0].Description = "Cooldown: $NUMBER$ seconds."

    obj("SkillDefinition","gd_skills2_Mordecai.Sniper.Focus").SkillDescription = "Increases Accuracy with all weapon types."
    obj("SkillDefinition","gd_skills2_Mordecai.Sniper.Focus").SkillEffectPresentations[1].Description = "Sniper Rifle sway."
    obj("SkillDefinition","gd_skills2_Mordecai.Sniper.Focus").SkillEffectPresentations[1].bUseCustomNumberPlacement = False
    obj("SkillDefinition","gd_skills2_Mordecai.Sniper.Caliber").SkillDescription = "Increases Damage with Sniper Rifles."
    obj("SkillDefinition","gd_skills2_Mordecai.Rogue.SwiftStrike").SkillDescription = "Increases Bloodwing Damage and Speed."
    obj("SkillDefinition","gd_skills2_Mordecai.Rogue.SwiftStrike").SkillEffectPresentations[0].Description = "Bloodwing Damage."
    obj("SkillDefinition","gd_skills2_Mordecai.Rogue.SwiftStrike").SkillEffectPresentations[1].Description = "Bloodwing Speed."
    obj("SkillDefinition","gd_skills2_Mordecai.Rogue.Swipe").SkillDescription = "Bloodwing causes enemies to drop additional money, ammo, and healing items when he attacks."
    obj("SkillDefinition","gd_skills2_Mordecai.Rogue.Swipe").SkillEffectPresentations[0].Description = "Maximum number of additional items dropped: $NUMBER$."
    obj("SkillDefinition","gd_skills2_Mordecai.Sniper.Killer").SkillEffectPresentations[0].Description = "Damage."
    obj("SkillDefinition","gd_skills2_Mordecai.Sniper.Killer").SkillEffectPresentations[0].bUseCustomNumberPlacement = False
    obj("SkillDefinition","gd_skills2_Mordecai.Sniper.Killer").SkillEffectPresentations[1].Description = "Reload Speed."
    obj("SkillDefinition","gd_skills2_Mordecai.Sniper.Killer").SkillEffectPresentations[1].bUseCustomNumberPlacement = False
    obj("SkillDefinition","gd_skills2_Mordecai.Rogue.FastHands").SkillEffectPresentations[0].Description = "Reload Speed."
    obj("SkillDefinition","gd_skills2_Mordecai.Rogue.FastHands").SkillEffectPresentations[0].bUseCustomNumberPlacement = False
    obj("SkillDefinition","gd_skills2_Mordecai.Rogue.OutForBlood").SkillDescription = "When Bloodwing strikes an enemy, you gain health based on the amount of damage done."
    obj("SkillDefinition","gd_skills2_Mordecai.Rogue.OutForBlood").SkillEffectPresentations[0].Description = "Percentage of damage converted to health: $NUMBER$."
    obj("SkillDefinition","gd_skills2_Mordecai.Gunslinger.LethalStrike").SkillDescription = "Increases Melee Damage.  Also, every melee attack has a 35% chance to be a Lethal Strike and deal extremely high damage."
    obj("SkillDefinition","gd_skills2_Mordecai.Gunslinger.LethalStrike").SkillEffectPresentations[0].Description = "Melee Damage."
    obj("SkillDefinition","gd_skills2_Mordecai.Gunslinger.LethalStrike").SkillEffectPresentations[0].bUseCustomNumberPlacement = False
    obj("SkillDefinition","gd_skills2_Mordecai.Sniper.Loaded").SkillEffectPresentations[0].Description = "Magazine Capacity."
    obj("SkillDefinition","gd_skills2_Mordecai.Sniper.Loaded").SkillEffectPresentations[0].bUseCustomNumberPlacement = False
    obj("SkillDefinition","gd_skills2_Mordecai.Sniper.CarrionCall").SkillDescription = "Shooting an enemy with a Sniper Rifle reduces the Cooldown of Bloodwing."
    obj("SkillDefinition","gd_skills2_Mordecai.Sniper.CarrionCall").SkillEffectPresentations[0].Description = "Cooldown reduction per hit: $NUMBER$ (in seconds)."
    obj("SkillDefinition","gd_skills2_Mordecai.Rogue.AerialImpact").SkillDescription = "Attacks from Bloodwing can Daze enemies, reducing their movement speed and accuracy."
    obj("SkillDefinition","gd_skills2_Mordecai.Rogue.AerialImpact").SkillEffectPresentations[0].Description = "Chance to Daze (vs an equal level enemy)."
    obj("SkillDefinition","gd_skills2_Mordecai.Rogue.AerialImpact").SkillEffectPresentations[0].bUseCustomNumberPlacement = False
    obj("SkillDefinition","gd_skills2_Mordecai.Rogue.Ransack").SkillEffectPresentations[0].Description = "Chance to drop an additional item."
    obj("SkillDefinition","gd_skills2_Mordecai.Rogue.Ransack").SkillEffectPresentations[0].bUseCustomNumberPlacement = False
    obj("SkillDefinition","gd_skills2_Mordecai.Gunslinger.Predator").SkillDescription = "Reduces the cooldown of your pet Bloodwing."
    obj("SkillDefinition","gd_skills2_Mordecai.Gunslinger.HairTrigger").SkillEffectPresentations[0].Description = "Fire Rate."
    obj("SkillDefinition","gd_skills2_Mordecai.Gunslinger.HairTrigger").SkillEffectPresentations[0].bUseCustomNumberPlacement = False
    obj("SkillDefinition","gd_skills2_Mordecai.Gunslinger.HairTrigger").SkillEffectPresentations[1].Description = "Magazine Size."
    obj("SkillDefinition","gd_skills2_Mordecai.Gunslinger.HairTrigger").SkillEffectPresentations[1].bUseCustomNumberPlacement = False
    obj("SkillDefinition","gd_skills2_Mordecai.Rogue.BirdOfPrey").SkillDescription = "Increases the number of targets Bloodwing can attack before returning."
    obj("SkillDefinition","gd_skills2_Mordecai.Rogue.BirdOfPrey").SkillEffectPresentations[0].Description = "Bloodwing can attack up to $NUMBER$ targets."
    obj("SkillDefinition","gd_skills2_Mordecai.Gunslinger.Relentless").SkillDescription = "Killing an enemy increases your Fire Rate and gives every bullet fired a 25% chance to be a Killer Shot and deal additional damage.  This effect lasts a few seconds."
    obj("SkillDefinition","gd_skills2_Mordecai.Gunslinger.Relentless").SkillEffectPresentations[0].Description = "Fire Rate."
    obj("SkillDefinition","gd_skills2_Mordecai.Gunslinger.Relentless").SkillEffectPresentations[0].bUseCustomNumberPlacement = False
    obj("SkillDefinition","gd_skills2_Mordecai.Gunslinger.Relentless").SkillEffectPresentations[1].Description = "Killer Shot damage."
    obj("SkillDefinition","gd_skills2_Mordecai.Gunslinger.Relentless").SkillEffectPresentations[1].bUseCustomNumberPlacement = False

        # Artifacts

            # Lilith
    obj("SkillDefinition","gd_Skills_Lilith.ActionElemental.IncendiaryReturn").SkillDescription = "Phasewalk deals Incendiary Damage."
    obj("SkillDefinition","gd_Skills2_Lilith.ActionElemental.IncendiaryReturn").SkillDescription = "Phasewalk deals Incendiary Damage."
    obj("SkillDefinition","gd_Skills_Lilith.ActionElemental.ShockingReturn").SkillDescription = "Phasewalk deals Shock Damage."
    obj("SkillDefinition","gd_Skills2_Lilith.ActionElemental.ShockingReturn").SkillDescription = "Phasewalk deals Shock Damage."  
    obj("SkillDefinition","gd_Skills_Lilith.ActionElemental.CorrosiveReturn").SkillDescription = "Phasewalk deals Corrosive Damage."
    obj("SkillDefinition","gd_Skills2_Lilith.ActionElemental.CorrosiveReturn").SkillDescription = "Phasewalk deals Corrosive Damage."  
    obj("SkillDefinition","gd_Skills_Lilith.ActionElemental.ExplosiveReturn").SkillDescription = "Phasewalk deals Explosive Damage."
    obj("SkillDefinition","gd_Skills2_Lilith.ActionElemental.ExplosiveReturn").SkillDescription = "Phasewalk deals Explosive Damage."  

            # Brick
    obj("SkillDefinition","gd_Skills_Brick.ActionElemental.IncendiaryPunch").SkillDescription = "Brick's punch deals Incendiary Damage."
    obj("SkillDefinition","gd_Skills2_Brick.ActionElemental.IncendiaryPunch").SkillDescription = "Brick's punch deals Incendiary Damage."
    obj("SkillDefinition","gd_Skills_Brick.ActionElemental.ShockingPunch").SkillDescription = "Brick's punch deals Shock Damage."
    obj("SkillDefinition","gd_Skills2_Brick.ActionElemental.ShockingPunch").SkillDescription = "Brick's punch deals Shock Damage."
    obj("SkillDefinition","gd_Skills_Brick.ActionElemental.CorrosivePunch").SkillDescription = "Brick's punch deals Corrosive Damage."
    obj("SkillDefinition","gd_Skills2_Brick.ActionElemental.CorrosivePunch").SkillDescription = "Brick's punch deals Corrosive Damage."
    obj("SkillDefinition","gd_Skills_Brick.ActionElemental.ExplosivePunch").SkillDescription = "Brick's punch deals Explosive Damage."
    obj("SkillDefinition","gd_Skills2_Brick.ActionElemental.ExplosivePunch").SkillDescription = "Brick's punch deals Explosive Damage."

            # Mordecai
    obj("SkillDefinition","gd_skills_Mordecai.ActionElemental.FireWing").SkillDescription = "The Bloodwing deals Incendiary damage."
    obj("SkillDefinition","gd_skills2_Mordecai.ActionElemental.FireWing").SkillDescription = "The Bloodwing deals Incendiary damage."
    obj("SkillDefinition","gd_skills_Mordecai.ActionElemental.ShockWing").SkillDescription = "The Bloodwing deals Shock damage."
    obj("SkillDefinition","gd_skills2_Mordecai.ActionElemental.ShockWing").SkillDescription = "The Bloodwing deals Shock damage."
    obj("SkillDefinition","gd_skills_Mordecai.ActionElemental.AcidWing").SkillDescription = "The Bloodwing deals Corrosive Damage."
    obj("SkillDefinition","gd_skills2_Mordecai.ActionElemental.AcidWing").SkillDescription = "The Bloodwing deals Corrosive Damage."
    obj("SkillDefinition","gd_skills_Mordecai.ActionElemental.ExplosiveWing").SkillDescription = "The Bloodwing deals Explosive damage."
    obj("SkillDefinition","gd_skills2_Mordecai.ActionElemental.ExplosiveWing").SkillDescription = "The Bloodwing deals Explosive damage."

            # Roland
    obj("SkillDefinition","gd_skills_Roland.ActionElemental.Scorpio_FireBolt").SkillDescription = "The Scorpio deals Incendiary Damage."
    obj("SkillDefinition","gd_skills2_Roland.ActionElemental.Scorpio_FireBolt").SkillDescription = "The Scorpio deals Incendiary Damage."
    obj("SkillDefinition","gd_skills_Roland.ActionElemental.Scorpio_ShockBolt").SkillDescription = "The Scorpio deals Shock damage."
    obj("SkillDefinition","gd_skills2_Roland.ActionElemental.Scorpio_ShockBolt").SkillDescription = "The Scorpio deals Shock damage."
    obj("SkillDefinition","gd_skills_Roland.ActionElemental.Scorpio_CorrosiveBolt").SkillDescription = "The Scorpio deals Corrosive damage."
    obj("SkillDefinition","gd_skills2_Roland.ActionElemental.Scorpio_CorrosiveBolt").SkillDescription = "The Scorpio deals Corrosive damage."
    obj("SkillDefinition","gd_skills_Roland.ActionElemental.Scorpio_ExplosiveBolt").SkillDescription = "The Scorpio deals Explosive Damage."
    obj("SkillDefinition","gd_skills2_Roland.ActionElemental.Scorpio_ExplosiveBolt").SkillDescription = "The Scorpio deals Explosive Damage."




    # Itempools

        # Shops
    obj("ItemPoolDefinition","gd_itempools_Shop.Items.shoppool_FeaturedItem_WeaponMachine").BalancedItems.append(current_obj.BalancedItems[5])
    obj("ItemPoolDefinition","gd_itempools_Shop.Items.shoppool_FeaturedItem_WeaponMachine").BalancedItems[(len(current_obj.BalancedItems)) - 1].InvBalanceDefinition = obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_SupportMachineGun")
    obj("ItemPoolDefinition","gd_itempools_Shop.Items.shoppool_Weapons_flatChance").BalancedItems.append(current_obj.BalancedItems[5])
    obj("ItemPoolDefinition","gd_itempools_Shop.Items.shoppool_Weapons_flatChance").BalancedItems[(len(current_obj.BalancedItems)) - 1].InvBalanceDefinition = obj("InventoryBalanceDefinition","gd_itemgrades.Weapons.ItemGrade_Weapon_SupportMachineGun")


        # Misc
    obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades.append(obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[9])
    obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[(len(current_obj.Grades)) - 1].GameStageRequirement.MinGameStage = 53
    obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[(len(current_obj.Grades)) - 1].GameStageRequirement.MaxGameStage = 100
    obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Explosive").Grades.append(obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[10])
    obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Incendiary").Grades.append(obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[10])
    obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Shock").Grades.append(obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[10])
    obj("InteractiveObjectBalanceDefinition","gd_balance_objects.FuelTanks.ObjectGrade_ExplodingFuelTank").Grades.append(obj("InteractiveObjectBalanceDefinition","gd_balance_objects.Barrels.ObjectGrade_ExplodingBarrels_Corrosive").Grades[10])

    obj("InteractiveObjectBalanceDefinition","dlc3_gd_explosives.SeaMine.BalanceDef_SeaMine").Grades[5].GameStageRequirement.MaxGameStage = 100


    obj("ItemPoolDefinition","gd_itempools.CrimsonLance.Infantry_Weapons").BalancedItems[1].bDropOnDeath = True
    obj("ItemPoolDefinition","gd_itempools.CrimsonLance.Infantry_Weapons_Badass").BalancedItems[0].bDropOnDeath = True
    obj("ItemPoolDefinition","dlc3_gd_itempools.CrimsonLance.Infantry_Weapons_Badass_enhance").BalancedItems[0].bDropOnDeath = True


    obj("PopulationDefinition","dlc3_gd_population_enemies.Drifters.DrifterSquad_Drifter").ActorArchetypeList.append(obj("PopulationDefinition","dlc3_gd_population_enemies.Drifters.DrifterSquad_BadassDrifter").ActorArchetypeList[0])
    obj("PopulationDefinition","dlc3_gd_population_enemies.Drifters.DrifterSquad_Drifter").ActorArchetypeList[(len(current_obj.ActorArchetypeList)) - 1].Probability.InitializationDefinition = obj("AttributeInitializationDefinition","gd_Balance.WeightingPlayerCount.Enemy_MajorUpgrade_PerPlayer")
    obj("PopulationDefinition","dlc3_gd_population_enemies.Drifters.DrifterSquad_Drifter").ActorArchetypeList[(len(current_obj.ActorArchetypeList)) - 1].Probability.BaseValueScaleConstant = 0.08
    obj("PopulationDefinition","dlc3_gd_population_enemies.Drifters.DrifterSquad_Drifter").ActorArchetypeList[(len(current_obj.ActorArchetypeList)) - 1].MaxActiveAtOneTime.InitializationDefinition = obj("AttributeInitializationDefinition","gd_Balance.WeightingPlayerCount.Enemy_MajorUpgrade_PerPlayer")

    obj("InteractiveNPCDefinition","gd_MissionNPCs.Taylor_Kobb").Mesh.Materials.append(obj("MaterialInstanceConstant","gd_Kobb_Brothers.Material.Mat_Janis_Body"))
    obj("InteractiveNPCDefinition","gd_MissionNPCs.Taylor_Kobb").Mesh.Materials.append(obj("MaterialInstanceConstant","gd_Kobb_Brothers.Material.Mat_Janis_Head"))
    obj("ItemDefinition","dlc1_MissionData.ItemDefs.ID_WereSkagSample").NonCompositeStaticMesh = obj("StaticMesh","Health_items.Mesh.HealthOil_01")
    obj("ItemDefinition","Z1_MissionData.ItemDefs.ID_JackProof").NonCompositeStaticMesh = obj("StaticMesh","UP_Assets.Mesh.mesh_jack_eyeball")
    obj("ItemDefinition","dlc1_MissionData.ItemDefs.ID_Eggs").NonCompositeStaticMesh = obj("StaticMesh","UP_Assets.Mesh.mesh_bloodwing_egg")

    obj("InteractiveObjectDefinition","Z0_MissionData.MissionDirectors.MD_SubstationNote").ExtraBehaviorSets[0].OnUsedBy.clear()


    #Code by EvanDeadlySins
        # Fixed typos
    obj("AttributePresentationDefinition","gd_tunercuffs.ManufacturerMaterials.Material_Anshin_1:AttributePresentationDefinition_1").Description = "Equip to throw Transfusion Grenades." # "thow" to "throw"
    obj("AIPawnBalanceDefinition","gd_Balance_Enemies_Creatures.Rakk.Pawn_Balance_Rakk_ShockChampion").Grades[1].GradeModifiers.DisplayName = "BadMutha Shock Rakk" # removes extra space
    obj("AIPawnBalanceDefinition","gd_Balance_Enemies_Creatures.Scythids.Pawn_Balance_Scythid_Giant").Grades[1].GradeModifiers.DisplayName = "Mammoth Scythid" # "Mommoth" to "Mammoth"
    obj("AIPawnBalanceDefinition","dlc4_gd_Balance_Enemies.SteeleTrap.Pawn_Balance_SteeleTrap").Grades[0].GradeModifiers.DisplayName = "Commandant Steele-Trap" # "Comandant" to "Commandant"
    obj("AIPawnBalanceDefinition","dlc4_gd_Balance_Enemies.SteeleTrap.Pawn_Balance_SteeleTrap2").Grades[0].GradeModifiers.DisplayName = "Commandant Steele-Trap"
    obj("WeaponNamePartDefinition","gd_weap_patrol_smg.Title.TitleM_Maliwan1_HellFire").PartName = "Hellfire" # "HellFire" to "Hellfire"

        # Enemies set to be 2 levels higher than GameStage were only set to be 1 level higher
    obj("AttributeDefinition","gd_Balance.EnemyLevel.EnemyLevel_GameStage_plus2").ValueResolverChain[0].Argument.BaseValueConstant = 2

        # Pup Skags can now spawn on Playthrough 2
    obj("AIPawnBalanceDefinition","gd_Balance_Enemies_Creatures.Skags.Pawn_Balance_Skag_Pup").Grades[1].GameStageRequirement.MaxGameStage = 33
    obj("AIPawnBalanceDefinition","gd_Balance_Enemies_Creatures.Skags.Pawn_Balance_Skag_Pup").Grades[1].GameStageRequirement.MinGameStage = 31



@hook(
    hook_func="WillowGame.WillowPlayerReplicationInfo:AddCurrencyOnHand",
    hook_type=Type.PRE,
)
def AddCurrencyOnHand(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    if obj.GetCurrencyOnHand() + __args.AddValue > 2147483647:
        __args.AddValue = 2147483647 - obj.GetCurrencyOnHand()


# This was made by RedxYeti
@hook("Engine.PlayerController:StartFire", Type.POST)
def ReloadFix(obj:UObject, *_) -> None:
    if not obj or not obj.Pawn or not obj.Pawn.Weapon:
        return
    weapon = obj.Pawn.Weapon
    
    if weapon and weapon.NeedToReload():
        weapon.BeginReload(0)


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
    hooks=[on_startgame, AddCurrencyOnHand],
    commands=[],
     # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/UnofficialPatchSDK.json"),
)

logging.info(f"Unofficial Patch SDK Loaded: {__version__}, {__version_info__}")