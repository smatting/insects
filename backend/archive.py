
# def foo():
#     # cursor = connection.cursor()
#     # cursor.execute('select count(*) from insects_frame')
#     # return cursor.fetchall()
#     tbegin = datetime.datetime(2019, 11, 1)
#     tend = datetime.datetime(2019, 11, 15)
#     return get_subsample(tbegin, tend)

def get_frame(frame_id):
    cursor = connection.cursor()
    q = '''
        select
            id,
            timestamp,
            url
        from
            insects_frame
        where id = %s
    '''
    cursor.execute(q, (frame_id, ))
    (id_, timestamp, url) = cursor.fetchone()
    return make_frame(id_, timestamp, url)

# def collection_create(name):
#     '''
#     Create empty connection
#     '''
#     now = datetime.datetime.now()
#     coll = models.Collection(name, date_created=now)
#     coll.save()
#     return coll


# def collection_add_subsample(coll_id, tbegin, tend, nsamples):
#     '''
#     Add subsample to a collection
#     '''
#     coll = models.Collection.objects.get(id=coll_id)
#     n, frames = frames_fetch_sub(tbegin, tend, lambda n: equidx(n, nsamples))
#     ids_ = [f['id'] for f in frames]
#     coll.frames.add(*ids_)

