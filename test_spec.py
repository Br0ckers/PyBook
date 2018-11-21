from mamba import description, context, it
import apple

with description('Database Management') as self:
    with context('find a user'):
        with it('returns a user'):
            assert(apple.find_one_user("joe bloggs")) == "joe bloggs"

with description('Database Management') as self:
    with context('find all users'):
        with it('returns all users'):
            assert(apple.find_user_count()) > 0

with description('Database Management') as self:
    with context('finsert a user'):
        with it('inserts a user'):
            apple.insert_one_user()
            assert(apple.find_one_user("winston wolf")) == "winston wolf"


with description('Database Management') as self:
    with context('delete a user'):
        with it('delete a user'):
            apple.delete_one_user("winston wolf")
            assert(apple.find_one_user("winston wolf")) == None
