class User:
    def __init__(self, first, last, email, age):
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
        return self
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
    def spend_points(self, amount):
        amount=self.gold_card_points - amount
        return self

herculus = User("chedi", "mola", "hirakel@gmail.com", "20")
ska = User("Mohamed", "Ali", "mouhamed.ali@gmail.com", "50")
miou = User("Mariem", "So", "mariem.so@gmail.com", "32")
herculus.display_info().enroll().spend_points(50).display_info()
ska.display_info().enroll().spend_points(80).display_info()
miou.display_info().enroll().spend_points(40).display_info()