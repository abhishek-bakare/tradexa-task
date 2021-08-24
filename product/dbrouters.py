from .models import Products


class ProductDBRouter:
    '''
    class for creating new db routing
    '''

    # route app label is the label of app
    route_app_labels = {'product'}

    def db_for_read(self, model, **hints):
        '''
        this function suggest new db that should used for read operations
        hints are used for communicating additional information to the router
        '''
        if model._meta.app_label in self.route_app_labels:

            # return new db name
            return 'product_db'
        return None

    def db_for_write(self, model, **hints):
        '''
         this function suggest new db that should used for write operations
        '''
        if model._meta.app_label in self.route_app_labels:
            return 'product_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        '''
        this function i write for if any relation operation to be perform like foreignkey
        '''
        if (obj1._meta.app_label in self.route_app_labels or
        obj2._meta.app_label in self.route_app_labels):

            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        '''
        this is for migration operation to our new db
        '''
        if app_label in self.route_app_labels:
            return db == 'product_db'
        return None

