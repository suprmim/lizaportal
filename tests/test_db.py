#! /usr/bin/env python2
# encoding: utf8

import py_path
from utils.db import get_db_session
from models.testmodel.sa_models import Test as TestModel


if __name__ == "__main__":

    ## Init session
    session = get_db_session(echo=True)

    ## Get list:
    print session.query(TestModel).all()

    ## remove all:
    print "REMOVING@!!!"
    print session.using_bind('master').query(TestModel).delete()
    print "<<<REMOVING@!!!"

    ## Get clear list:
    print session.query(TestModel).all()

    ## Create an element:
    tt = TestModel(name='test1')
    session.add(tt)
    tt = TestModel(name='test2')
    session.add(tt)

    session.commit()

    ## Get all new elements:
    print session.query(TestModel).all()


