from project.hero import Hero
from project.elf import Elf
from project.wizard import Wizard
from project.knight import Knight
from project.muse_elf import MuseElf
from project.dark_knight import DarkKnight
from project.dark_wizard import DarkWizard
from project.soul_master import SoulMaster
from project.blade_knight import BladeKnight


heroes = [

    Hero('hero', 1),
    Elf('elf', 1),
    Wizard('wizard', 1),
    Knight('knight', 1),
    MuseElf('muse_elf', 1),
    DarkWizard('dark_wizard', 1),
    DarkKnight('dark_knight', 1),
    SoulMaster('soul_master', 1),
    BladeKnight('blade_knight', 1),
]


for h in heroes:
    print(h.__class__.__name__, h, h.__dict__)