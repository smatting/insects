insert into insects_process(name, kind) values ('stefan-test', 'manual');

drop table if exists foo;
create temp table foo as (
    select
        'https://storage.googleapis.com/eco1/frames/' || id_new as url,
        time_stamp as timestamp,
        1 as process_id,
        row_number() over (partition by event_time_stamp) as clip_id,
        id_new
    from
        src_frame_newname
);

truncate insects_frame cascade;
insert into insects_frame (url, timestamp, process_id) (
    select
        url,
        timestamp,
        process_id
    from
        foo
);

truncate insects_clip cascade;
insert into insects_clip (process_id, id)
select
    1 as process_id,
    x.clip_id as id
from
    (
    select distinct  clip_id from foo
    ) x
;

truncate insects_clip_frames;
insert into insects_clip_frames (clip_id, frame_id)
select
    foo.clip_id,
    f.id as frame_id
from
    insects_frame f
    left join foo
        on ('https://storage.googleapis.com/eco1/frames/' || foo.id_new) = f.url


-- 2020-01-12


drop table if exists auth_group cascade;
drop table if exists auth_group_permissions cascade;
drop table if exists auth_permission cascade;
drop table if exists auth_user cascade;
drop table if exists auth_user_groups cascade;
drop table if exists auth_user_user_permissions cascade;
drop table if exists django_admin_log cascade;
drop table if exists django_content_type cascade;
drop table if exists django_migrations cascade;
drop table if exists django_session cascade;
drop table if exists insects_appearance cascade;
drop table if exists insects_boundingbox cascade;
drop table if exists insects_classification cascade;
drop table if exists insects_classificationvalue cascade;
drop table if exists insects_clip cascade;
drop table if exists insects_clip_frames cascade;
drop table if exists insects_frame cascade;
drop table if exists insects_process cascade;
drop table if exists insects_species cascade;
drop table if exists insects_tracking cascade;



with
foo as (
    select
        'https://storage.googleapis.com/eco1/frames/' || id_new as url,
        time_stamp as timestamp
    from
        public.src_frame_newname
)
insert into insects_frame (url, timestamp) (
    select
        url,
        timestamp
    from
        foo
);
