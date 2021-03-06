from classes.game import Person,bcolors
from classes.magic import Spell
from classes.inventory import Item

print("\n\n")
print("NAME                HIT POINTS                  MAGIC POINTS")
print("               _________________________        __________ ")
print(bcolors.BOLD+ "valos: "+
      "400/460|"+bcolors.OKGREEN+"████████████████████     "+bcolors.ENDC+"| "+bcolors.BOLD+
      "65/65|"+bcolors.OKBLUE+"██████████"+bcolors.ENDC+ "| ")
print("               _________________________        __________ ")
print(bcolors.BOLD+ "valos: "+
      "460/460|"+bcolors.OKGREEN+"█████████████████████████"+bcolors.ENDC+"| "+bcolors.BOLD+
      "65/65|"+bcolors.OKBLUE+"██████████"+bcolors.ENDC+ "| ")
print("               _________________________        __________ ")
print(bcolors.BOLD+ "valos: "+
      "460/460|"+bcolors.OKGREEN+"█████████████████████████"+bcolors.ENDC+"| "+bcolors.BOLD+
      "65/65|"+bcolors.OKBLUE+"██████████"+bcolors.ENDC+ "| ")

print("\n\n")
#black magic
fire=Spell("Fire",10,100,"black")
thunder=Spell("Thunder",10,100,"black")
blizzard=Spell("Blizzard",10,100,"black")
meteor=Spell("Meteor",20,200,"black")
quake=Spell("Quake",14,140,"black")
#whitemagic
cure=Spell("Cure",12,120,"white")
cura=Spell("Cura",20,200,"white")

#Items
potion=Item("Potion","potion","Heals 50 points",50)
hipotion=Item("Hi-Potion","potion","Heals 100 points",100)
superpotion=Item("Super Potion","potion","Heals 500 points",500)
elixer=Item("Elixer","elixer","Fully restores health of one party member",566)
hielixer=Item("MegaElixer","elixer","Fully restores party's health power and magic power",7978)
grenade=Item("Grenade","attack","Deals 500 damage",567)
#people
player_spells=[fire,thunder,blizzard,meteor,cure,cura]
player_items=[{"item":potion,"quantity":15},
              {"item":hipotion,"quantity":5},
              {"item":superpotion,"quantity":5},
              {"item":elixer,"quantity":5},
              {"item":hielixer,"quantity":2},
              {"item":grenade,"quantity":5}]
player=Person(460,65,60,34,player_spells,player_items)
enemy=Person(1200,65,45,25,[],[])
running = True
i=0
print(bcolors.FAIL+bcolors.BOLD+"Enemy attack dem"+bcolors.ENDC)
while running:
    print("======================")
    player.choose_action()
    choice=input("chagua: ")
    index=int(choice)-1
    if index == 0:
        dmg=player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for",dmg,"points of damage.")
    elif index==1:
        player.choose_magic()
        magic_choice=int(input("choose magic: "))-1
        if magic_choice==-1:
            continue

        spell=player.magic[magic_choice]
        magic_dmg=spell.generate_damage()


        current_mp=player.get_mp()
        if spell.cost>current_mp:
            print(bcolors.FAIL+"\a not enough magic points\n"+bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)
        if spell.type=="white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n"+spell.name+ " heals for",str(magic_dmg),"Health power"+bcolors.ENDC)
        elif spell.type=="black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE+ "\n" + spell.name + " inflicts",str(magic_dmg),"damage points"+bcolors.ENDC)
    elif index==2:
        player.choose_item()
        item_choice=int(input("Choose item: "))-1

        if item_choice==-1:
            continue
        item=player.items[item_choice]["item"]
        if player.items[item_choice]["quantity"]==0:
            print(bcolors.FAIL+"\n"+"None left..."+bcolors.ENDC)
            continue

        player.items[item_choice]["quantity"]-=1


        if item.type=="potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN+"\n"+item.name+" heals for",str(item.prop),"Health points"+bcolors.ENDC)
        elif item.type=="elixer":
            player.hp=player.maxhp
            player.mp=player.maxmp
            print(bcolors.OKGREEN+"\n"+item.name+" fully restores health power and magic power"+bcolors.ENDC)
        elif item.type=="attack":
            enemy.take_damage(item.prop)
            print(bcolors.FAIL+"\n"+item.name+" causes"+str(item.prop)+" damage points"+bcolors.ENDC)
    enemy_choice=1
    enemy_dmg=enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for",enemy_dmg)

    print("-------------------")
    print("Enemy hit points:",bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print("Player health power:",bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC + "\n")
    print("Player magic power:",bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) +  bcolors.ENDC + "\n")
    if enemy.get_hp()==0:
        print(bcolors.OKGREEN+bcolors.BOLD+"You win byach"+bcolors.ENDC)
        running=False
    elif player.get_hp()==0:
        print(bcolors.FAIL+"You lost bomboclaat"+bcolors.ENDC)
        running=False