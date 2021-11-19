class ProductRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'product_data':
            return 'proucts_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'product_data':
            return 'proucts_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'product_data' or \
                obj2._meta.app_label == 'product_data':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'product_data':
            return db == 'proucts_db'
        return None


class UserRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'user_data':
            return 'users_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'user_data':
            return 'users_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'user_data' or \
                obj2._meta.app_label == 'user_data':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'user_data':
            return db == 'users_db'
        return None


class PostRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'post_data':
            return 'post_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'post_data':
            return 'post_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'post_data' or \
                obj2._meta.app_label == 'post_data':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'post_data':
            return db == 'post_db'
        return None