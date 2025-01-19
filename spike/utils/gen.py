impor random

class Generate:
    def __init__(self, name: str, nums: bool, schars: bool):
        """user defined"""
        self.name = name
        self.use_nums = nums
        self.use_schars = schars

        """me defined"""
        self.len = 15
        self.pwd_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.pwd = ""

    def set_pwd_chars(self):
        nums = "1234567890"
        schars = "!@#$%^&*()"

        if self.use_nums:
            self.pwd_chars += nums

        if self.use_schars:
            self.pwd_chars += schars

    def generate(self):
        """generate password based on parameters"""
        self.set_pwd_chars()
        for i in range(self.len):
            self.pwd += random.choice(self.pwd_chars)
