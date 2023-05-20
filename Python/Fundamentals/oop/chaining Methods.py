class User:
    def __init__(self, first, last, email, age,):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.gold_card_points)
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
    
    def spend_points(self, amount):
        amount=self.gold_card_points - amount
        print (amount)
herculus = User("chedi", "mola", "hirakel@gmail.com", "20")
ska = User("Mohamed", "Ali", "mouhamed.ali@gmail.com", "50")
miou = User("Mariem", "So", "mariem.so@gmail.com", "32")
herculus.enroll()
herculus.spend_points(50)
ska.enroll()
ska.spend_points(80)
ska.display_info()
miou.display_info()
