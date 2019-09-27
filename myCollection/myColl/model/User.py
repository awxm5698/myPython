import datetime
from model.JsonFile import JsonFile
from model.Md5 import Md5


class User(JsonFile):

    def __init__(self, file_name):
        super(User, self).__init__(file_name)
        self.my_md5 = Md5.my_md5

    def new_user_info(self, login_name, password):
        user_id = self.get_new_user_id()
        user_info = {
            "user_id": user_id,
            "login_name": login_name,
            "password": self.my_md5(password),
            "is_deleted": False,
            "create_time": str(datetime.datetime.now()),
            "update_time": str(datetime.datetime.now())
        }
        return user_info

    def get_new_user_id(self):
        user_info = self.read_json_file()
        user_count = len(user_info)
        return user_count+1

    def get_user_info(self, key, name):
        user_info = self.read_json_file()
        is_exist = False
        for user in user_info:
            if user.get(key) == name:
                is_exist = True
                return user
        if not is_exist:
            return None

    def create_new_user(self, login_name, password):
        new_user = self.new_user_info(login_name, password)
        if self.get_user_info("login_name", login_name) is None:
            self.add_data_to_json_file(new_user)

    def user_login(self, login_name, password):
        user = self.get_user_info("login_name", login_name)
        is_login = False
        if user is not None:
            psd = user.get("password")
            if psd == self.my_md5(password):
                is_login = True
                return user
        if not is_login:
            return "user or password is wrong"

    def update_user_password(self, login_name, old_password, new_password):
        info = self.get_user_info("login_name", login_name)
        new_info = self.get_user_info("login_name", login_name)
        if new_info is not None and new_info.get("password") == self.my_md5(old_password):
            new_info["password"] = self.my_md5(new_password)
            new_info["update_time"] = str(datetime.datetime.now())
            self.update_data_on_json_file(info, new_info)
            return "Update success"
        else:
            return "user or password is wrong"

