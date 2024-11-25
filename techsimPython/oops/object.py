class Mobile:
    def calling(self):
        print("calling feature")
        # print("argument", self)
    def attributes(self, ram, rom):
        self.ram = ram
        self.rom = rom
    
# obj = Mobile()
# obj.calling()
# # print(obj)

# mobile = Mobile()
# mobile.attributes() 
# print(mobile.ram)
# print(mobile.rom)
# mobile.camera = "2"
# print(mobile.camera)

# test_mob = Mobile()
# test_mob.attributes()
# print(test_mob.ram)

mobile = Mobile()
mobile.attributes("16GB","128GB")
print(mobile.ram, mobile.rom)
