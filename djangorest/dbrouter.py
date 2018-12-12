class EquipmentRouter:
    """
    A router to control all database operations on models in the
    equipment application.
    """
    def __init__(self):
        self.equipment_models = ['Lot', 'Customer', 'Sale']

    def db_for_read(self, model, **hints):
        """
        Attempts to read equipment models go to equipment db.
        """
        if model._meta.object_name in self.equipment_models:
            return 'equipment'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model._meta.object_name in self.equipment_models:
            return 'equipment'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if obj1._meta.app_label == 'equipment' or \
           obj2._meta.app_label == 'equipment':
           return True
        if obj1._meta.app_label == 'app' or \
           obj2._meta.app_label == 'app':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        return db == 'default'
