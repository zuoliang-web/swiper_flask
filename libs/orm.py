

from flask_sqlalchemy import SQLAlchemy,BaseQuery
from sqlalchemy.orm import loading
from sqlalchemy.orm import persistence

class Query(BaseQuery):

    #def get_or_create(self,model,ident,):
        
        # 先判断传入的id，是否在能在数据库中查找到
        # 1. 先调用get方法 ，如果没有值，
        # 2. 没值，调用create方法

        # orm_id = kwargs.get('id')
        
        #is_value = self._get_impl(ident, loading.load_on_pk_identity)
        #print('isvalue',is_value)
        #if is_value:
        #    print('我是一车')
        #else:
        #    istance = model(**)
        #    super(Query,self).add()
        #    print('我喜欢你')
        #return self._get_impl(ident, loading.load_on_pk_identity)

    def get_or_create(self,session, model, **kwargs):
        instance = self._get_impl(kwargs.get('id'), loading.load_on_pk_identity)
        if instance:
            return instance
        else:
            instance = model(**kwargs)
        
            session.add(instance)
            session.commit()
            return instance


    def update_or_create(self, values, synchronize_session="evaluate", update_args=None):
        print(values)
        # 如果是修改的话执行：
        # update_args = update_args or {}
        # update_op = persistence.BulkUpdate.factory(
        #     self, synchronize_session, values, update_args
        # )
        # update_op.exec_()
        # return update_op.rowcount       

# def patch_monkey():
#     BaseQuery.get_or_create = types.MethodType(get_or_create,BaseQuery)
